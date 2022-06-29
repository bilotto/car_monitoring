from __init__ import logging
from CarDevice import CarDevice
from auxiliary_classes import TimerThread
from threading import Event, Lock
from car_device_routines import main_car_device, push_to_server
from simulator import probability_is_broken

always = Event()

def start_monitoring_thread(car_dvc_obj, timeout=10):
    logging.info("{},Start monitoring thread".format(car_dvc_obj))
    thread = TimerThread(car_dvc_obj.event, timeout, main_car_device, car_dvc_obj)
    thread.start()

def start_push_thread(car_dvc_obj, timeout=60):
    logging.info("{},Start push_to_server thread".format(car_dvc_obj))
    thread = TimerThread(car_dvc_obj.event, timeout, push_to_server, car_dvc_obj)
    thread.start()

def start_probability_thread(car_dvc_obj, timeout=5):
    logging.info("{},Start probability_is_broken thread".format(car_dvc_obj))
    thread = TimerThread(always, timeout, probability_is_broken, car_dvc_obj)
    thread.start()
  
car_device_1 = CarDevice(car_id=1, brand='Ford', model='Ka')
car_device_1.lock = Lock()
car_device_1.event = Event()

start_monitoring_thread(car_device_1, 5)
start_push_thread(car_device_1, 30)
start_probability_thread(car_device_1, 1)

while True:
    pass


