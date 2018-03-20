
min_liste = []

class Dog:
    def __init__(self, voice="Bark", name="Bobby"):
        self.voice = voice
        self.name = name
    
    def speak(self):
        print "I am dog number: " + str(self.voice)


for i in range(20):
    min_liste.append(Dog(i))

print min_liste
min_liste.append(Dog(245))

for i in range(len(min_liste)):
    min_liste[i].speak()

