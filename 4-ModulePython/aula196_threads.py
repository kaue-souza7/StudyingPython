from time import sleep
from threading import Thread
from threading import Lock

'''class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()


    def run(self):
        sleep(self.time)
        print(self.text)

t1 = MyThread('First Thread', 10)
t1.start()

t2 = MyThread('Thread 2', 5)
t2.start()

t3 = MyThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
'''






'''def vai_demorar(text, time):
    sleep(time)
    print(text)

t = Thread(target=vai_demorar, args=('---Thread Chegou---', 10))
t.start()

t2 = Thread(target=vai_demorar, args=('Thread 2', 5))
t2.start()

t3 = Thread(target=vai_demorar, args=('Thread 3', 2))
t3.start()

# Exemplo
# t.join()

while t.is_alive():
    print('Esperando a thread.')
    sleep(2)

# for i in range(20):
#     print(i)
#     sleep(1)
'''

class Ingressos:
    def __init__(self, stock) -> None:
        self.stock = stock
        self.lock = Lock()

    def buy(self, amount):
        self.lock.acquire()

        if amount > self.stock:
            print(f'Não temos {amount} ingressos em estoque.')
            self.lock.release()
            return
        
        sleep(1) # type: ignore

        self.stock -= amount
        print(f'Você comprou {amount} ingressos.'
              f'Ainda temos {self.stock} ingressos em estoque.')
        
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)
    
    for i in range(1, 20):
        t = Thread(target=ingressos.buy, args=(i,))
        t.start()
