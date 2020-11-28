from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    # return all locations of interest
    return {"message": "hello"}

# - GET '/locations'
#     - return all locations of interest
# - POST '/locations'
#     - Create a new location
# - GET '/locations/<int:pk>'
#     - return data of that location
# - PATCH '/locations/<int:pk>'
#     - Update location information
# - DELETE '/locations/<int:pk>'
#     - Delete location
# - GET '/locations/zombie'
#     - Return all zombie hordes
# - GET '/locations/zombie/closest'
#     - Return the closest zombie horde
# - GET '/locations/resource'
#     - Return JSON of all abandoned resource stash
# - GET '/locations/closest'
#     - Return JSON of the closest outpost that is accepting survivors
# - GET '/locations/closest/route'
#     - Return route to closest outpost
#     - Avoid all zombie hordes by 100KM
