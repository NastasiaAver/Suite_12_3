import unittest
import Module_12_2
import Module_12_1


tester = unittest.TestSuite()

tester.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_1.RunnerTest))
tester.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.TournamentTest))


test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(tester)