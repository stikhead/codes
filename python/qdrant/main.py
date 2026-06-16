from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

client = QdrantClient(":memory:")

client.create_collection(
    collection_name="my_first_collection",
    vectors_config=VectorParams(
        size=4,
        distance=Distance.COSINE
    )


)


print("collection created")

points = [
    PointStruct(
        id=1,
        vector=[0.1, 0.2, 0.3, 0.4],
        payload={"city": "london", "weather": "rainy"}
    ),
    PointStruct(
        id=2, 
        vector=[0.8, 0.9, 0.9, 0.8], 
        payload={"city": "Dubai", "weather": "sunny"}
    ),
    PointStruct(
        id=3, 
        vector=[0.2, 0.1, 0.3, 0.5], 
        payload={"city": "Seattle", "weather": "rainy"}
    )
]

client.upsert(
    collection_name="my_first_collection",
    points=points
)
print("Data inserted!")
search_query = [0.2, 0.2, 0.3, 0.4 ]
search_results = client.query_points(
    collection_name="my_first_collection",
    query=search_query,
    limit=2
)

print("search results:")
for r in search_results.points: 
    print(f"ID: {r.id}, Score: {r.score:.4f}, Payload: {r.payload}")