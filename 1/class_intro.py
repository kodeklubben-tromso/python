
import time


class Dog(object):
    def __init__(self):
        self.voice = "Bark"

    def say(self):
        print self.voice

    def say_alot(self, n):
        for i in range(n):
            print self.say()

    def say_alot_while(self, n):
        
        i = 0
        while True:
            self.say()
            time.sleep(0.4)
            i += 1
            if i > n:
                break

    def immitate(self, word):
        self.voice = word

if __name__ == "__main__":
    
    dog = Dog()
    dog.say_alot(6)
    dog.immitate("Moooo")
    dog.say()
    dog.say_alot(6)