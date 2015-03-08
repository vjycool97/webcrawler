import mechanize
import time
import urllib 


class Transaction(object):
    def __init__(self):
        self.custom_timers = {}
        self.s = 0
        self.base_url = 'http://nptel.ac.in/'
    
    def run(self,url):
        for num in range(0,20):
            br = mechanize.Browser()
            br.set_handle_robots(False)
            
            start_timer = time.time()
            resp = br.open(url)
            #resp.read()
            response_time = time.time() - start_timer
            self.custom_timers['All_Items'] = response_time
            print response_time
            print ("\n")
            self.s += response_time 
            assert (resp.code == 200), 'Bad HTTP Response'
            
           

if __name__ == '__main__':
    trans = Transaction()
    trans.run(trans.base_url)
    print trans.s
    #print trans.custom_timers   
