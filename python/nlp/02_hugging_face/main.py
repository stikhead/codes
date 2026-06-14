from transformers import pipeline

# classifier = pipeline("sentiment-analysis")

# result = classifier("this movie was not good at all!")
# print(result)

from fastapi import FastAPI

app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.post("/predict")
async def predict(text):
    result = classifier(text)[0]
    return {"label": result["label"], "confidence": result["score"]}