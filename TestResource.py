import unittest
from DLAdvisor.ProfileBuilder import Collector, UserProfile
from DLAdvisor.Analyzer import Advisor, Resource

## TODO (Nowshaba) : Follow the template and fill in the remaining
class TestResource(unittest.TestCase) :    

    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        self.pr1 =  Resource.PrepResource(1,[['Prep Stage ONE','http://pstageone.com']])
        self.or1 =  Resource.OLResource(1,[['OL Stage ONE','http://ostageone.com']])
        self.pr2 =  Resource.PrepResource(1,[['Prep Stage TWO','http://pstageone.com']])
        self.or2 =  Resource.OLResource(1,[['OL Stage TWO','http://ostageone.com']])
        
    def test_createPrepResource(self):
        self.assertIn('Prep Stage',self.pr1.resources[0][0])
        self.assertIn('pstageone.com',self.pr1.resources[0][1])
        self.assertIn('Prep Stage',self.pr2.resources[0][0])
        self.assertIn('pstageone.com',self.pr2.resources[0][1])

    def test_createOLResource(self):
        self.assertIn('OL Stage',self.or1.resources[0][0])
        self.assertIn('ostageone.com',self.or1.resources[0][1])
        self.assertIn('OL Stage',self.or2.resources[0][0])
        self.assertIn('ostageone.com',self.or2.resources[0][1])

    def tearDown(self):
        del(self.pr1)
        del(self.or1)
        del(self.pr2)
        del(self.or2)
        
    @classmethod
    def tearDownClass(cls):
        pass
    
    