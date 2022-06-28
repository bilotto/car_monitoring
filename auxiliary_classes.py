from threading import Thread

class TimerThread(Thread):
    def __init__(self, event, timeout, callback, *args):
        Thread.__init__(self)
        self.stopped = event
        self.timeout = timeout
        self.callback = callback
        self.callback_args = args

    def run(self):
        while not self.stopped.wait(self.timeout):
            if len(self.callback_args) == 2:
                self.callback(self.callback_args[0], self.callback_args[1])
            elif len(self.callback_args) == 1:
                self.callback(self.callback_args[0])
            else:
                self.callback()

