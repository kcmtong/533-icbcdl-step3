import unittest
from TestUserProfile import TestUserProfile
from TestCollector import TestCollector
from TestResource import TestResource
from TestAdvisor import TestAdvisor

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestUserProfile))
    suite.addTest(unittest.makeSuite(TestCollector))
    suite.addTest(unittest.makeSuite(TestResource))
    suite.addTest(unittest.makeSuite(TestAdvisor))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

unittest.main(argv=[''], verbosity=2, exit=False)
    
my_suite()
