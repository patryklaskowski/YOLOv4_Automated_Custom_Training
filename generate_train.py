# generate_train.py

#
# Creates train.txt file where all train images paths are listed.
# Save path: /mydrive/yolov4/<project_dir>/data/train.txt
#

import os

def main():
    # Path to directory with images to train on
    # /mydrive/yolov4/<project_dir>/data/train/
    train_path = os.path.join(data_path, 'train')

    image_files = []
    for filename in os.listdir(train_path):
      if filename.endswith('.jpg'):
        image_files.append(os.path.join(train_path, filename))

    # /mydrive/yolov4/<project_dir>/data/
    os.chdir(data_path)
    print(data_path)
    with open("train.txt", "w") as file:
      for image in image_files:
        file.write(f'{image}\n')

    print(f'Found {len(image_files)} train images total ({len(image_files)/len(classes)} per class).')

if __name__ == '__main__':
    main()
