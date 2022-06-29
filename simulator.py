from random import randint
import random
from codes import DTC
from __init__ import logging

FAILURE_CHANCE_PERCENTAGE = 20
BROKEN_CAR_CHANGE_PERCENTAGE = 1

def is_failure():
    if randint(0, 100) < int(FAILURE_CHANCE_PERCENTAGE):
        return True
    return False

def is_broken():
    if randint(0, 100) < int(BROKEN_CAR_CHANGE_PERCENTAGE):
        return True
    return False

def random_dtc():
    dtc_key = random.choice(list(DTC.keys()))
    return dtc_key

def get_dtc(car_dvc):
    if not car_dvc.current_dtc:
        if is_failure():
            dtc_key = random_dtc()
            dtc_value = DTC.get(dtc_key)
            car_dvc.current_dtc = (dtc_key, dtc_value)
            return (dtc_key, dtc_value)
    else:
        return car_dvc.current_dtc

def break_car(car_dvc):
    logging.error("{},The car is broken".format(car_dvc))
    car_dvc.acquire()
    car_dvc.broken = True
    car_dvc.release()

def probability_is_broken(car_dvc):
    if car_dvc.broken:
        return
    elif is_broken():
        car_dvc.break_car()

