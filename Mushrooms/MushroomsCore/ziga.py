from .scripts.label_image import process_image

image_path = '/home/maxim/Code/Python/Mushrooms/temp/data.jpg'


def handle_uploaded_file(file):
    with open(image_path, 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    dest.close()

    return process_image(image_path)
