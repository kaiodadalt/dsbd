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
    
    cpu = 4
    loop_range = num_steps/cpu
    processes = []
    
    for i in range(cpu):
        processes.append(Process(target=pi_naive, args=(int(i*loop_range), int((i+1)*loop_range) -1, step)))
    
    for i in range(cpu):
        processes[i].start()
        
    for i in range(cpu):
        processes[i].join()
    
    toc = time.time() # Tempo Final
    # pi = step * sums
    
    pi = (  0.5675880184165929 +
            0.9799142760368506  + 
            0.8746754634957313 +
            0.7194137431698626 )
    
    print ("Valor Pi: %.10f" %pi)
    print ("Tempo Pi: %.8f s" %(toc-tic))