import math
import json

def dot(a: list[float], b: list[float]) -> float:
    "İki vektörün iç çarpımı"
    if len(a) != len(b):
        raise ValueError("Vektör boyutları eşit olmalıdır.")
    
    return sum(x * y for x, y in zip(a, b))

def norm(a: list[float]) -> float:
    "Bir vektörün Öklid normunu hesaplar."
    return math.sqrt(sum(x ** 2 for x in a))

def cosine(a: list[float], b: list[float]) -> float:
    "İki vektör arasındaki kosinüs benzerliğini hesaplar."
    norm_a = norm(a)
    norm_b = norm(b)
    
    if norm_a == 0.0 or norm_b == 0.0:
        raise ValueError("Sıfır vektörü için kosinüs benzerliği hesaplanamaz.")
        
    return dot(a, b) / (norm_a * norm_b)

with open ("scratch/embed.json") as f:
    data = json.load(f)

vectors = data["embeddings"]
A, B, C, D = vectors[0], vectors[1], vectors[2], vectors[3]

print(cosine(A,B))
print(cosine(A,C))
print(cosine(B,C))
print(cosine(A,D))