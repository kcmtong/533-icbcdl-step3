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
        self.age3 = Collector.calculateAge(date(1982,9,22))
        self.age4 = Collector.calculateAge(date(1996,4,24))
        self.currentSTR = Collector.greeting()
        
    def test_greeting(self):
        curTime = datetime.datetime.now()
        if curTime.hour < 12 :
            self.assertEqual('morning',self.currentSTR)
        elif 12 <= curTime.hour < 18 :
            self.assertEqual('afternoon',self.currentSTR)
        else:
            self.assertEqual('evening',self.currentSTR)
    
    def test_calculateAge(self):
        self.assertEqual(42,self.age1)
        self.assertEqual(50,self.age2)
        self.assertNotEqual(40,self.age1)
        self.assertNotEqual(60,self.age2)
        self.assertNotEqual(20,self.age3)
        self.assertNotEqual(70,self.age4)

    def test_passBasicEligibility(self):
        pass
    
    def tearDown(self):
        del(self.age1)
        del(self.age2)
        del(self.age3)
        del(self.age4)
        del(self.currentSTR)

    @classmethod
    def tearDownClass(cls):
        pass

unittest.main(argv=[''], verbosity=2, exit=False)