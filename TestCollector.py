import unittest
from DLAdvisor.ProfileBuilder import Collector, UserProfile
from DLAdvisor.Analyzer import Advisor
import datetime
from datetime import date

class TestCollector(unittest.TestCase) :    

    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        self.age1 = Collector.calculateAge(date(1980,7,18))
        self.age2 = Collector.calculateAge(date(1972,11,3))
        
    def test_greeting(self):
        # The greeting() method in the Collector contains message printing, but without and return string
        # No testing can therefore be done here.
        pass
    
    def test_calculateAge(self):
        self.assertEqual(42,self.age1)
        self.assertEqual(50,self.age2)
        self.assertNotEqual(40,self.age1)
        self.assertNotEqual(60,self.age2)

    def test_passBasicEligibility(self):
        # The passBasicEligibility() method in the Collector are mainly interactive functions which ask for ouser input and then perform validation, which can not be automated easily.  
        # Manual testing can be done to ensure the proper user interaction behaviour.
        pass
    
    def tearDown(self):
        del(self.age1)
        del(self.age2)

    @classmethod
    def tearDownClass(cls):
        pass
    