import time
from multiprocessing import Process


def pi_naive(start, end, step):
    print ("Start: ", str(start))
    print ("End: ", str(end))
    sum = 0.0
    
    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
        
    print(sum * step)

if __name__ == "__main__":
    num_steps = 10000000 #10.000.000 (10+e7)
    sums = 0.0
    step = 1.0/num_steps
    tic = time.time() # Tempo Inicial
    
    loop_range = num_steps/4
    processes = []
    
    for i in range(4):
        processes.append(Process(target=pi_naive, args=(int(i*loop_range), int((i+1)*loop_range), step)))
    
    for i in range(4):
        processes[i].start()
        
    for i in range(4):
        processes[i].join()
    
    toc = time.time() # Tempo Final
    # pi = step * sums
    
    pi = (  0.5675882184166029 +
            0.874675783495744 +
            0.7194139991698749 +
            0.9799146525074476)
    
    print ("Valor Pi: %.10f" %pi)
    print ("Tempo Pi: %.8f s" %(toc-tic))