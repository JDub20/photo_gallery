from iptcinfo import IPTCInfo
import sys, os


def photoInfo(photoDir):
    photosDir = "sample-jpegs-with-metadata"
    photo1 = os.path.join(photosDir,"6170_sample_image_01.jpg")
    fn = [photoDir][0]

    # Create new info object
    info = IPTCInfo(fn)

    # Check if file had IPTC data
    if len(info.data) < 4: raise Exception(info.error)

    # Print list of keywords, supplemental categories, contacts
    byLine = info.data['by-line']
    city =  info.data['city']
    caption =  info.data['caption/abstract']

    data = info.data
    
    return data