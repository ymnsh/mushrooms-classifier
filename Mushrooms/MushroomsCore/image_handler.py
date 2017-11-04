import os

from .scripts.label_image import process_image

image_path = os.getcwd() + "/temp/data.jpg"


def handle_uploaded_file(file):
    with open(image_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    destination.close()

    return process_image(image_path)
