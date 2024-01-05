# without singleton pattern
class Logger:
    def __init__(self):
        self.log_file = open("log.txt", "a")

    def log(self, message):
        self.log_file.write(message + "\n")

logger1 = Logger()
logger2 = Logger()

# with singleton pattern
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.log_file = open("log.txt", "a")

    def log(self, message):
        self.log_file.write(message + "\n")

logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # True