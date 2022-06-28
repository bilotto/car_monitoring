import logging

DEBUG_MODE = True

# format = "%(levelname)s,%(asctime)s,%(funcName)s,%(threadName)s,%(message)s"
format = "%(levelname)s,%(asctime)s,%(message)s"

if not DEBUG_MODE:
    logging.basicConfig(format=format,
                        level=logging.INFO,
                        datefmt="%Y-%m-%dT%H:%M:%S",
                        handlers=[
                            # logging.FileHandler("/var/log/cron.log"),
                            logging.StreamHandler()
                        ])
else:
    logging.basicConfig(format=format,
                        level=logging.DEBUG,
                        datefmt="%Y-%m-%dT%H:%M:%S",
                        handlers=[
                            # logging.FileHandler("/var/log/cron.log"),
                            logging.StreamHandler()
                        ])
