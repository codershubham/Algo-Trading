import logging

# for reference
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')

class Logger:
    __instance = None

    def __new__(cls, name=None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.logger = logging.getLogger(name)
            cls.__instance.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            cls.__instance.logger.addHandler(console_handler)

        return cls.__instance


#    def Debug(name, message, level = 1):
#        if level == 1:
#            __instance.logger.debug(message)
#        elif level == 2:
#            __instance.logger.info(message)
#        elif level == 3:
#            __instance.logger.warning(message)
#        elif level == 4:
#            __instance.logger.error(message)
#        elif level == 5:
#            __instance.logger.critical(message)

    @staticmethod
    def getObject(name):
        return Logger(name)
