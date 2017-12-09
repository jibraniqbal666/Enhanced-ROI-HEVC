import json

description = 'This is stable 1.0 version of the 2014 MS COCO dataset.'
url = 'http://mscoco.org'
version = '1.0'
year = 2017
contributor = 'Microsoft COCO group'
date_created = '2017-08-02 09:11:52'

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

coco_url = 'http://mscoco.org/images'
flickr_url = 'http://farm1.staticflickr.com'
date_captured = '2017-12-04 15:43:24'

iscrowd = 0
license = 1

fp = open("instances_trainForJSON.txt")
for i, line in enumerate(fp):
    textData = line.split("  ")

    file_name = textData[0]
    width = textData[1]
    height = textData[2]
    image_id = textData[3]
    segmentation = textData[4]
    a = textData[5]
    bbs = textData[6].strip('\n')

    data["images"].append({"license": license, "file_name": file_name, "coco_url": coco_url, "height": height, "width": width,
         "date_captured": date_captured, "flickr_url": flickr_url, "id": image_id})  # show the image
    data["annotations"].append({"segmentation": segmentation, "area": a, "iscrowd": iscrowd, "image_id": image_id, "bbox": bbs,
         "category_id": category_id, "id": image_id})

jsonData = json.dumps(data)
d = json.loads(jsonData)

with open('instances_train2014.json', 'w') as outfile:
    json.dump(d, outfile)