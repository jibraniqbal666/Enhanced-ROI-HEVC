from keras.preprocessing.image import ImageDataGenerator  
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import os

input_image_number=1
total_image_number = 1

while(1): 
  try:
    input_path = 'wound_%d.jpg'%input_image_number
    output_path = 'wound_augmented{}.jpg'  
    count = 9
  
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
    for i, new_images in enumerate(images_flow):  
        # we access only first image because of batch_size=1
        new_image = array_to_img(new_images[0], scale=True)
        new_image.save(output_path.format(total_image_number))
        total_image_number = total_image_number + 1
        if i >= count:
            break
    os.remove('wound_%d.jpg'%input_image_number)
    print('Progress is Input image Number:%d '%input_image_number)
    input_image_number = input_image_number+1

  except IOError:
    print('Total number of images produced: %d '%total_image_number)
    print ('This image is not present: wound_%d.jpg '%input_image_number)
    break

