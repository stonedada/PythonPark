import cv2


path=r"D:\Data\backups\PngImages\img_Retardance_t000_p004_z001.png"
save_path=r"D:\Data\backups\img_Retardance_t000_p004_z001.png"
# path_2=r"D:\Data\backups\im_c002_z000_t000_p000_overlay.png"
img=cv2.imread(path,1)
print("transformed img",img.shape)
cv2.imwrite(save_path,img)

save_path_2=r"D:\Data\backups\img_Retardance_t000_p004_z001_save.png"
img_2=cv2.imread(save_path,-1)
print("saved img",img_2.shape)
cv2.imwrite(save_path_2,img)