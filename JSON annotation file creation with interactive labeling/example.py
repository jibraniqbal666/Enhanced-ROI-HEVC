import math, os, json, PIL, glob, uuid
from PIL import Image
import numpy as np
import pylab as pl
from roipoly import roipoly
import pycocotools._mask as _mask
image_count = 1

#for info (same for everyone)-----------------------------------------------------------------
description = 'This is stable 1.0 version of the 2014 MS COCO dataset.'
url = 'http://mscoco.org'
version = '1.0'
year = 2017
contributor = 'Microsoft COCO group'
date_created = '2017-08-02 09:11:52'
info = {"description": description, "url": url, "version": version, "year": year, "contributor": contributor, "date_created": date_created}

data = {}
data['info'] = {"description": description, "url": url, "version": version, "year": year, "contributor": contributor, "date_created": date_created}
data['images'] = []
data['licenses'] = []
data['annotations'] = []
data['categories'] = []

#for licenses (same for everyone)-------------------------------------------------------------
urlLicense = 'http://creativecommons.org/licenses/by-nc-sa/2.0/'
idLicense = 1
nameLicense = 'Attribution-NonCommercial-ShareAlike License'
data["licenses"].append({"url": urlLicense, "id": idLicense, "name": nameLicense})

#for categories-----------------------------------------------------------------------------------------
supercategory = 'MedicalImages'
name = 'RegionOfSurgery'
category_id = 1
data["categories"].append({"supercategory":supercategory, "id":category_id, "name":name})

uid = 0
coco_url = 'http://mscoco.org/images'
flickr_url = 'http://farm1.staticflickr.com'
date_captured = '2017-12-04 15:43:24'

while(1):   #--------- change or handle exception
# create image
#img = pl.ones((100, 100)) * range(0, 100)
    try:
        uid = uid + 1
        #img = pl.imread('res %d.jpg'%image_count)
        img = Image.open('wound_augmented%d.jpg'%image_count)
        #for images
        width, height  = img.size
        license = 1
        file_name = 'wound_augmented%d.jpg'%image_count


        data["images"].append({"license": license, "file_name": file_name, "coco_url": coco_url, "height": height, "width": width,
        "date_captured": date_captured, "flickr_url": flickr_url, "id": image_count})  # show the image

        # for annotations
        iscrowd = 0
        image_id = image_count

        pl.imshow(img, interpolation='nearest')
        pl.colorbar()
        pl.title("Image Number %d"%image_count)

        # let user draw first ROI
        ROI1 = roipoly(roicolor='r')  # let user draw first ROI

        # show the image with the first ROI
        pl.imshow(img, interpolation='nearest')
        segPixels = ROI1.displayROI()
        Xaxis, Yaxis = segPixels
        segmentation = [[]]
        #-------segmentation and bounding box procedure
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
        # for categories
        data["annotations"].append({"segmentation": segmentation, "area": a, "iscrowd": iscrowd, "image_id": image_id, "bbox": bbs,
        "category_id": category_id, "id": uid})

        jsonData = json.dumps(data)
        pl.imshow(img, interpolation='nearest', cmap="Greys")
        pl.waitforbuttonpress()
        pl.close('all')
        image_count = image_count + 1
    except Exception:
        print('Image not found %d'%image_count)
        break



d = jsonData
d = json.loads(d)
d["annotations"]
with open('instances_train2014.json','w') as outfile:
  json.dump(d,outfile)
