from stateStore import stateStore

class stateBase( object ) :

   # Constructor
   def __init__(self, config) :
      self.ss = stateStore()
      self.config = config

   # Destructor
   def __del__(self):
      pass

   # State Entry Processing
   def enterState(self):
      pass

   # State Exit Processing
   def exitState(self):
      pass

   # State Periodic Processing
   def run(self):
      pass
