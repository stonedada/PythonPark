import requests
from pathlib import Path

def save_pic(path:Path):
    for i in range(100):
        url = f"http://bingw.jasonzeng.dev?resolution=UHD&index={i}"
        with requests.get(url) as r:
            with open(path/f"{i}.jpg","wb") as w:
                w.write(r.content)


if __name__ == "__main__":
    saved_path = Path("../bing_pic")
    saved_path.mkdir(parents = True, exist_ok = True)
    save_pic(saved_path)