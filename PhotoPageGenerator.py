import os, sys
from jinja2 import Environment, FileSystemLoader, Template
from photoInfo import photoInfo

PATH = os.path.abspath(".")
PHOTOS_PATH_NAME = "sample-jpegs-with-metadata"
env = Environment(loader=FileSystemLoader(''))
photoPageTemplate = env.get_template('PhotoPageTemplate.html')
PHOTOS_PATH = os.path.join(PHOTOS_PATH_NAME)

photos = os.listdir(PHOTOS_PATH)

def photoHTMLPage(fileName):
    #the split is to get rid of the ".jpg"
    return os.path.join("index", fileName.split(".")[0]+".html")

def photoNeighborHTMLPage(fileName):
    return os.path.join(fileName.split(".")[0]+".html")

for i, photoFile in enumerate(photos):

    currentPhotoHTMLPage = photoHTMLPage(photoFile)

    f = open(currentPhotoHTMLPage,"w")

    photoSrc = os.path.join("..", PHOTOS_PATH, photoFile)

    nextIndex = (i + 1) % len(photos)
    nextPhotoHTMLPage = photoNeighborHTMLPage(photos[nextIndex])

    prevIndex = (i - 1) % len(photos)
    prevPhotoHTMLPage = photoNeighborHTMLPage(photos[prevIndex])
    
    photoData = photoInfo(os.path.join(PHOTOS_PATH, photoFile))
    
    photoByLine = photoData['by-line']
    photoCity =  photoData['city']
    photoCaption =  photoData['caption/abstract']


    f.write(photoPageTemplate.render(currentPhotoSrc = photoSrc,
                                     nextPhotoSrc = nextPhotoHTMLPage,
                                     previousPhotoSrc = prevPhotoHTMLPage,
                                     byLine = photoByLine,
                                     caption = photoCaption,
                                     city = photoCity))