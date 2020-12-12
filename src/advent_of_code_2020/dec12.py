# src/


class Ship:

    _compass = {
        "N": complex(0, 1),
        "E": complex(1, 0),
        "S": complex(0, -1),
        "W": complex(-1, 0),
    }
    _turns = {"L": complex(0, 1), "R": complex(0, -1)}

    def __init__(self):
        self._pos = complex(0, 0)
        self._waypoint = complex(10, 1)  ##hardcoded

    def manhattan(self):
        return abs(self._pos.real) + abs(self._pos.imag)

    def move(self, instr):
        _command = instr[0]
        _value = int(instr[1:])
        if _command in self._compass:
            self._waypoint = self._waypoint + self._compass[_command] * _value
        elif _command in self._turns:
            self._waypoint = self._waypoint * self._turns[_command] ** (_value / 90)
        elif _command == "F":
            self._pos = self._pos + self._waypoint * _value

    def __str__(self):
        return f"({self._pos.real},{self._pos.imag})"


def loadroute(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


route = loadroute("dec12_input.txt")
s = Ship()
print(s)
for instruction in route:
    s.move(instruction)
    print(s)
print(s.manhattan())
