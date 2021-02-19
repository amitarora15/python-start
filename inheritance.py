class Aircraft:

    def __init__(self, registration):
        self._regisration = registration

    def start(self):
        print('Starting filght having model :' + self._regisration + self.model())


class Boeing(Aircraft):
    def model(self):
        return "Boeing"


class A707(Aircraft):
    def model(self):
        return "A707"

