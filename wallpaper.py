import requests as r
import threading as th
import json  

apiLink = 'https://collectionapi.metmuseum.org/public/collection/v1/'
objectIDs = r.get(apiLink + 'objects').json()['objectIDs']
dataCount = len(objectIDs)
threadCount = 250
split = int(dataCount/threadCount)
paintingList = {}
startIdx = 1
c = 1
lock = th.Lock()
f = open('list.txt', 'w')

def getLinks(startIndex, split):
    for idx in range(startIndex, startIndex + split):
        try: 
            response = r.get(apiLink + 'objects/' + str(objectIDs[idx]))
            link = response.json()['primaryImage']
            importance = response.json()['isHighlight']
            if link and importance:
                print('Added {0} to list'.format(objectIDs[idx]))
                paintingList[objectIDs[idx]] = {
                    'id' :  objectIDs[idx],
                    'link': link
                }
                writeToFile(json.dumps(paintingList[objectIDs[idx]]))

        except: 
            #print('Unable to currently access object {0}'.format(idx))
            print()

        finally: 
            #incrementCounter()
            print('{0} % \complete'.format(int(c/dataCount)*100))
               
def incrementCounter():
    global c
    lock.acquire()
    c = c + 1
    lock.release()

def writeToFile(str):
    global f 
    lock.acquire()
    f.write(str)
    lock.release

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
    
    f.write(json.dumps(paintingList))
    f.close() 

def debug():
    f.write(json.dumps(paintingList))

if __name__ == "__main__":
    main() 
    #debug()
