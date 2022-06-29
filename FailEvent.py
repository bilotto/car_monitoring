
import datetime
from codes import DTC


class FailEvent:

    def __init__(self, dtc_code):
        self.timestamp = datetime.datetime.now()
        self.dtc_code = dtc_code

    def __repr__(self) -> str:
        return "{},{},{}".format(self.timestamp.strftime("%Y-%m-%dT%H:%M:%S"), self.dtc_code, DTC.get(self.dtc_code))
