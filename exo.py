import time
import threading
import urllib.request

start = time.perf_counter()

def download_image(img_url):
    img_bytes = urllib.request.urlopen(img_url).read()
    img_name = img_url.split('/')[2]
    img_file = open(img_name, 'wb')
    img_file.write(img_bytes)
    img_file.close()


try:
    #t1 = threading.Thread(target=download_image, args=["https://astra.icu/p2.png"])
    t2 = threading.Thread(target=download_image, args=["https://astra.icu/p3.png"])

    #t1.start()
    t2.start()

    #t1.join() # j'attends la fin de la thread
    t2.join() # j'attends la fin de la thread


    end = time.perf_counter()


except ValueError:
    print(f"il n'y a pas de lien pour l'image ")
else:
    print(f"Tasks ended in {round(end - start, 2)} second(s)")





