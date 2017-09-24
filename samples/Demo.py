from pirant.app import DevRant

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