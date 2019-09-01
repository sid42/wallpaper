import requests as r
import json  

response = r.get('https://collectionapi.metmuseum.org/public/collection/v1/objects')
data = response.json()['objectIDs']

paintingList = []

f = open('list.txt', 'w')

for id in range(len(data)):
    response = r.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(data[id]))
    link = response.json()['primaryImage']
    importance = response.json()['isHighlight']
    print(id)
    if (link) and (importance == True):
        paintingList.append(id)
        f.write(str(data[id]) + '\n')
    else: 
        print('invalid')

f.close()

#print(data['objectIDs'])