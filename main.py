class SingletonBlackBox:
    __instance = None

    def __init__(self):
        self.some_property = 42

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


obj1 = SingletonBlackBox.get_instance()
