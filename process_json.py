#in this we will convert the json (text/sentences) to vectors using bge-m3 model of ollama

import requests
import os
import pandas as pd
import json
import joblib

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_list
    })

    embedding=r.json()["embeddings"]
    return embedding

jsons=os.listdir("jsons")  #take all the jsons

my_dict=[]
chunk_id=0

for json_file in jsons:
    with open(f"jsons/{json_file}")as f:
        content=json.load(f)
    print(f"Creating Embeddings for {json_file}")
    embeddings=create_embedding([c['text'] for c in content['chunks']])

    for i,chunk in enumerate(content['chunks']):
        chunk['chunk_id']=chunk_id
        chunk['embedding']=embeddings[i]
        chunk_id+=1
        my_dict.append(chunk)

df=pd.DataFrame.from_records(my_dict)

#save df
joblib.dump(df,"embeddings.joblib")