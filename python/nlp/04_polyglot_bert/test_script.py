import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

print("Booting AI Engine...")
tokenizer = AutoTokenizer.from_pretrained("./custom_polyglot_bert")
model = AutoModelForSequenceClassification.from_pretrained("./custom_polyglot_bert", num_labels=2)

while(True):
    user_payload = input("enter a sentences")

    # def tokenize_payload(payload):
    #     return tokenizer(
    #         payload, 
    #         return_tensors="pt",
    #         max_length = 12,
    #         truncation=True,
    #         padding=True
    #     )

    tokenized = tokenizer(user_payload, return_tensors="pt")

    with torch.no_grad():
        output = model(**tokenized)

    print(output.logits)

    score = output.logits

    if(score[0][0] > score[0][1]):
        print("english sentence")
    else:
        print('hindi sentence')