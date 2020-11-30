<div align=center>
<h1> ZMaps </h1>
Resource and threat tracking dashboard for the zombie apocalypse
</div>

- Models
  - Location of interest: 
    - geographic location: geographic location
    - Type of landmark: zombie horde, resource stash, outpost
  - Zombie horde:
    - Number of zombies
    - Average stage of decomposition
  - Resource stash:
    - Litres of water : int
    - Litres of gasoline : int
    - Weapons : (string, int)
    - Food : (string, int)
    - Technology : string
  - Outpost:
    - Type: Military, Civilian
    - Population size: int
    - Resources : Resource stash
    - Accepting survivors: Boolean
    - Has Internet Access: Boolean

- Operations:
  - POST Location of interest
    - POST Zombie Horde
    - POST Outpost
      - POST Resource Stash

  - GET all locations of interest
  - GET all Zombie Hordes
  - GET all Outposts
  - GET outpost closest to me (eventually) 

  - PATCH number of zombies in zombie horde
  - PATCH average stage of decomposition in zombie horde
  - PATCH each resource in a resource stash
  - PATCH population of Outpost and its resources

- Frontend:
  - Map that displays all locations of interest
    - Legend
      - Zombie horde is red dot
      - Resource stash is purple dot
      - Military outpost is green dot
      - Civilian outpost is blue dot
    - Clicking on map creates a location of interest
      - Can fill out more information about it
    - Can request directions
  - Global information
  - World Anti-Zombie Federation
  - Inspired by World War Z
- Backend API:
  - Routes
    - GET '/locations'
      - return all locations of interest
    - POST '/locations'
      - Create a new location
    - GET '/locations/<int:pk>'
      - return data of that location
    - PATCH '/locations/<int:pk>'
      - Update location information
    - DELETE '/locations/<int:pk>'
      - Delete location
    - GET '/locations/zombie'
      - Return all zombie hordes
    - GET '/locations/zombie/closest'
      - Return the closest zombie horde
    - GET '/locations/resource'
      - Return JSON of all abandoned resource stash
    - GET '/locations/closest'
      - Return JSON of the closest outpost that is accepting survivors
    - GET '/locations/closest/route'
      - Return route to closest outpost
      - Avoid all zombie hordes by 100KM

  