#!/usr/bin/env python3
import os
from PIL import Image
size =(128,128)
for image in os.listdir("."):
        if not image.endswith(".py") and not image.endswith(".DS_Store"):
                img = Image.open(image).convert('RGB')
                img.rotate(-90)
                img.thumbnail(size)
                new_name = os.path.basename(image)
                img.save("/opt/icons/{}".format(new_name), "jepg")
                img.close()
        else:
            continue

#con este si se logro
#!/usr/bin/env python3
import os
from PIL import Image
old_path = os.path.expanduser('~') + '/images/'
new_path = '/opt/icons/'
for image in os.listdir(old_path):
        if '.' not in image[0]:
                img = Image.open(old_path + image)
                img.rotate(-90).resize((128, 128)).convert("RGB").save(new_path + image.split('.')[0], 'jpeg')
                img.close()


