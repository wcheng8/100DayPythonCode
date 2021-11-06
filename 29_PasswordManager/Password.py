import time
class Password():
    def __init__(self):
        self.username = ''
        self.site = ''
        self.password = ''
        # self.time = time.clock_gettime()

    def print_pas(self):
        pass_string = f"{self.site} | {self.username} | {self.password}"
        return pass_string