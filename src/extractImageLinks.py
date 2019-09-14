import requests as r
import threading as th
import json  

apiLink = 'https://collectionapi.metmuseum.org/public/collection/v1/'
objectIDs = r.get(apiLink + 'objects').json()['objectIDs']
dataCount = len(objectIDs)
threadCount = 250
split = int(dataCount/threadCount)
startIdx = 1
c = 1
lockForCounter = th.Lock()
lockForWrite = th.Lock()

def getLinks(startIndex, split):
    global c
    for idx in range(startIndex, startIndex + split):
        try: 
            response = r.get(apiLink + 'objects/' + str(objectIDs[idx]))
            link = response.json()['primaryImage']
            importance = response.json()['isHighlight']
            if link and importance:
                print('Added {0} to list'.format(objectIDs[idx]))
                writeToFile(json.dumps({
                    'id' : objectIDs[idx],
                    'link' : link   
                }))

        except: 
            print('Unable to currently access object {0}'.format(idx))
            
        finally: 
            incrementCounter()
            print('{0} %'.format((c/dataCount)*100) + ' complete')
               
def incrementCounter():
    global c
    lockForCounter.acquire()
    c = c + 1
    lockForCounter.release()

def writeToFile(str): 
    lockForWrite.acquire()
    f = open('./resources/list.txt', 'a+')
    f.write(str + '\n')
    f.close()
    print('WRITE SUCCESSFUL \n' + str)
    lockForWrite.release()

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

def debug():
    for i in range(10000000000):
        print(i)
    
if __name__ == "__main__":
    main() 
    #debug()
