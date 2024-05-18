from multiprocessing import Process

def print_name(name, id):
    print('hello, sou', name, id)
    
if __name__ == '__main__':
    processes = []
    for i in range(400):
        process = Process(target=print_name, args=('Kaio Filho', i,))
        processes.append(process)

    print_name('Kaio', 'Pai')
    
    for i in range(400):
        processes[i].start()
        
    for i in range(400):
        processes[i].join()
    