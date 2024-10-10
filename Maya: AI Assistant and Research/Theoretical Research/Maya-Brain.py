import logging
import threading
import time

class Brain:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s ---- %(message)s')
    def __init__(self):
        self.status = ''
        logging.info('Maya Brain Starting...')
        self.sens_mem = Sensory_Memory(self)
        self.work_mem = Working_Memory(self)
        self.lt_mem = Long_Term_Memory(self)
        self.instincts = Instictual_Response(self)
        #start threads with respective loops

    
    
    
class Sensory_Memory():
    ##Basic recognition
    def __init__(self, brain):
        self.brain = brain
    
    #main loop responsible for listening for all external input
    def sensory_loop(self):
        pass
    
    
class Working_Memory():
        ##working memory: Executive thought
        def __init__(self, brain):
            self.status = brain.status
            self.brain = brain
            self.cent_exec = Central_Executive(self)
            self.epi_buff = Episodic_Buffer(self)
            self.vis_spa_pad = Visuo_Spatial_Scratchpad(self)

        #main loop responsible for listening for external and internal stimuli

class Central_Executive():
            ##executive functions
            def __init__(self, work_mem):
                self.work_mem = work_mem
            #main loop responsible for listening for internal and external stimuli that require attention
                #distributes into queue, experience document, etc
         
class Episodic_Buffer():
            #Epsisodic buffer
            def __init__(self, work_mem):
                self.work_mem = work_mem
            #main loop responsible for listening for commands from central executive


class Visuo_Spatial_Scratchpad():
            ##Visuo-Spatial Scratchpad
            def __init__(self, work_mem):
                self.work_mem = work_mem
            #main loop responsible for listening for commands from central executive


class Long_Term_Memory():
        #Long term memory module
        def __init__(self, brain):
            self.brain = brain
        #main loop repsonsible for listening for commands from central executive
    
class Instictual_Response():
        #instinctual response
        def __init__(self, brain):
            self.brain = brain
        #main loop responsible for listening for internal and external stimuli for fast response

hi = Brain()

from pocketsphinx import LiveSpeech
for phrase in LiveSpeech():
    print(phrase)