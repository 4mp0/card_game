
import threading, time

def loop1():
    while True:
        print("Hello")
        time.sleep(1)
def loop2():
    while True:
        print("World")
        time.sleep(1)

thread1 = threading.Thread(target=loop1)
thread2 = threading.Thread(target=loop2)

thread1.start()
thread2.start()