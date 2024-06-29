import time
from multiprocessing import Pool

def pi_naive(args):
    start, end, step = args
    sum = 0.0
    
    for i in range(start, end):
        x = (i + 0.5) * step
        sum += 4.0 / (1.0 + x * x)
    
    return sum * step

if __name__ == "__main__":
    num_steps = 10000000  # 10.000.000 (10+e7)
    step = 1.0 / num_steps
    cpu = 4
    loop_range = num_steps // cpu
    
    pool = Pool(cpu)
    tic = time.time()  # Tempo Inicial
    
    ranges = [(i * loop_range, (i + 1) * loop_range - 1, step) for i in range(cpu)]
    
    results = pool.map(pi_naive, ranges)
    
    pi = sum(results)
    
    toc = time.time()  # Tempo Final
    
    print("Valor Pi: %.10f" % pi)
    print("Tempo Pi: %.8f s" % (toc - tic))
