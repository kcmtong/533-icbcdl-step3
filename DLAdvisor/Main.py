from DLAdvisor.ProfileBuilder import Collector, UserProfile
from DLAdvisor.Analyzer import Advisor
from time import sleep
from tqdm import tqdm

def execute():
    Collector.greeting()
#    if (!Collector.passBasicEligiblity()) :
#        print("Sorry, not eligible! Bye!")
#        return
    if (not Collector.passBasicEligibility()) :
        print("Sorry, you are not eligible!")
        return
    print("Great! you are eligible to proceed!")
    
    user = Collector.gatherProfile()    
    user.formatName()
    print("Here is your profile summary\n######" + str(user) +
          "\n######")

    print("Analyzing...")
    for i in tqdm(range(5)):
        sleep(0.5)
    
    # TODO BY KENNY
    # temp set all user.stage = 1, to skip the following line when UserProfile pkg is completed
    # user.stage = 1
    Advisor.advice(user.stage)
    
    
    
