from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer

print("loading the model..")
model = SentenceTransformer('all-MiniLM-L6-v2')

client = QdrantClient(":memory:")

client.create_collection(
    collection_name = "semantic_search",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

print("collection created")

documents = [
 {"id": 1, "text": "The quick brown fox jumps over the lazy dog.", "category": "animals"},
    {"id": 2, "text": "Qdrant is a database for storing high-dimensional vectors.", "category": "technology"},
    {"id": 3, "text": "Python is a popular programming language for data science and AI.", "category": "technology"},
    {"id": 4, "text": "Felines are small, carnivorous mammals often kept as pets.", "category": "animals"}   
]

points = []
for doc in documents:
    vector = model.encode(doc["text"]).tolist()

    points.append(
        PointStruct(
            id=doc["id"],
            vector=vector,
            payload={"text": doc["text"], "category": doc["category"]}
        )
    )


client.upsert(
    collection_name="semantic_search",
    points=points
)

query_text = "tell me about coding and machine learning"
print(f"searching for {query_text}")

query_vector = model.encode(query_text).tolist()

search_results = client.query_points(
    collection_name="semantic_search",
    query=query_vector,
    limit=2
)

for r in search_results.points:
    print(f"Score: {r.score:.4f} | Category: {r.payload['category']} | Text: {r.payload['text']}")