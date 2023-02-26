from unittest import TestCase
from main import list_all, queries, stats, list_test
from main import request_choice, number_choice, channel_selection
from parameterized import parameterized

class TestMyltiplyNums(TestCase):
    def test_number_1(self):
        result = number_choice(dir_all=list_all)
        roster = [15, 35, 54, 98, 119, 213]
        self.assertEqual(result, roster)

    def test_number_2(self):
        result = request_choice(quer = queries)
        roster = {3: 57, 2: 43}
        self.assertEqual(result, roster)

    def test_number_3(self):
        result = channel_selection(choice = stats)
        roster = ('yandex')
        self.assertEqual(result, roster)

    @ parameterized.expand(list_test)
    def test_number_4(self, etalon, choice):
        choice = stats
        result = channel_selection(choice)
        self.assertEqual(result, etalon)
