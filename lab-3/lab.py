import random
import math
import time
from typing import Callable


def random_exp(lambd):
    random_number = random.uniform(0, 1)
    return - math.log(1 - random_number)/lambd


class Client():
    def __init__(self):
        self.queue_start = 0.0
        self.queue_end = 0.0
        self.queue_time = 0.0
        self.service_start = 0.0
        self.service_end = 0.0
        self.service_time = 0.0
        self.overall_time = 0.0
    
    def start_queue(self):
        self.queue_start = time.time()
    
    def end_queue(self):
        self.queue_end = time.time()
        self.queue_time = self.queue_end - self.queue_start

    def start_service(self):
        self.service_start = time.time()

    def end_service(self):
        self.service_end = time.time()
        self.service_time = self.service_end - self.service.start
        self.overall_time = self.queue_time + self.service_time

class Server():
    
    def __init__(self, service_time, queue: Queue):
        self.service_time = service_time
        #Tiene que estar en SEGUNDOS
    
    def serve(self, client: Client):
        client.start_service()
        time.sleep(self.service_time)
        client.end_service()

class Queue():

    def __init__(self, lmax, s, lambd: Callable, mu: Callable):
        self.lmax = lmax
        self.server_count = s
    
    def simulation(time_limit):
        #aqui quede xd