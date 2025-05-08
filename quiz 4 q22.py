class Organ:
    def __init__(self):
        pass


class Heart(Organ):
    def __init__(self, blood):
        super().__init__()
        self.blood = blood

    def beat(self):
        print("Heart is beating.")


class Brain(Organ):
    def __init__(self, thoughts):
        super().__init__()
        self.thoughts = thoughts

    def think(self, thought):
        self.thoughts.append(thought)
