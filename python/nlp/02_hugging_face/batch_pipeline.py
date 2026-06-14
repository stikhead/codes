from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, DataCollatorWithPadding
import pandas as pd
from torch.utils.data import DataLoader
from torch.optim import AdamW
# data = {
#     "english_sentence": ["Hello world", "How are you doing today?", "Python is fast"],
#     "hindi_sentence": ["नमस्ते दुनिया", "आज आप कैसे हैं?", "पायथन तेज है"]
# }

data = {
    "sentence": ["Hello world", "How are you doing today?", "Python is fast", "नमस्ते दुनिया", "आज आप कैसे हैं?", "पायथन तेज है"],
    "label": [0, 0, 0, 1, 1, 1] # 0 -> english, 1 -> hindi
}

df = pd.DataFrame(data)

# pandas into high speed hugging face dataset format
hf_dataset = Dataset.from_pandas(df)

# loading the tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

# vectorization function applies the padding and trunaction rules
def tokenize_batch(batch):
    return tokenizer(
        # batch["english_sentence"],
        batch["sentence"],
        padding=True,
        truncation=True,
        max_length=12, # hard limit on tensor size to protect vram
        # return_tensors="pt" # output strict pytorch tensors
    )

# apply the function to dataset using parallel processing
print("tokenizing dataset...")
tokenized_dataset = hf_dataset.map(tokenize_batch, batched=True)

print("\n---pipeline results----")
batch_input_ids = tokenized_dataset["input_ids"]
batch_attention_mask = tokenized_dataset["attention_mask"]

print(f"Batch Input IDs:\n{batch_input_ids}")
print(f"\nAttention Mask:\n{batch_attention_mask}")


from transformers import DataCollatorWithPadding
from torch.utils.data import DataLoader

# We remove the "sentence" column because GPUs cannot do math on strings.
tokenized_dataset = tokenized_dataset.remove_columns(["sentence"])

# Tell Hugging Face to strictly format the output as PyTorch tensors
tokenized_dataset.set_format("torch")

# Initialize the dynamic padder
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Create the PyTorch DataLoader (The Streaming Engine)
batch_size = 2 # Extremely small batch size just for testing
train_dataloader = DataLoader(
    tokenized_dataset, 
    shuffle=True, # Shuffle the data so the AI actually learns, not memorizes
    batch_size=batch_size, 
    collate_fn=data_collator # Use our dynamic padder
)

# Initialize model with 2-class classification head
print("loading sequence classification model...")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-multilingual-cased", num_labels=2)

# optimizer (the system component that adjusts the matrix weights)
optimizer = AdamW(model.parameters(), lr=5e-5)

# test the stream! Let's pull exactly ONE batch from the engine.
# print("\n--- Testing the DataLoader Stream ---")
# for batch in train_dataloader:
#     print(f"Shapes streaming to the GPU:")
#     # You will see the shape is [2, X], where 2 is our batch size, 
#     # and X is the longest sentence in this specific batch!
#     print({k: v.shape for k, v in batch.items()})
    
#     # We break immediately because we only want to test the first batch
    
for batch in train_dataloader:
    outputs = model(**batch)
    loss = outputs.loss # error rate
    logits = outputs.logits # raw prediction scores [scroe_for_0, score_for_1...]
    print(f"Current Batch Labels: {batch['labels'].tolist()}")
    print(f"Model Predictions (Logits):\n{logits}")
    print(f"Calculated Loss (Error): {loss.item():.4f}")

    # backward pass: calculate gradients and adjust the internal matrix weights
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    #     Current Batch Labels: [0, 0]
    # Model Predictions (Logits):
    # tensor([[-0.0290,  0.2105],
    #         [-0.0195, -0.0821]])
    # 1. The Labels: [0, 0] means both sentences in this batch were English.
    # 2. The Logits (The Guesses): This 2x2 matrix represents the raw mathematical scores the classification head generated.

    # Row 1 ([-0.0290,  0.2105]): The AI scored Index 0 (English) at -0.0290 and Index 1 (Hindi) at 0.2105. Because the score for Index 1 is higher, the AI's official guess was Hindi. It was wrong.
    # Row 2 ([-0.0195, -0.0821]): The AI scored Index 0 at -0.0195 and Index 1 at -0.0821. Because -0.0195 is mathematically larger than -0.0821, the AI guessed English. It was right.

    # 3. The Loss (0.7412): Because it got one wrong and one right, the Cross-Entropy Loss function calculated a moderate error penalty of 0.7412.
    # During the loss.backward() and optimizer.step() commands, PyTorch used that exact penalty to reach back into the 768-dimensional matrices and shift the floats slightly so that next time, it is less likely to guess Hindi for that first sentence.