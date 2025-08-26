import time
import threading
import random

buffer = []
buffer_size = 10

produce = threading.Event()
consume = threading.Event()

produce.set()
mutex = threading.Lock()

def producer():
    
    while True:
        produce.wait()
        item = random.randint(0,99)
        with mutex:
            if len(buffer) < buffer_size:
                buffer.append(item)
                print(f"Produced: {item}")
                if len(buffer) == buffer_size:
                    produce.clear()
                    consume.set()
        time.sleep(1.5)

def consumer():
    while True:
        consume.wait()
        with mutex:
            if len(buffer) > 0:
                item = buffer.pop(0)
                print(f"Consumed: {item}")
                if len(buffer) == 0:
                    consume.clear()
                    produce.set()
        time.sleep(1.5)
        
prod_thread = threading.Thread(target=producer)
cons_thread = threading.Thread(target=consumer)

prod_thread.start()
cons_thread.start()