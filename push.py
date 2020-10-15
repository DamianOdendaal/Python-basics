import os
import sys

class PushWork():
    def push():
        os.system("git add -A")
        os.system("git commit -m " + str(sys.argv[0]))
        os.system("git push")


PushWork.push()