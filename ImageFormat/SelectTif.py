import os
import random
import tifffile
from tqdm import tqdm


def Select(imagePath, destPath, position):
    """
    introduce:
        random select images in the dataset to train and validation
    args:
        :param str imagePah: the directory of dataset images
        :param str destPath: the destination directory of selected images
        :param int position: the number of position to be selected

    return
        void
    """
    labelPath = imagePath + "_label"
    label_destPath = destPath + "_label"
    iteractor=tqdm(range(127,position),ncols=70)
    for p in iteractor:
        p = '{:03d}'.format(p)
        s = random.randint(0, 44)
        s = '{:03d}'.format(s)
        img_name = f"img_Retardance_t000_p{p}_z{s}.tif"
        print(img_name,)
        img_path = os.path.join(imagePath, img_name)
        label_name = f"img_568_t000_p{p}_z{s}.tif"
        label_path = os.path.join(labelPath, label_name)
        img = tifffile.imread(img_path)
        tifffile.imwrite(os.path.join(destPath, img_name), img)
        label = tifffile.imread(label_path)
        tifffile.imwrite(os.path.join(label_destPath, label_name), label)


if __name__ == '__main__':
    imagePath = "/data/stone/microDL/dataset/input/data/train_npz"
    destPath = '/home/stone/dataset/tif/test'
    position = 160
    Select(imagePath, destPath, position)
