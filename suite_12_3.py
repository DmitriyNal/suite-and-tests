import unittest
import tests_12_3

test_suite = unittest.TestSuite()

test_suite.addTest(unittest.makeSuite(tests_12_3.RunnerTest))
test_suite.addTest(unittest.makeSuite(tests_12_3.TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)
