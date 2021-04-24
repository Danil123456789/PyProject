def isSpecialSimbols(num):
    return num == 32 or num == 44 or num == 46


class BlackBox:
    __instance = None

    def get_response(self, text, randNum):
        isComplete = True
        res = ""
        print(randNum)
        text = text.lower()
        print(text)
        for i in text:
            letterNum = ord(i) - 1072
            smileNum = ord(i) - 128513 - randNum
            print(str(ord(i)) + " " + str(letterNum))
            print(str(ord(i)) + " " + str(smileNum))
            if 0 <= letterNum <= 33 or isSpecialSimbols(ord(i)):
                if isSpecialSimbols(ord(i)):
                    num = 128513 + randNum + ord(i)
                else:
                    num = 128513 + randNum + letterNum
            elif 0 <= smileNum <= 47:
                if smileNum == 33:
                    num = 1072 + 33
                elif isSpecialSimbols(smileNum):
                    num = smileNum
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
