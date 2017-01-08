from stateStore import stateStore
from stateBase import stateBase
import threading
import time
import socket
import subprocess

#
#  State Machine
#
class stateMachine(object):
    def __init__(self,config):
        self.config          = config
        self.ss              = stateStore()
        self.ss.putVal('runStateMachine',True)
        #init state classes
        self.sRun   = runSlam(self.config)
        self.sPause = pauseSlam(self.config)
        self.sExit  = exitSlam(self.config)
        #set initial state as Pause state
        self.currentState = self.sPause
        self.nextState    = self.sPause
        
    def checkStateInput(self):
        #read file and
        stateFile = open(self.config['fileName'],'rb')
        newState  = ''
        for line in stateFile:
            newState = line
        stateFile.close()
        if newState == 'run':
            self.nextState = self.sRun
        elif newState == 'pause':
            self.nextState = self.sPause
        elif newState == 'exit':
            self.nextState = self.sExit

    def run(self):
        while self.ss.getVal('runStateMachine'):
            time.sleep(0.005)
            #check the user input
            self.checkStateInput()
            
            #if new state run the state
            if self.nextState != self.currentState:
                self.currentState.exitState()
                self.nextState.enterState()
                self.currentState = self.nextState

            self.currentState.run()

#
#  State Classes
#
class runSlam(stateBase):
    def __init__(self,config):
        super(runSlam,self).__init__(config)

    def enterState(self):
        subprocess.call(['./runCaptureSend.sh'])
        
        
    def run(self):
        #Take images, send pictures
        if self.config['debugStates']:
            testFile = open(self.config['testFile'],'wb')
            testFile.write('runState')
            testFile.close()

class pauseSlam(stateBase):
    def __init__(self,config):
        super(pauseSlam,self).__init__(config)

    def run(self):
        #pause the image taking and wait... will have to be careful of what the sending script is doing
        if self.config['debugStates']:
            testFile = open(self.config['testFile'],'wb')
            testFile.write('pauseState')
            testFile.close()

class exitSlam(stateBase):
    def __init__(self,config):
        super(exitSlam,self).__init__(config)

    def run(self):
        #set exit stuff and prepare to end this code
        if self.config['debugStates']:
            testFile = open(self.config['testFile'],'wb')
            testFile.write('exitState')
            testFile.close()
        self.ss.putVal('runStateMachine',False)

#
#  Command Line Input Thread
#
class enterInput(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #flush the state file that may exist
        stateFile = open('state.txt','wb')
        stateFile.write('')
        stateFile.close()

    def run(self):
        # thread actions
        run = True
        while run:
            #ask for input
            stateInput = raw_input("Change state to: ")
            #write to file
            stateFile = open('state.txt','wb')
            stateFile.write(stateInput)
            stateFile.close()
            time.sleep(1)
            if stateInput == 'exit':
                run = False

#
#  Tcp Server Thread
#
class tcpInput(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #flush the state file that may exist
        stateFile = open('state.txt','wb')
        stateFile.write('')
        stateFile.close()
        self.state = 'pause'
        #set up connection binding (bind to port 4200)
        port = 4200
        self.s = socket.socket()
        self.s.bind(('',port))
        self.s.listen(1)
        self.conn, addr = self.s.accept()
        print 'connected'

    def run(self):
        # thread actions, 
        while True:
            #wait for input
            self.state = self.conn.recv(1024)
            print self.state
            if not self.state: #connection lost
                break
            #write to file
            stateFile = open('state.txt','wb')
            stateFile.write(self.state)
            stateFile.close()
            time.sleep(0.5)
            if self.state == 'exit': #exitting
                break
        self.conn.close()


#
#  Main Code
#
conf = { 
         'fileName'    : 'state.txt',
         'testFile'    : 'currentState.txt',
         'debugStates' : True
       }
#InputThread = enterInput()
InputThread = tcpInput()
InputThread.start()
SM = stateMachine(conf)
SM.run()

