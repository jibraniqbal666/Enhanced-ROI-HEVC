import math, os, json, PIL, glob, uuid
from PIL import Image
import numpy as np
import pylab as pl
from roipoly import roipoly
import pycocotools._mask as _mask

image_id = 0

while(1):   

    try:
        image_id = image_id + 1
        img = Image.open('wound_augmented%d.jpg'%image_id)
        width, height  = img.size
        file_name = 'wound_augmented%d.jpg'%image_id

        pl.imshow(img, interpolation='nearest')
        pl.colorbar()
        pl.title("Image Number %d  ----Press r to try again"%image_id)

        # let user draw first ROI
        ROI1 = roipoly(roicolor='r')  # let user draw first ROI

        # show the image with the first ROI
        pl.imshow(img, interpolation='nearest')
        segPixels = ROI1.displayROI()
        Xaxis, Yaxis = segPixels
        segmentation = [[]]

        for i in range(0,len(Xaxis)):
            segmentation[0].append(Xaxis[i])
            segmentation[0].append(Yaxis[i])

        frPyObjects = _mask.frPyObjects
        Rs = frPyObjects(segmentation, height, width)
        area = _mask.area
        a = area(Rs)
        a = a[0]
        a = np.uint32(a).item() #converting numpy integer to primitive python integer
        toBbox = _mask.toBbox
        bbs = toBbox(Rs)
        bbs = bbs[0].tolist() #conveting array to list

        pl.imshow(img, interpolation='nearest', cmap="Greys")
        pl.waitforbuttonpress()
        choice = raw_input("> ")
        if choice == 'r':              #press r to try again
            image_id = image_id - 1
            pl.close('all')
            continue
        else:

            with open("instances_trainForJSON.txt", "a") as text_file:
                text_file.write("%s  %s  %s  %s  %s  %s  %s\n"%(file_name,width,height,image_id,segmentation,a,bbs))
            pl.close('all')

    except Exception as ex:
        print ex
        raise
        print('Image not found %d'%image_id)
        break



