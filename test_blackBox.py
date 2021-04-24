import unittest
from blackBox import BlackBox

blackBox = BlackBox.get_instance()


class TestBlackBox(unittest.TestCase):
    def testBox_1(self):
        self.assertEqual(blackBox.get_response("Привет", 3), "😓😔😌😆😉😖", "Should be 😓😔😌😆😉😖")

    def textBox_2(self):
        self.assertEqual(blackBox.get_response("😜😕😗😕😟😕", 6), "кспсзс", "Should be кспсзс")
