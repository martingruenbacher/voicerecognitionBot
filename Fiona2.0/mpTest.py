from multiprocessing import Process, Queue
import time

def f(q):
    while True:
        q.put("MyAudio") # send audiofiles
        time.sleep(0.5)

def g(q,q1):
    while True:
        print(q.get(), q.qsize())
        q1.put("Mach das") # send erkannte funktion
        time.sleep(1)
    
def h(q1):
    while True:
        print(q1.get(), q1.qsize()) # mach erkannte funktion
        time.sleep(1)

if __name__ == '__main__':
    q = Queue()
    q1 = Queue()

    p = Process(target=f, args=(q,))
    p.start()
    p1 = Process(target=g, args=(q,q1,))
    p1.start()
    p2 = Process(target=h, args=(q1,))
    p2.start()
