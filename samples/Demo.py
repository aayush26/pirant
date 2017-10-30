from pirant import DevRant
devrant = DevRant()

# Get Top 10 Rants
topRants = devrant.get_rants("top", 10, 0)
print topRants['rants'][0]['text']

# Get Recent 10 Rants
recentRants = devrant.get_rants("recent", 10, 0)
print recentRants['rants'][0]['text']

# Get Algo 10 Rants
algoRants = devrant.get_rants("algo", 10, 0)
print algoRants['rants'][0]['text']

# Get Rant and all its comments given Rant Id
rant = devrant.get_rant_by_id(194632)
print rant['rant']['text']
print rant['comments'][0]['body']

# Get Recent 10 weekly (does not accept limit param)
rant = devrant.get_weekly_rants("recent", 10)
print rant['rants'][0]['text']

# Search Rant by keyword
searchResult = devrant.search_rants_by_keyword("devrant")
print searchResult['results'][1]['text']
print searchResult['results'][1]['attached_image']['url']
print searchResult['results'][1]['user_avatar']['i']

# Get Top 5 collabs
collabsResult = devrant.get_collabs(0, 5)
print collabsResult['rants'][0]['c_type_long']

# Get Collab and all its comments given Collab Id
collab= devrant.get_collab_by_id(913738)
print collab['rant']['c_description']
print collab['comments'][0]['body']