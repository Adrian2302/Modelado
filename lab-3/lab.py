import random
import math
import time

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
    
    def start_queue():
        self.queue_start = time.time()
    
    def end_queue():
        self.queue_end = time.time()
        self.queue_time = self.queue_end - self.queue_start

    def start_service():
        self.service_start = time.time()

    def end_service():
        self.service_end = time.time()
        self.service_time = self.service_end - self.service.start
        self.overall_time = self.queue_time + self.service_time
    