from keras.preprocessing.image import ImageDataGenerator  
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import os
import subprocess as sp
import re

def augment(input_path, count = 5):

    try:
        input_path = input_path
        output_path_base = os.path.split(input_path)[0]
        filename = os.path.split(input_path)[1]
        output_path = 'wound_{}.jpg'  
        count = count
  
        gen = ImageDataGenerator(  
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True,
            vertical_flip=True,
            shear_range=0.2,
            fill_mode='nearest',
            zoom_range=0.2
        )

        # load image to array
        image = img_to_array(load_img(input_path))
  
        # reshape to array rank 4
        image = image.reshape((1,) + image.shape)

        # let's create infinite flow of images
        images_flow = gen.flow(image, batch_size=1)  
        print(images_flow)
        for i, new_images in enumerate(images_flow):
            print(i) 
            # we access only first image because of batch_size=1
            new_image = array_to_img(new_images[0], scale=True)
            m = re.search(r"(\d+)", filename)
            if m is not None :
                print(os.path.join(output_path_base,
                                   output_path.format(int(m.group(0)) + i)))
                new_image.save(os.path.join(output_path_base,
                                            output_path.format(int(m.group(0)) + i )))
            else :
                print("There no number available in images for formatting")
            if i >= count:
                break

    except IOError:
        print("I/O error")

def split(vid_path, ffmpeg_bin, start = 0, fps = 1, frame_skip = 0, count = 0, frame_number = 0 ):
    dir_path = os.path.split(vid_path)[0]
    output_dir_path = os.path.join(dir_path, 'output')
    if not os.path.isdir(output_dir_path):
        os.makedirs(output_dir_path)
    
    images_dir_path = os.path.join(output_dir_path, 'wound_%d.jpg')
    
    skip_fps = 'select = (not(lt(n\, {0}))) * (not(mod(n\, {1})))'.format(
            frame_skip, fps)
    command = [ffmpeg_bin, '-i', vid_path, '-vf', skip_fps,
               '-vsync', 'vfr', '-v:q', '2']
    
    #add additonal option
    if frame_number > 0 :
        command.append('-vframes')
        command.append(str(frame_number))
    if start >= 0 :
        command.append('-start_number')
        command.append(str(start))

    #output directory path
    command.append(images_dir_path)

    #run ffmpeg command
    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, err = pipe.communicate()
    print(stdout,err)
    
    #rename generated frames
    for filename in os.listdir(output_dir_path):
        m = re.search(r"(\d+)", filename)
        if m is not None :
            os.rename(os.path.join(output_dir_path, filename),os.path.join(output_dir_path, 'wound_{0}.jpg'.format(int(m.group(0)) * (count + 1))))
    return output_dir_path            

def split_augment(vid_path, ffmpeg_bin='C:\\Users\\Ryuk666\\Downloads\\Compressed\\ffmpeg-3.4-win64-static\\bin\\ffmpeg.exe', start=0, fps=1, frame_skip=0, count=0, frame_number=0 ):
    output_dir_path = split(vid_path = vid_path, ffmpeg_bin = ffmpeg_bin, start = start, fps = fps, frame_skip= frame_skip, count = count, frame_number = frame_number)
    print (output_dir_path)
    for filename in os.listdir(output_dir_path):
        print(filename)
        augment(os.path.join(output_dir_path, filename), count = count)


