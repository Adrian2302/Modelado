import random
import math
import time
from typing import Callable
import numpy as np


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
    
    def __init__(self, service_time):
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
        self.lambd = lambd
        self.mu = mu
    
    def simulation(self, time_limit):
        n = 0
        current_time = 0
        queue = []
        servers = np.ones([self.server_count], dtype=int)

        time_client = current_time + random_exp(self.lambd(n))  # Se calcula la llegada del primer cliente
        new_event = (time_client, "New Client")
        event_queue = []
        event_queue.append(new_event)  #se añade a la cola de eventos la hora del primer cliente
        
        while(current_time <= time_limit or len(event_queue) > 0):  # Siempre y cuando no se pase del time limite o si la cola no está vacía, entonces se itera
            current_event = event_queue[0]
            event_queue.pop(0)

            if(current_event[1] == "New Client"):  # Si la cola de eventos saca un cliente nuevo
                if(n < self.lmax):
                    n = n + 1
                current_time = current_event[0]

                index = np.where(servers == 1) # Se revisa si hay servidores disponibles
                if len(index[0]) > 0: # Si hay servidores disponibles, entonces se pasa el cliente a un servidor y se calcula el tiempo de finalizacion del servicio
                    servers[index[0][0]] = 0

                    time_release_server = current_time + random_exp(self.mu(n))
                    new_event = (time_release_server, index[0][0], "Server")
                    event_queue.append(new_event)

                else:  # Si no hay servidores disponibles, entonces se agrega el cliente a la cola.
                    if(len(queue) + self.server_count < self.lmax and current_time <= time_limit):
                        queue.append(current_event)

                if(current_time <= time_limit):
                    time_client = current_time + random_exp(self.lambd(n))
                    new_event = (time_client, "New Client")
                    event_queue.append(new_event)

            else:  # Caso donde la cola de eventos sea que se liberó un servidor
                n = n - 1
                current_time = current_event[0]
                if len(queue) > 0:
                    index = current_event[1]
                    current_event = queue[0]
                    queue.pop(0)

                    time_release_server = current_time + random_exp(self.mu(n))
                    new_event = (time_release_server, index, "Server")
                    event_queue.append(new_event)

                else:
                    servers[current_event[1]] = 1

            event_queue.sort()


                