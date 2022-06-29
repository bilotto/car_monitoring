from __init__ import logging

def main_car_device(car_dvc):
    car_dvc.run_diagnosis()
        
def push_to_server(car_dvc):
    if not car_dvc.n_failures:
        logging.info("{},Nothing new to push".format(car_dvc))
        return
    logging.info("{},Will push {} new notifications to the server".format(car_dvc, car_dvc.n_failures))
    car_dvc.push_to_server()

def probability_is_broken(car_dvc):
    from random import randint
    BROKEN_CAR_CHANGE_PERCENTAGE = 5
    def is_broken():
        if randint(0, 100) < int(BROKEN_CAR_CHANGE_PERCENTAGE):
            return True
        return False
    if car_dvc.broken:
        return
    elif not car_dvc.current_dtc:
        return
    elif is_broken():
        car_dvc.break_car()