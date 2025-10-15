from queue import deque
from collections import defaultdict

page_reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3
n = len(page_reference_string)


def fifo(page_reference_string, frames):
    memory = deque()
    faults = 0
    hits = 0
    status = []
    
    for page in page_reference_string:
        if page not in memory:
            faults += 1
            if len(memory) == frames:
                memory.popleft()
            memory.append(page)
        else:
            hits += 1
        status.append(list(memory))
        print(f"Page: {page}, Frames: {memory}, Hits: {hits}, Faults: {faults}")
    return faults, status

def lru(page_reference_string, frames):
    memory = deque()
    faults = 0
    hits = 0
    status = []
    
    for page in page_reference_string:
        if page not in memory:
            faults += 1
            if len(memory) == frames:
                memory.popleft()
            memory.append(page)    
        else:
            hits += 1
            memory.remove(page)
            memory.append(page)
        status.append(list(memory))
        print(f"Page: {page}, Frames: {memory}, Hits: {hits}, Faults: {faults}")
    return faults, status

def lfu (page_reference_string, frames):
    memory = deque()
    faults = 0
    hits = 0
    status = []
    frecuencia = defaultdict(int)
    
    for page in page_reference_string:
        if page in memory:
            hits += 1
            frecuencia[page] += 1
        else:
            faults += 1
            
            if len(memory) < frames:
                memory.append(page)
            else:
                
                menos_frecuente = min(frecuencia[p] for p in memory)
                
                candit = [p for p in memory if frecuencia[p] == menos_frecuente]
                eliminarPag = candit[0]
                memory.remove(eliminarPag)
                del frecuencia[eliminarPag]
                memory.append(page)
            frecuencia[page] += 1
        
        status.append(list(memory))
        print(f"Page: {page}, Frames: {memory}, Hits: {hits}, Faults: {faults}")
    return faults, hits, status       

def opt(page_reference_string, frames):
    memory = deque()
    faults = 0
    hits = 0
    status = []  
    
    for i, page in enumerate(page_reference_string):
        if page in memory:
            hits += 1
        else: 
            faults += 1
            
            if len(memory) < frames:
                memory.append(page)
            else: 
                
                futurasPaginas = page_reference_string[i + 1:]
                ultimoIndice = -1
                eliminarPag = None
                
                for p in memory:
                    if p in futurasPaginas:
                        index = futurasPaginas.index(p)
                    else:
                        index = float('inf')
                    if index > ultimoIndice:
                        ultimoIndice = index
                        eliminarPag = p
                memory.remove(eliminarPag)
                memory.append(page)
        status.append(list(memory))
        print(f"Page: {page}, Frames: {memory}, Hits: {hits}, Faults: {faults}")
    return faults, hits, status
                          
def clock(page_reference_string, frames):
    status = []
    memory = deque()
    hits = 0
    faults = 0
    bits = []
    pointer = 0
    
    for page in page_reference_string:
        if page in memory:
            hits += 1
            index = memory.index(page)
            bits[index] = 1
            
        else:
            faults += 1
            
            if len(memory) < frames:
                memory.append(page)
                bits.append(1)
            else:
                
                while True:
                    if bits[pointer] == 0:
                        memory[pointer] = page
                        bits[pointer] = 1
                        pointer = (pointer + 1) % frames
                        break
                    else: 
                        bits[pointer] = 0
                        pointer = (pointer + 1) % frames
        status.append(list(memory))
        print(f"Page: {page}, Frames: {memory}, Bits: {bits}, Hits: {hits}, Faults: {faults}")
    return faults, hits, status
        
            
    
def main():
    print("Least Recently Used Algorithm")
    lru(page_reference_string, frames)
    print("-----------------------------------------")
    print("First In First Out Algorithm")
    fifo(page_reference_string, frames)
    print("-----------------------------------------")
    print("Least Frequently Used Algorithm")
    lfu(page_reference_string, frames) 
    print("-----------------------------------------")
    print("Optimal Replacement Algorithm")
    opt(page_reference_string, frames) 
    print("-----------------------------------------")
    print("Second Chance (or Clock)")
    clock(page_reference_string, frames)

    
main()