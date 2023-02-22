import glob
from pathlib import Path

files = Path(r"D:\Data\backups\test_npz").glob("*")
dist=r"D:\Data\backups\test_npz"
print(type(files))
for file in files:
    print(file)


file_list=glob.glob(dist+"\*")
print(len(file_list))