import unittest
from DLAdvisor.ProfileBuilder import Collector, UserProfile
from DLAdvisor.Analyzer import Advisor

class TestAdvisor(unittest.TestCase) :    

    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        self.prepresources1 = Advisor.populatePrepResources(1)
        self.prepresources2 = Advisor.populatePrepResources(2)
        self.prepresources3 = Advisor.populatePrepResources(3) 
        self.prepresources4 = Advisor.populatePrepResources(4) 
        self.oresources1 = Advisor.populateOLResources(1)
        self.oresources2 = Advisor.populateOLResources(2)
        self.oresources3 = Advisor.populateOLResources(3)
        self.oresources4 = Advisor.populateOLResources(4)
        
    def test_populatePrepResources(self):
        self.assertIn('Knowledge Test',self.prepresources1.resources[0][0])
        self.assertIn('Get-your-L.aspx',self.prepresources1.resources[0][1])
        self.assertIn('RoadTest 7',self.prepresources2.resources[0][0])
        self.assertIn('Get-your-N.aspx',self.prepresources2.resources[0][1])
        self.assertIn('RoadTest 5',self.prepresources3.resources[0][0])
        self.assertIn('Get-your-full-licence.aspx',self.prepresources3.resources[0][1])
        self.assertIn('Reciprocal License',self.prepresources4.resources[0][0])
        self.assertIn('Moving-from-another-country.aspx',self.prepresources4.resources[0][1])
        
    def test_populateOLResources(self):
        self.assertIn("Book a ICBC Knowledge",self.oresources1.resources[0][0])
        self.assertIn("maticwebbookin",self.oresources1.resources[0][1])
        self.assertIn("Book a Road Test 7",self.oresources2.resources[0][0])
        self.assertIn("webdeas-ui",self.oresources2.resources[0][1])
        self.assertIn("Book a Road Test 5",self.oresources3.resources[0][0])
        self.assertIn("webdeas-ui",self.oresources3.resources[0][1])
        self.assertIn("Book a ICBC License Exchange Appointment",self.oresources4.resources[0][0])
        self.assertIn("onlinebusiness.icbc.com",self.oresources4.resources[0][1])

    def tearDown(self):
        del(self.prepresources1)
        del(self.prepresources2)
        del(self.prepresources3)
        del(self.prepresources4)
        del(self.oresources1)
        del(self.oresources2)
        del(self.oresources3)
        del(self.oresources4)
        
    @classmethod
    def tearDownClass(cls):
        pass
    