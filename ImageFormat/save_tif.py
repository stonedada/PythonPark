import cv2


path=r"D:\Data\backups\PngImages\img_Retardance_t000_p004_z001.png"
img=cv2.imread(path,1)
print("transformed img",img.shape)
cv2.imwrite(r"D:\Data\backups\img_Retardance_t000_p004_z001.png",img)