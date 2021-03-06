import blackBox


class SingletonController:
    __instance = None

    def __init__(self):
        self.users = {}

    def add_user(self):
        self.users.fromkeys(len(self.users), 0)  # ключ - это id; значение - это level

    def get_user(self, key):
        self.users.get(key)

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonController()
        return cls.__instance


controller = SingletonController().get_instance()
blackBx = blackBox.BlackBox().get_instance()

print(blackBx.get_output_message(input()))
