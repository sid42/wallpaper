import urllib.request
import random
import json
from PIL import Image, ImageOps

wallpaperPath = r'C:\Program Files\wallpaper\resources\wallpaper.jpg' 

def downloadImage():
    with open('./resources/list.txt','r') as f:
        data = [line.strip() for line in f]
        img = json.loads(data[random.randrange(len(data))])
        urllib.request.urlretrieve(img['link'], wallpaperPath)
        return data 

def setSpecifications():
    size = (1920, 1080)
    img = Image.open(wallpaperPath)
    print(img.size)
    img.thumbnail(size, Image.ANTIALIAS)
    fittedImg = Image.new('RGBA', size, (255, 255, 255, 0))
    fittedImg.paste(
        img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
    )
    fittedImg.save(wallpaperPath, 'PNG')
    

def debug():
    urllib.request.urlretrieve('https://images.metmuseum.org/CRDImages/an/original/DT879.jpg', './resources/wallpaper.jpg')

def main():
    downloadImage()
    setSpecifications()

if __name__ == "__main__":
    main() 
    #debug()


