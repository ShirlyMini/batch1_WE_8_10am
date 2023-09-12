import multiprocessing as mp
import time
import math
result_a=[]
result_b=[]
result_c=[]

def make_cal1(num):
    for n in num:
        result_a.append(math.sqrt(n**3))

def make_cal2(num):
    for n in num:
        result_a.append(math.sqrt(n**4))

def make_cal3(num):
    for n in num:
        result_a.append(math.sqrt(n**5))

if __name__=="__main__":
    number_list= list(range(1000000))
    start=time.time()
    make_cal1(number_list)
    make_cal2(number_list)
    make_cal3(number_list)
    end = time.time()
    print(end - start)
    p1=mp.Process(target=make_cal1, args=[number_list])
    p2=mp.Process(target=make_cal2, args=[number_list])
    p3=mp.Process(target=make_cal3, args=[number_list])
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    # p1.join()
    # p2.join()
    # p3.join()
    end=time.time()
    print(end-start)