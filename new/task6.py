#import library
from fastapi import FastAPI,HTTPException
import requests

#create app
task6=FastAPI(title="API example")

#create a get endpoint
@task6.get("/task")
def get_task():
    url="https://official-joke-api.appspot.com/random_joke"
    try:
      response=requests.get(url, timeout=5)
      response.raise_for_status()
      return {
         "fetch":"successfully",
         "message": "congratulation"
      }
    
    #handle endpoint error
    except requests.Timeout:
          raise HTTPException(status_code=504,detail="request time out")
   
   #handle other error
    except requests.RequestException:
      raise HTTPException(status_code=500, detail="something went wrong with the api")
