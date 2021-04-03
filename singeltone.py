class SingletonController:
    __instance = None

    def __init__(self):
        self.users = {}

    def add_user(self, id_player):
        self.users[id_player] = "0!0"  # ключ - это id; значение 1 - это level, значение 2 - это рандомное число сдвига

    def get_value(self, key):
        return self.users[key]

    def set_value(self, key, value):
        self.users[key] = value

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonController()
        return cls.__instance