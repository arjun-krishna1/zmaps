# import the FastAPI class, provides functionality for
# your API
from fastapi import FastAPI

# create a FastAPI Instance, app
# main point of interaction to create all API
app = FastAPI()

# path operation decorator
# tells FastAPI that the function below is in charge
# of handling requests that go to the / path using a 
# get operationa
@app.get('/')
async def root():
    # this will be called by FastAPI when it recieves
    # a request to the / route
    # you can return a dict, list, str or int
    # you can also return Pydantic models
    # these are converted to JSON
    return {"message": "hello"}

'''
RECAP
1. Import FastAPI
2. create an app instance
3. write a path operation decorator (  @app.get('/) )
4. write a path operation function  ( def root(): ... )
5. Run the development server       ( uvicorn main:app --reload )
'''
'''
uvicorn main:app
main -> the file main.py
app -> the object created inside of main.py, 
        app = FastAPI()
--reload -> make the server restart after code 
        changes, development only

'''