import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import time

def work():
    cap = cv2.VideoCapture(0)
    model = tensorflow.keras.models.load_model('keras_model.h5')

    while True:
        np.set_printoptions(suppress=True)
        # Load the model  
        ret, fram = cap.read()
            
        if ret:
            cv2.imshow('video', fram)
            color_coverted = cv2.cvtColor(fram, cv2.COLOR_BGR2RGB)
            k = cv2.waitKey(1000)
            image=Image.fromarray(color_coverted)


            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            #turn the image into a numpy array
            image_array = np.asarray(image)

            # display the resized image
            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            # run the inference
            prediction = model.predict(data)
            
            print(prediction)
            
            if k == 27:
                break
        else:
            print('error')
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    print("works")
    work()
    