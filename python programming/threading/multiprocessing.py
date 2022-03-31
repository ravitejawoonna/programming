import time
import multiprocessing


def sleep(ms):
    print(f"sleeping for {ms} seconds..")
    time.sleep(ms)
    print("Done sleeping..")
    
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=sleep, args=[1])
    p2 = multiprocessing.Process(target=sleep, args=[1])
    
    p1.start()
    p2.start()
    
    finish = time.perf_counter()
    print(f"Finished after: {str(finish)} secs")
    