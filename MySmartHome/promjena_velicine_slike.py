from PIL import Image
import os

# Putanja do direktorija gdje se nalaze slike
image_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'MySmartHome', 'images')

# Imena slika
images = ['kratki_rukavi.png', 'lagana_jakna.png', 'zimska_jakna.png', 'kapa_sal_zimska_jakna.png']

# Željena veličina
new_size = (400, 800)

for image_name in images:
    image_path = os.path.join(image_dir, image_name)
    with Image.open(image_path) as img:
        resized_img = img.resize(new_size)
        resized_img.save(image_path)

print("Promjena veličine slika je završena.")
