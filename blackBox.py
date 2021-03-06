class BlackBox:
    __instance = None

    def get_response(self, message):
        newMessage = ""
        for i in message:
            newMessage += chr(ord(i) + 1)
        return newMessage

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = BlackBox()
        return cls.__instance
