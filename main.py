#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
from ml import nlp
import uvicorn 

app=FastAPI()

@app.get("/")
def read_main():
    return{"message":"Hello World"}

@app.get("/article/{article_id}")
def analyze_article(article_id: int):
     return{"article_id":article_id}

#Performing simple arithmatic
@app.get("/article/{article_id}")
def analyze_article(article_id: int):
    return{"article_id":article_id, "previous_id": article_id-1}


# Adding new paraeter with default value None, for which no required parameter

@app.get("/article/{article_id}")
def analyze_article(article_id: int, q:str=None):
    return{"article_id":article_id, "q":q}

# Creatng a document and counting the number of entites
@app.get("/article/{article_id}")
def analyze_article(article_id: int, q:str=None):
    count=0
    if q:
        doc=nlp(q)
        count=len(doc.ents)
    return{"article_id":article_id, "q":q, "count":count}

if __name__=='__main__':
    uvicorn.run("main:app", port=8000, reload=True)

