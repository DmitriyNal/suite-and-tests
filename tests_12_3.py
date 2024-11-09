import unittest
import unittest
from unittest import TestCase
from tests_12_2 import Tournament, Runner
from tests_12_1 import Runner



class RunnerTest(unittest.TestCase):
    """
        test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 50.
        """
    is_frozen = False
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("Usain Bolt")
        for _ in range(1, 11):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    """
        test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод run у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 100.
        """

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("Korobov")
        for _ in range(1, 11):
            runner.run()
        self.assertEqual(runner.distance, 100)

        """test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk соответственно.
        Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов"""

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("Korobov")
        runner2 = Runner("Usain Bolt")
        for _ in range(1, 11):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)




class TournamentTest(TestCase):
    is_frozen = True

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        for name, result in cls.all_results.items():
            print(f'{name}')
            for key, value in result.items():
                print(f'\t{key}: {value}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_turn1(self):
        turn_1 = Tournament(90, self.runner1, self.runner3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == self.runner3.name)
        self.all_results['Test1'] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_turn2(self):
        turn_2 = Tournament(90, self.runner2, self.runner3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == self.runner3.name)
        self.all_results['Test2'] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_turn3(self):
        turn_3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == self.runner3.name)
        self.all_results['Test3'] = result

    if __name__ == '__main__':
        unittest.main()
