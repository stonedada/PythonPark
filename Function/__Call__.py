

class Preprocess(object):

    def __init__(self, output_size):
        self.output_size = output_size

    def __call__(self, image, label):

        image = image/123
        label = label/456

        return image,label






if __name__ == '__main__':

    transform=Preprocess([256,256])
    image=123
    label=456
    image,label=transform(image=image,label=label)
    print(image,label)

