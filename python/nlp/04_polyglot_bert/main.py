import torch
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, DataCollatorWithPadding
from torch.utils.data import DataLoader
from torch.optim import AdamW
from pathlib import Path

data = {
    "sentence": ["Hello world", "How are you doing today?", "Python is fast", 
                 "नमस्ते दुनिया", "आज आप कैसे हैं?", "पायथन तेज है"],
    "label": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
hf = Dataset.from_pandas(df)

curr_dir = Path.cwd()
model_dir = curr_dir/"custom_polyglot_bert"
if not model_dir.exists():
    print("no directory, model doesnt exists, downloading from internet")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-multilingual-cased")
else:
    print("pretrained model found, loading it.....")
    tokenizer = AutoTokenizer.from_pretrained("./custom_polyglot_bert")
    model = AutoModelForSequenceClassification.from_pretrained("./custom_polyglot_bert", num_labels=2)

def tokenize_batch(batch):
    return tokenizer(
        batch["sentence"],
        max_length=12,
        truncation=True,
        padding=True
    )

tokenized_dataset = hf.map(tokenize_batch, batched=True)
tokenized_dataset = tokenized_dataset.remove_columns(["sentence"])
tokenized_dataset.set_format("torch")

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
train_dataloader = DataLoader(tokenized_dataset, batch_size=2, shuffle=True, collate_fn=data_collator)

optimizer = AdamW(model.parameters(), lr=5e-5)

epochs  = 3 
print("starting training...")
model.train()

for epoch in range(epochs):
    total_loss = 0

    for batch in train_dataloader:
        outputs = model(**batch)
        loss = outputs.loss

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_dataloader)
    print(f"epoch {epoch + 1}/ {epochs} | average loss: {avg_loss:.4f}")

save_dir = "./custom_polyglot_bert"

model.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)
print(f"success!, model and tokenizer saved in: {save_dir}")