import numpy as np
import torch
from matplotlib import pyplot as plt
from torchvision import transforms
from PIL import Image
from skimage.color import lab2rgb, rgb2lab

from my_code.model.model import MainModel
from my_code.net_gan.train_unet import build_res_unet
from my_code.constants import NET_GAN_PATH, MODEL_PATH, SIZE

def load_model():
    net_G = build_res_unet(n_input=1, n_output=2, size=SIZE)
    net_G.load_state_dict(torch.load(NET_GAN_PATH, map_location=torch.device('cpu')))
    model = MainModel(net_G=net_G)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
    return model

def lab_to_rgb(L, ab):
    #לוקח אצוות תמונות
    L = (L + 1.) * 50.
    ab = ab * 110.
    Lab = torch.cat([L, ab], dim=1).permute(0, 2, 3, 1).detach().cpu().numpy()
    #instead of (batch size,cannels,hight,whight)->(batch size,hight,whight,cannels) foreach lab2rgb of skimge
    rgb_imgs = []
    for img in Lab:
        img_rgb = lab2rgb(img)
        rgb_imgs.append(img_rgb)
    return np.stack(rgb_imgs, axis=0)


def color_image(img_path, model):
    img = Image.open(img_path).convert("RGB")
    SIZE = 256
    my_transforms = transforms.Resize((SIZE, SIZE), Image.BICUBIC)
    img = my_transforms(img)
    img = np.array(img)
    img_lab = rgb2lab(img).astype("float32")  # Converting RGB to L*a*b
    img_lab = transforms.ToTensor()(img_lab)
    L = img_lab[[0], ...] / 50. - 1.
    model.L = L.unsqueeze(0)#המרה מבלוק נתונים בודד לאצווה עטופה בגודל אחד יותר
    model()
    l = model.L
    L = l
    ab = model.fake_color
    rgb = lab_to_rgb(L, ab)[0]
    rgb = np.uint8(rgb * 255)
    return rgb
def color_open_image(img, model):
    SIZE = 256
    my_transforms = transforms.Resize((SIZE, SIZE), Image.BICUBIC)
    img = my_transforms(img)
    img = np.array(img)
    img_lab = rgb2lab(img).astype("float32")  # Converting RGB to L*a*b
    img_lab = transforms.ToTensor()(img_lab)
    L = img_lab[[0], ...] / 50. - 1.
    model.L = L.unsqueeze(0)#המרה מבלוק נתונים בודד לאצווה עטופה בגודל אחד יותר
    model()
    l = model.L
    L = l
    ab = model.fake_color
    rgb = lab_to_rgb(L, ab)[0]
    rgb = np.uint8(rgb * 255)
    return rgb

def flow(image_path):
    model = load_model()
    return color_image(image_path, model)

def flow_open(image_path):
    model = load_model()
    img = Image.open(image_path).convert("RGB")
    return color_open_image(img, model)

if __name__ == '__main__':
    color = flow("../gray_images/20151205_214255.jpg")
    plt.imshow(color)
    plt.axis('off')
    plt.show()
