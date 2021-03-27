class BlackBox:
    __instance = None

    def get_response(self, text, randNum):
        isComplete = True
        res = ""
        print(randNum)
        for i in text:
            letterNum = ord(i) - 1072
            smileNum = ord(i) - 128513 - randNum
            print(str(ord(i)) + " " + str(letterNum))
            print(str(ord(i)) + " " + str(smileNum))
            if 0 <= letterNum <= 33 or ord(i) == 32:
                if ord(i) == 32:
                    num = 128513 + randNum + 32
                else:
                    num = 128513 + randNum + letterNum
            elif 0 <= smileNum <= 33:
                if smileNum == 33:
                    num = 1072 + 33
                elif smileNum == 32:
                    num = 32
                else:
                    num = 1072 + (31 - smileNum)
            else:
                isComplete = False
                break
            if num >= 0:
                res += chr(num)
        if isComplete:
            if res.replace(' ', '') == "":
                return "<Пусто>"
            else:
                return res
        else:
            return "Введены недопустимые символы."

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = BlackBox()
        return cls.__instance
