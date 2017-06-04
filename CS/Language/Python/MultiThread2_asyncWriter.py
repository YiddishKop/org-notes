# MultiThreading - 2
# Asynchronous Tasks
# Some tasks can take a long time. Input and output for example can take a long time.
# Some programs are required to be real time. So we can setup Threads to run in the background to write a file or search for items while the user can still interact with the interface or commandline.
# Custom Threads
# We can make our own thread subclasses.
# These are useful for making task specific threads that we can simply reuse as well as add features to the thread.
# Can make managing harder or more simple depending on how advanced we make our threading.

# AsyncWrite Program
# A basic threading program that writes a file in the background.
# A custom thread class will be created to take a string and save it to a file in the background.
# We will make it sleep for a second so we can see it working.


import threading
import time

class AsyncWriter(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out


    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        # 2 second
        time.sleep(2)

        print("Finished Backgroud File Write to " + self.out)

def Main():
    message = input("Enter a string to store:")
    background = AsyncWriter(message, 'out.txt')
    background.start()
    print("The program can continue while it write in another thread")
    print("100 + 400 = ", 100+400)

    # it will still waiting until background thread i done
    # when background is done, it will continue
    background.join()
    print("waited until thread was complete")

if __name__ =="__main__":
    Main()
