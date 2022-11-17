import multiprocessing
import time
import threading
import requests

urls = ["https://cdn.pixabay.com/photo/2022/11/14/06/56/maple-7590861_960_720.jpg", "https://cdn.pixabay.com/photo/2016/12/19/08/39/mobile-phone-1917737_960_720.jpg", ]



def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    print(urls[0])
    t1 = multiprocessing.Process(target=download_image, args=[urls[0]])
    print(urls[1])
    t2 = multiprocessing.Process(target=download_image, args=[urls[1]])

    start = time.perf_counter()

    t1.start()
    t2.start()

    t1.join() # j'attends la fin de la thread
    t2.join() # j'attends la fin de la thread

    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")







