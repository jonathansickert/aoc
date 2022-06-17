
from typing import NamedTuple


h: int = 0
d: int = 0

class Command(NamedTuple):
    type: str
    param: int


with open("./ressources/dive.txt", "r") as f:
    data = [x.replace("\n", "").split(" ") for x in f.readlines()]
    commands = [Command(x[0], int(x[1])) for x in data]
    for command in commands:
        if command.type == "forward":
            h += command.param
        if command.type == "down":
            d += command.param
        if command.type == "up":
            d -= command.param

solution = h*d

print("Solution dive: ",solution)

