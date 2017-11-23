# Enhanced-ROI-HEVC
These are the video links that we are using to produce frames:

1. https://www.youtube.com/watch?v=yYLxfXsLqBUSplit (Thickness Skin Graft Reconstruction Pearl: The Cerclage Reduction)

2. https://www.youtube.com/watch?v=ZgNJ8YDA7dY (Live Surgery: Ganglion Cyst Volar Wrist)

3. https://www.youtube.com/watch?v=3o7cgZsd3bs (Live Surgery: Small Finger Extensor Tendon Saw Injury Cut Repair)

As starting frames of videos are related to the introduction about surgical procedure so we are skipping these frames. Further, to avoid redundancy we are extracting 1 frame after every 15 frames. We are using this command:

    ffmpeg -i input_video.mp4 -vf "select=(not(lt(n\,1050)))*(not(mod(n\,15)))" -vsync vfr -q:v 2 wound_%d.jpg

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
