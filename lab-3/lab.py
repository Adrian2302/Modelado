import random
import math
from typing import Callable
import numpy as np


def random_exp(lambd):
    random_number = random.uniform(0, 1)
    if lambd == 0:
        return
    return - math.log(1 - random_number)/lambd


class Client():
    def __init__(self):
        self.queue_start = 0.0
        self.queue_time = 0.0
        self.service_start = 0.0
        self.service_time = 0.0
        self.overall_time = 0.0
    
    def start_queue(self, time):
        self.queue_start = time
    
    def end_queue(self, time):
        self.queue_time = time - self.queue_start

    def start_service(self, time):
        self.service_start = time

    def end_service(self, time):
        service_end = time
        self.service_time = service_end - self.service_start
        self.overall_time = self.queue_time + self.service_time

    def get_times(self):
        return self.queue_time, self.service_time, self.overall_time
    


class Server():
    
    def __init__(self):
        self.idle = True
        self.idle_time = 0.0
        self.last_service = 0.0
        self.current_client = None
        #Tiene que estar en SEGUNDOS
    
    def serve(self, client: Client, time):
        self.idle_time += time - self.last_service
        self.idle = False
        self.current_client = client
        client.end_queue(time)
        client.start_service(time)

    def end_serve(self, time):
        self.current_client.end_service(time)
        self.current_client = None
        self.last_service = time
        self.idle = True
    
    def is_idle(self):
        return self.idle
    
    def get_idle_time(self):
        return self.idle_time

    def get_client(self):
        return self.current_client

class Queue():

    def __init__(self, lmax, s, lambd: Callable, mu: Callable):
        self.lmax = lmax
        self.client_count = 0
        self.lost_count = 0
        self.server_count = s
        self.lambd = lambd
        self.mu = mu
        self.total_idle_time = 0.0
        self.total_queue_time = 0.0
        self.total_service_time = 0.0
    
    def simulation(self, time_limit):
        n = 0
        current_time = 0
        queue = []
        servers = [Server() for i in range(self.server_count)]
        time_client = current_time + random_exp(self.lambd(n))  # Se calcula la llegada del primer cliente
        client = Client()
        clients = [client]
        new_event = (time_client, client)

        event_queue = []
        event_queue.append(new_event)  #se añade a la cola de eventos la hora del primer cliente
        
        while(current_time <= time_limit or len(event_queue) > 0):  # Siempre y cuando no se pase del time limite o si la cola no está vacía, entonces se itera
            current_event = event_queue[0]
            event_queue.pop(0)

            if type(current_event[1]) is Client:  # Si la cola de eventos saca un cliente nuevo
                if(n < self.lmax):
                    n = n + 1
                    self.client_count += 1
                    

                current_time = current_event[0]

                idle_servers = [idx for idx, s in enumerate(servers) if s.is_idle() == True]# Se revisa si hay servidores disponibles
                if len(idle_servers) > 0: # Si hay servidores disponibles, entonces se pasa el cliente a un servidor y se calcula el tiempo de finalizacion del servicio
                    index = idle_servers[0]
                    server = servers[index]
                    server.serve(current_event[1], current_time)
                    time_release_server = current_time + random_exp(self.mu(n))
                    new_event = (time_release_server, server)
                    event_queue.append(new_event)

                else:  # Si no hay servidores disponibles, entonces se agrega el cliente a la cola.
                    if len(queue) + self.server_count < self.lmax and current_time <= time_limit:
                        queue.append(current_event)
                        client = current_event[1]
                        client.start_queue(current_time)
                    else:
                        self.lost_count += 1

                if(current_time <= time_limit):
                    time_client = current_time + random_exp(self.lambd(n))
                    client = Client()
                    clients.append(client)
                    new_event = (time_client, client)
                    event_queue.append(new_event)


            else:  # Caso donde la cola de eventos sea que se liberó un servidor
                n = n - 1
                current_time = current_event[0]
                server = current_event[1]
                server.end_serve(current_time)
                if len(queue) > 0:
                    current_event = queue[0]
                    queue.pop(0)
                    client = current_event[1]
                    server.serve(client, current_time)
                    time_release_server = current_time + random_exp(self.mu(n))
                    new_event = (time_release_server, server)
                    event_queue.append(new_event)

            event_queue.sort()

        #Calcular tiempo sin hacer nada de los servidores
        for s in servers:
            self.total_idle_time += s.get_idle_time()

        for c in clients:
            q_time, s_time, o_time = c.get_times()
            self.total_queue_time += q_time
            self.total_service_time += s_time

        print("---TIEMPOS---")
        print("Tiempo inactivo promedio de servidores:", (self.total_idle_time / self.server_count))
        print("Tiempo en cola promedio de clientes:", (self.total_queue_time / self.client_count))
        print("Tiempo en atención promedio de clientes:", (self.total_service_time / self.client_count))



                