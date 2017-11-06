import os

from .scripts.label_image import process_image


def handle_uploaded_file(file, session_uuid):
    image_path = os.getcwd() + "/temp/data_{}.jpg".format(session_uuid)
    with open(image_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    destination.close()

    return process_image(image_path)
