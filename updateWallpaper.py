import urllib.request
import random
import json

def downloadImage():
    with open('./resources/list.txt','r') as f:
        data = [line.strip() for line in f]
        img = json.loads(data[random.randrange(len(data))])
        urllib.request.urlretrieve(img['link'], 'C:/Program Files/wallpaper/resources/wallpaper.jpg')
        return data 

def debug():
    urllib.request.urlretrieve('https://images.metmuseum.org/CRDImages/an/original/DT879.jpg', './resources/wallpaper.jpg')

def main():
    downloadImage()

if __name__ == "__main__":
    main() 
    #debug()


