# DATA 533 Project (Group 3) : BC Driver's License Advisor

## Background
The objective of the BC Driver's License (DL) Advisor is to advice the BC residents the next cource of action to get BC Driving License based on the inputs from the user. 

## Structure and Module
The DLAdvisor package containers two subpackages, namely :
1. Sub package - ProfileBuilder : responsible for interacting with users, collect inputs, and constructing user profile objects. This subpackage have two modules 

    1.1) Collector: This module have the following methods/functions
    
        1.1.1) greeting(): which greets the user based on the time of the day
        1.1.2) calculateAge(dateEntry): which takes date as input and returns the age in years
        1.1.3) passBasicEligibility(): this checks the eligibility of the user based on user input and return true of false if eligibility criteria is met.
        1.1.4) gatherProfile(): this passes the user input to create a profile using UserProfile Module and returns profile object.
        
    1.2) UserProfile: This class have the following methods/functions
    
        1.2.1) def __init__: Initializes the parameters or attributes of the user
        1.2.2) __str__(self): Formats the user input in a specified format
        1.2.3) formatName(self): Formats the user name to upper case.
        
2. Sub Package - Analyzer : responsible for gathering resources object, and present the recommendation to users. This subpackage have two modules 

    2.1) Advisor: This module have the following methods/functions
    
        2.1.1) advice(stage): Advices to the user based on identified stage based on user input.
        2.1.2) populatePrepResources(stage): Populate Prep Resources 
        2.1.3) populateOLResources(stage): Populate Online Resources 
        
    2.2) Resource: This module have the following classes and methods/functions
    
        Class: Resource
        2.2.1) __init__(self,stage,resources): Initializes stage wise resources
        2.2.2) display(self): Displays resources list.
        2.2.3) checkResourceType(self,resourceslink)
        Class: PrepResource(Resource)
        2.2.4) __init__(self,stage,resources): Initializes stage wise resources
        2.2.5) display(self): Displays resources list.
        Class: OLResource(Resource)
        2.2.6) __init__(self,stage,resources): Initializes stage wise resources
        2.2.7) display(self): Displays resources list.

## Call the Main Controller
Take reference to the `RunMe.ipynb`.

## Main Controller
`Main.py` (under DLAdvsior) is the main program which orchestrates all the modules and class in under the package.

## How They Work
Keep track of the user profile, determine the user stage, populate various resources depending on user stage, and present to user.

## Restrictions
1. This is for BC Residents only
2. Disclaimer : This module is for conceptual illustration only.  Some conditions and rules may not have been fully implemented in this application.  Please refer to icbc website for the most update and detailed policy.

