# Process that run in parallel 
# When to use:
# CPU bound tasks,Parallel execution    

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")


if __name__ == "__main__":

    # create two processes 
    p1 = multiprocessing.process(target=square_numbers)
    p2 = multiprocessing.process(target=cube_numbers)
    t = time.time()

    # start the process 
    p1.start()
    p2.start()

    # wait for the processes to join
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)