import logging
import threading
import time
class STEM():
    #STEM class for the brain stem module of Maya
    def __init__(self):
        self.eval_lock = threading.Lock()
        self.status = ''
        self.cur_status = ''
        self.brain_eval_thread = threading.Thread(target=self.brain_eval)
    def main(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s ---- %(message)s')
        logging.info('Maya STEM Starting...')


        self.brain_eval_thread.start()

        while True:
            time.sleep(3) #for testing purposes
            with self.eval_lock:
                #check status and decide upon that
                self.cur_status = self.status
            logging.info(f'Brain status: {self.cur_status}')

            if self.cur_status == 'terminated':
                ##restart brain
                pass
            #maintain homeostasis of any kind



    def brain_eval(self):
        #loop
        #contact brain
        with self.eval_lock:
            self.status = 'hi' #msg from brain
        #if hung, send back concerning status, retry with high priority, continue until highest priority and consider terminated
        pass

if __name__ == '__main__':
    maya_stem = STEM()
    maya_stem.main()