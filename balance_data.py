import cv2
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load("training_data.npy", allow_pickle=True)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

ups = []
upsshield = []
downs = []
downsshield = []
lefts = []
leftsshield = []
rights = []
rightsshield = []
shield = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]   

    if choice == [1, 0, 0, 0, 0]:
        ups.append([img, choice])
    elif choice == [1, 0, 0, 0, 1]:
        upsshield.append([img, choice])
    elif choice == [0, 1, 0, 0, 0]:
        downs.append([img, choice])
    elif choice == [0, 1, 0, 0, 1]:
        downsshield.append([img, choice])
    elif choice == [0, 0, 1, 0, 0]:
        lefts.append([img, choice])
    elif choice == [0, 0, 1, 0, 1]:
        leftsshield.append([img, choice])
    elif choice == [0, 0, 0, 1, 0]:
        rights.append([img, choice])
    elif choice == [0, 0, 0, 1, 1]:
        rightsshield.append([img, choice])
    elif choice == [0, 0, 0, 0, 1]:
        shield.append([img, choice])
    else:
        print("No matches!!!")

ups = ups[:len(lefts)]



"""
for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow("test", img)
    print(choice)

    if cv2.waitKey(25) & 0XFF == ord("q"):
        cv2.destroyAllWindows()
        break
"""