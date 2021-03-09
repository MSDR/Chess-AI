#for generally useful helper functions/classes
import inspect, sys

#provides a helpful error message for an undefined function
#function borrowed from UC Berkeley: http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print "|||| ERROR | Function not implemented: %s at line %s of %s" % (method, line, fileName)
    sys.exit(1)

#provides a helpful warning message for a partially defined function, indicating more work may be needed
def raisePartiallyDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print "| WARNING | Function only partially implemented: %s at line %s of %s" % (method, line, fileName)

#provides an error message when something goes wrong in code execution
# error is an error message to be printed before program exit
def raiseError(error):
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print "|||| ERROR |", error, "| in function %s at line %s of %s" % (method, line, fileName)
    sys.exit(1)

#provides a warning message when something goes wrong in code execution
# error is a warning message to be printed before program exit
def raiseWarning(warning):
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print "| WARNING |", warning, "| in function %s at line %s of %s" % (method, line, fileName)
