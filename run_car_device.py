from __init__ import logging
from CarDevice import CarDevice
from auxiliary_classes import TimerThread
from threading import Event

def main_car_device(car_dvc_obj):
    if car_dvc_obj.broken:
        logging.error("{},Fail! The car is broken".format(car_dvc_obj))
        return
    dtc = car_dvc_obj.run_get_dtc()
    if dtc:
        car_dvc_obj.register_failure(dtc)
    else:
        logging.info("{},Success! The car is good".format(car_dvc_obj))

def start_timer_thread(car_dvc_obj):
    thread = TimerThread(always, 1, main_car_device, car_dvc_obj)
    thread.start()

car_device_1 = CarDevice(car_id=1, brand='Ford', model='Ka')
car_device_2 = CarDevice(car_id=2, brand='Volkswagen', model='Fusca')
car_device_3 = CarDevice(car_id=3, brand='Fiat', model='Palio')

always = Event()

start_timer_thread(car_device_1)
start_timer_thread(car_device_2)
start_timer_thread(car_device_3)

while True:
    pass