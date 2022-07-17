# EcoSystem-simulator

WHAT IS THIS?
- This app is simulating an ecologic system.

WHAT ARE THE RULES?
- Our system has 3 objects: Foxes, Rabbits and Grass.
- The Rabbits eats the grass. for every pair of grass objects the rabbit eats - it reproduces.
- The foxes eats the rabbit. for every pair of rabbit the fox eats - it reproduces.
- If the fox doesn't eat for too long - it starves. it turns blue and eventually dies.
- The corpes of the rabbits turn into grasses objects and thats how the "organic material" doesn't get lost.

AND, WHAT'S THE POINT?
- The point is seeing the balance an ecologic system has:
- "too many" grasses object, let the rabbit reproduces.
- "too many" rabbits, let the foxes reproduce.
- "too many" foxes, kills the rabbits and therfore let the grass reproduce.
- Well, this is the circle of life.

SEEING THE DATA
- since we really want to see the beauty of nature, 
  there's a python file that plots the data and let us see the real impact of the elements on each other.
  
WHAT ARE THE FILES?
- "ecosystem.gmk": the simulator itself, built using GML.
- "ecosystem.exe": the simulator exported as an exe file.
- "plot-creator.py": a python script that turns the data of the last simulation into a graph.
