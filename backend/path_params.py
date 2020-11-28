from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI()

# parameter is model_name
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    # if this is the first choice
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}


    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    else:
        return {'model_name': model_name, 'message': 'Have some residuals'}

# from fastapi import FastAPI

# app = FastAPI()


# # item_id is a path parameter, same syntax used by Python format strings
# @app.get('/items/{item_id}')
# async def read_item(item_id: int):
#     # declare the type of a path parameter in the function, using Python type annotations
#     # declare `item_id` ro be an `int`
#     # value of the path parameter item_id will be passed to my function as the argument item_id
#     return {'item_id': item_id}

# # all data validation is performed under the hood by Pydantic
# # you can use the same type declarations str, float, bool and other more complex data types
# # fixed paths should be declared before parametric paths as the fixed path could be interpreted as a parameter