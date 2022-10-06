import os
import cv2
import numpy as np
import pickle

current_id = 0
label_ids = {}
x_train = []
y_labels = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "dataset")
print(image_dir)

recognizer = cv2.face.LBPHFaceRecognizer_create()
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

for root, dirs, files in os.walk(image_dir):
    # print(root, dirs, files)
    for file in files:
        path = os.path.join(root, file)
        # print(path)
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_array = np.array(gray, "uint8")
        # print(image_array)

        label = os.path.basename(root)
        # print(label)

        if not label in label_ids:
            # print(label)
            label_ids[label] = current_id
            current_id += 1
        # print(label_ids)
        id_ = label_ids[label]
        # print(id_)
        #
        faces = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi = image_array[y:y + h, x:x + w]
            x_train.append(roi)
            y_labels.append(id_)

print(x_train)

with open("lable_pickle", "wb") as f:
    pickle.dump(label_ids, f)

# 训练模型
recognizer.train(x_train, np.array(y_labels))
# 保存
recognizer.save("mytrainer.xml")
