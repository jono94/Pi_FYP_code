import sys
#
# A simple shared state mediator for holding state variables in an internal dictionary
#
# An implementation of the Monostate patter using the Borg approach.
#

class stateStore( object ):

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def getVal( self, valName ):
        result = self.__shared_state.get( valName, 0 )
        return result

    def putVal( self, valName, value ):
        self.__shared_state[valName] = value
        return True

    def printStateStore(self):
        for key in sorted(self.__shared_state):
            strOut = key + ' '*40
            strOut = strOut[0:40] + " : " + str(self.__shared_state[key])
            print strOut

    def valExists(self, valName ):
        valueExists = False

        try:
           result = self.__shared_state[valName]
           valueExists = True
        except:
           valueExists = False

        return valueExists

    def printStateStoreCsv(self):
        for key, value in self.__shared_state.items():
            sys.stdout.write( str(value) + ',' )

        print ""
    

