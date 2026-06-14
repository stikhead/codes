import torch
from transformers import AutoTokenizer, AutoModel

mode_name = "bert-base-multilingual-cased"
# tokenizer
tokenizer = AutoTokenizer.from_pretrained(mode_name)

# actual neural netowork
print("loading model into memory....")
model = AutoModel.from_pretrained(mode_name)

text = "hello world"

# tokenize, but tell hugging face to format it specifically for pytorch ("pt")
inputs = tokenizer(text, return_tensors="pt")
print(f"Token IDs shape: {inputs['input_ids'].shape}")
# push the numbers through neural network
# use torch.no_graf() to save memory bc we are just testing, not training
with torch.no_grad():
    output = model(**inputs)

# look at the output of final layer
print(output)
last_hidden_state = output.last_hidden_state
print(f"\nNeural Network Output Shape: {last_hidden_state.shape}")
print("The actual math for the first token ([CLS]):")
print(last_hidden_state[0][0][:5])