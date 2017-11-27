# Enhanced-ROI-HEVC
These are the video links that we are using to produce frames:

1. https://www.youtube.com/watch?v=yYLxfXsLqBUSplit (Thickness Skin Graft Reconstruction Pearl: The Cerclage Reduction)

2. https://www.youtube.com/watch?v=ZgNJ8YDA7dY (Live Surgery: Ganglion Cyst Volar Wrist)

3. https://www.youtube.com/watch?v=3o7cgZsd3bs (Live Surgery: Small Finger Extensor Tendon Saw Injury Cut Repair)

As starting frames of videos are related to the introduction about surgical procedure so we are skipping these frames. Further, to avoid redundancy we are extracting 1 frame after every 15 frames. We are using ffmpeg tool with this command:

    ffmpeg -i input_video.mp4 -vf "select=(not(lt(n\,1050)))*(not(mod(n\,15)))" -vsync vfr -q:v 2 wound_%d.jpg
In the above command, 1050 is the number of frames that we want to skip from beginning.

To keep numbering your images where you left in the previous video, you can simply add <-start_number> argument in the above command.

Due to fewer number of images, we are doing image augmentation using keras and augmentor tool.

In keras we are using these parameters:

    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    shear_range=0.2,
    fill_mode='nearest',
    zoom_range=0.2
    
    
automatic splitting and augmetation (on version 3)

perfect formatting, if you extract 5 frames from a video, and count of augmented will also be 5 
output will be 
original_images [0,6,12,18,24] augmented=[1,2,3,4,5,7,8,9,10,11,13......29]

for above configurations

from augVer2 import split_augment
split_augment('C:\\Users\\Ryuk666\\Downloads\\Live Surgery Foreign Body (BB) Removal from Finger.mp4',ffmpeg_bin=your_ffmpeg_downloaded_binary_path,frame_number=5, count =5)

docs will be coming soon
