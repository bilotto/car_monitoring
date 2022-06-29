from __init__ import logging

class BaseClass:

    def __init__(self):
        self.lock = None
        self.event = None

    def acquire(self):
      if self.lock:
        self.lock.acquire()

    def release(self):
      if self.lock:
        self.lock.release()

    def log_line(self, line, level='DEBUG'):
      log_message = "{},{}".format(self, line)
      if level == 'INFO':
        logging.info(log_message)
      elif level == 'ERROR':
        logging.error(log_message)
      elif level == 'DEBUG':
        logging.debug(log_message)
      elif level == 'WARN':
        logging.warn(log_message)
