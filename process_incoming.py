from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import requests

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_list
    })

    response=r.json()["embeddings"]
    print(response)
    return response

df=joblib.load("embedings.joblib")

incoming_query=input("Ask a Question: ")
question_embedding=create_embedding([incoming_query])[0]

similarities=cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()

