class Dog:
    def __init__(self, n, w):
        self.name = n
        self.weight = w

    def feed(self, w):
        self.weight += w

    def __str__(self):
        return "Name: " + str(self.name) + "\nWeight: " + str(self.weight)