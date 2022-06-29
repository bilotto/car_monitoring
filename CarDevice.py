from codes import DTC
from __init__ import logging
from BaseClass import BaseClass
from FailEvent import FailEvent
from simulator import get_dtc


class CarDevice(BaseClass):

    def __init__(self, car_id, brand=None, model=None):
        BaseClass.__init__(self)
        self.car_id = str(car_id)
        self.brand = brand
        self.model = model
        self.failures = []
        self.n_diagnosis = 0
        self.broken = False
        self.current_dtc = None
        logging.info("Registering CarDevice {}".format(self))
        #

    def __getattribute__(self, name):
        if name == 'n_failures':
          return len(self.failures)
        return super().__getattribute__(name)

    def register_failure(self, fail_event):
        logging.info("{},Registering fail_event: {}".format(self, fail_event))
        self.acquire()
        self.failures.append(fail_event)
        self.release()

    def __repr__(self) -> str:
        return "{},{},{}".format(self.car_id, self.brand, self.model)

    def run_get_dtc(self):
        return get_dtc(self)

    def run_diagnosis(self):
        self.n_diagnosis += 1
        logging.info("Running car diagnosis {}".format(self.n_diagnosis))
        dtc = self.run_get_dtc()
        if not dtc:
            logging.info("{},Success! The car is good".format(self))
            return
        fail_event = FailEvent(dtc[0])
        logging.warn("{},Fail event,{}".format(self, fail_event))
        self.register_failure(fail_event)


    def push_fail_event(self, fail_event):
        logging.info("{},Pushing fail_event: {}".format(self, fail_event))
        self.acquire()
        self.failures.remove(fail_event)
        self.release()
        return True
        
    def push_to_server(self):
        for idx, fail_event in enumerate(self.failures):
            logging.info("{},Pushing fail_event {} to server".format(self, idx + 1))
            push_success = self.push_fail_event(fail_event)
            if not push_success:
                logging.error("Not possible to push")

