# generate_validation.py

#
# Creates validation.txt file where all validation images paths are listed.
# Save path: /mydrive/yolov4/<project_dir>/data/validation.txt
#

import os

def main():
    # Path to directory with images to validate on
    # /mydrive/yolov4/<project_dir>/data/validation/
    validation_path = os.path.join(data_path, 'validation')

    image_files = []
    for filename in os.listdir(validation_path):
      if filename.endswith('.jpg'):
        image_files.append(os.path.join(validation_path, filename))

    # /mydrive/yolov4/<project_dir>/data/
    os.chdir(data_path)
    print(data_path)
    with open("validation.txt", "w") as file:
      for image in image_files:
        file.write(f'{image}\n')

    print(f'Found {len(image_files)} train images total ({len(image_files)/len(classes)} per class).')

if __name__ == '__main__':
    main()
