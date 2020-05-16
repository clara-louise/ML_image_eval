import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import os

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('converted_keras/keras_model.h5')


def predict_image_class(image_path):
    # returns a prediction [[]]

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(image_path)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    # image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return prediction


f = open("converted_keras/labels.txt", "r")
predicted_classes = []
for line in f:
    predicted_classes.append(line.split()[1])


test_classes = (os.listdir("test_data/"))
counts_per_test_classes = {}

for test_class in test_classes:
    counts = {}
    print(test_class + " images, predicted class and score")
    for image in os.listdir("test_data/" + test_class):
        prediction = predict_image_class(
            "test_data/" + test_class + "/" + image)[0]

        max_value = max(prediction)
        i_of_max = [i for i, j in enumerate(prediction) if j == max_value]
        # Assuming that there is only one max, which may not always be true
        predicted_class = predicted_classes[i_of_max[0]]
        # uncomment below to get detailed predictions
        print(image, predicted_class, max_value)

        if predicted_class not in counts:
            counts[predicted_class] = 1
        else:
            counts[predicted_class] = counts[predicted_class] + 1

    counts_per_test_classes[test_class] = counts

print(counts_per_test_classes)
