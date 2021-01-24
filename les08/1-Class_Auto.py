class Auto:
    def __init__(self, verbruik):
        self._verbruik = verbruik
        self._tankinhoud = 0.0

    def get_tankinhoud(self):
        return self._tankinhoud

    def get_verbruik(self):
        return self._verbruik

    def fill(self, volume):
        self._tankinhoud += volume

    def drive(self, afstand):
        self._tankinhoud -= self._verbruik * (afstand/100)

        if self._tankinhoud < 0:
            self._tankinhoud = 0


def main():
    mini = Auto(4.5)
    mini.fill(40)
    mini.drive(50)
    print(mini.get_tankinhoud())


main()
