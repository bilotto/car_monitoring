from codes import DTC
from __init__ import logging
from random import randint
import random

FAILURE_CHANCE_PERCENTAGE = 20
BROKEN_CAR_CHANGE_PERCENTAGE = 45

def is_failure():
    if randint(0, 100) < int(FAILURE_CHANCE_PERCENTAGE):
        return True
    return False

def is_broken():
    if randint(0, 100) < int(BROKEN_CAR_CHANGE_PERCENTAGE):
        return True
    return False

class CarDevice:

    def __init__(self, car_id, brand=None, model=None):
        self.car_id = str(car_id)
        self.brand = brand
        self.model = model
        self.failures = []
        self.n_diagnosis = 0
        self.broken = False
        logging.info("Registering CarDevice {}".format(self))

    def register_failure(self, dtc):
        logging.info("{},Adding failure: {}".format(self, dtc))
        self.failures.append(dtc)
        logging.info("{},Number of failures: {}".format(self, len(self.failures)))
        if is_broken():
            logging.error("{},The car is broken!".format(self))
            self.broken = True

    def __repr__(self) -> str:
        return "{},{},{}".format(self.car_id, self.brand, self.model)


    def run_get_dtc(self):
        self.n_diagnosis += 1
        logging.info("Running car diagnosis {}".format(self.n_diagnosis))
        if is_failure():
            dtc_key = random.choice(list(DTC.keys()))
            dtc_value = DTC.get(dtc_key)
            logging.warn("{},Failure found,{},{}".format(self, dtc_key, dtc_value))
            return (dtc_key, dtc_value)
        return None

