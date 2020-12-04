import time
import threading

def cal_sum(a,b):
    time.sleep(1)
    print("Sum = "+str(a+b))
    
def cal_sub(a,b):
    time.sleep(0.2)
    print("Sub = "+str(a-b))

t = time.time()

t1 = threading.Thread(target= cal_sum, args=(5,5))
t2 = threading.Thread(target= cal_sub, args=(5,5))

t1.start()
t2.start()

t1.join()
t2.join()