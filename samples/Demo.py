from pirant import DevRant
devrant = DevRant()

# Get Top 10 Rants
topRants = devrant.getRants("top", 10, 0)
print topRants['rants'][0]['text']

# Get Recent 10 Rants
recentRants = devrant.getRants("recent", 10, 0)
print recentRants['rants'][0]['text']

# Get Algo 10 Rants
algoRants = devrant.getRants("algo", 10, 0)
print algoRants['rants'][0]['text']

# Get Rant and all its comments given Rant Id
rant = devrant.getRantById(194632)
print rant['rant']['text']
print rant['comments'][0]['body']
