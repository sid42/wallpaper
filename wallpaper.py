import requests as r
import threading as th
import json  

data = r.get('https://collectionapi.metmuseum.org/public/collection/v1/objects').json()['objectIDs']
dataCount = len(data)
threadCount = 4
split = int(dataCount/threadCount)
paintingList = []
startIdx = 1

def getLinks(startIndex, split):
    for id in range(startIndex, startIndex + split):
    	response = r.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(data[id]))
    	link = response.json()['primaryImage']
    	importance = response.json()['isHighlight']
    	print(id)
    	if link and importance:
            paintingList.add(id)
    	else: 
       	    print('invalid')

def main():
    global startIdx, split
    threads = list()
    for i in range(threadCount): 
        t = th.Thread(target=getLinks, args=(startIdx, split))
        t.start()
        threads.append(t)
        startIdx = startIdx + split

    for i, thread in enumerate(threads):
        thread.join() 

    print("its over")


if __name__ == "__main__":
    main() 
    

