from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from SentimentAnalysis.pipeline.stage_07_prediction import PredictionPipeline
from SentimentAnalysis.config.configuration import ConfigurationManager
from SentimentAnalysis.logging import logger
from pathlib import Path


text:str = "What is the Sentiment?"


app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Successful !")
    
    except Exception as e:
        return Response(f"Error Occurred! {e}")
    
@app.get("/predict")
async def predict_route(text):
    try:

        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)    

