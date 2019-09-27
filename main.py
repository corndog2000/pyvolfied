import cv2
import numpy as np
import os
import time

from PIL import ImageGrab

# From local files
#from directkeys import PressKey, ReleaseKey, U, D, L, R, LCTRL, NUM1, NUM5
from GripPipeline import GripPipeline
from grabscreen import grab_screen
from getkeys import key_check


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

def keys_to_output(keys):
    #[U, D, L, R]
    output = [0, 0, 0, 0, 0]

    if "J" in keys:
        output[4] = 1

    if "W" in keys:
        output[0] = 1
    elif "A" in keys:
        output[1] = 1
    elif "S" in keys:
        output[2] = 1
    elif "D" in keys:
        output[3] = 1

    return output

# Load the training data file
file_name = "training_data.npy"

if os.path.isfile(file_name):
    print("File exists, loading previsous data.")
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print("File does not exist, starting fresh.")
    training_data = []

def main(gpipe):
    # Count down
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    #last_time = time.time()

    frame_count = 0

    while(True):
        screen = grab_screen(region=(130, 52, 828, 1040))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80, 60))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen, output])

        #print("Frame took {} seconds".format(time.time()-last_time))
        #last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name, training_data)

        if frame_count >= 100000:
            print(len(training_data))
            np.save(file_name, training_data)
            exit("Recorded 100,000 frames.")

        frame_count += 1

if __name__ == "__main__":
    gpipe = GripPipeline()
    main(gpipe)