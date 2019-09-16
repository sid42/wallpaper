import urllib.request
import requests as re
import random
import json
import logging
from PIL import Image, ImageOps

wallpaperPath = r'C:/Program Files/wallpaper/resources/' 
api = 'https://collectionapi.metmuseum.org/public/collection/v1/'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('update.log', encoding='utf-8')])

def downloadImage():
    with open('./resources/list.txt','r') as f:
        data = [line.strip() for line in f]
        img = json.loads(data[random.randrange(len(data))])
        urllib.request.urlretrieve(img['link'], wallpaperPath + 'wallpaper.jpg')
        return img 

def setSpecifications():
    size = (1920, 1080)
    fillColour = (0, 0, 0, 0)
    img = Image.open(wallpaperPath + 'wallpaper.jpg')
    print(img.size)
    img.thumbnail(size, Image.ANTIALIAS)
    fittedImg = Image.new('RGBA', size, fillColour)
    fittedImg.paste(
        img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
    )
    fittedImg.save(wallpaperPath + 'wallpaper.png', 'PNG')

def setInfo(id):
    info = re.get(api + 'objects/' + str(id))
    print(info.json())
    with open(wallpaperPath + 'wallpaperInfo.json', 'w+') as f:
        f.write(json.dumps(info.json()))
    

def debug():
    urllib.request.urlretrieve('https://images.metmuseum.org/CRDImages/an/original/DT879.jpg', './resources/wallpaper.jpg')

def main():
    try:
        img = downloadImage()
        setSpecifications()
        setInfo(img['id'])
        logging.info('Successfully updated wallpaper \n')
    except:
        logging.error('Unable to update wallpaper \n')

if __name__ == "__main__":
    main() 
    #debug()


