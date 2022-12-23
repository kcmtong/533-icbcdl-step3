import unittest
from DLAdvisor.ProfileBuilder import Collector, UserProfile
from DLAdvisor.Analyzer import Advisor

class TestUserProfile(unittest.TestCase) :    
    
    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        self.p1 =  UserProfile.UserProfile('Kenny',0,False,False,1)
        self.p2 =  UserProfile.UserProfile('John',1,True,True,1)
        self.p3 =  UserProfile.UserProfile('Nowshaba',2,False,False,3)
        
    def test_createProfile(self):
        self.assertEqual(self.p1.name,'Kenny')
        self.assertFalse(self.p1.current_icbc_lic)
        self.assertEqual(self.p2.name,'John')
        self.assertTrue(self.p2.current_icbc_lic)
        self.assertEqual(self.p3.name,'Nowshaba')
        self.assertTrue(self.p3.current_icbc_lic)

    def test_str(self):
        self.assertIn('None',str(self.p1))
        self.assertIn('False',str(self.p1))
        self.assertIn('Learner',str(self.p2))
        self.assertIn('True',str(self.p2))
        self.assertIn('Novice',str(self.p3))
        self.assertIn('False',str(self.p3))
        
    def tearDown(self):
        del(self.p1)
        del(self.p2)
        del(self.p3)
        
    @classmethod
    def tearDownClass(cls):
        pass