# Enhanced-ROI-HEVC
These are the video links which we are using to produce frames:

1. https://www.youtube.com/watch?v=yYLxfXsLqBUSplit (Thickness Skin Graft Reconstruction Pearl: The Cerclage Reduction)

2. https://www.youtube.com/watch?v=ZgNJ8YDA7dY (Live Surgery: Ganglion Cyst Volar Wrist)

3. https://www.youtube.com/watch?v=3o7cgZsd3bs (Live Surgery: Small Finger Extensor Tendon Saw Injury Cut Repair)

Due to fewer number of images, we doing image augmentation using keras and augmentor tool
In keras we are using these parameters:
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    shear_range=0.2,
    fill_mode='nearest',
    zoom_range=0.2
