import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
def convert_annotation(path,image_id):
    in_file = open(os.path.join(path+r'/annotation/%s.xml'%(image_id)))  #input
  
    
    out_file = open(os.path.join(path+r'/labels/%s.txt'%(image_id)), 'w')    #output
    tree=ET.parse(in_file)     #get xml tree
    root = tree.getroot()      #get root
    size = root.find('size')
    w = int(size.find('width').text)    #width of image
    h = int(size.find('height').text)
    
    for obj in root.iter('object'):   #find every object
        difficult = obj.find('difficult').text   #find difficult
        cls = obj.find('name').text
        if  int(difficult) == 1:
            continue
    
    
        xmlbox = obj.find('bndbox')  #get boundbox
        name = obj.find('name').text
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(name.encode("utf-8") + " " + " ".join([str(a) for a in bb]) + '\n') #




path=r'/users/panfeng/python/Test'

os.walk(path)

filenames=os.listdir(os.path.join(path+'/annotation'))

isExists=os.path.exists(os.path.join(path+r'/labels/'))

if not isExists:
    os.mkdir(os.path.join(path+r'/labels/'))

for filename in filenames:
    
    print(filename)
    image_id=filename.split(".")[0]
    convert_annotation(path,image_id)
