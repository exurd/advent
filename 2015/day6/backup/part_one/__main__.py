"""
Day 6: Probably a Fire Hazard (Part one)
"""
import sys
from enum import Flag
import re

express = re.compile(r"(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)")


class Power(Flag):
    """Power state flags for lights."""
    ON = True
    OFF = False


class Light():
    """
    Single light class. Can be turned off and on.

    Position kept for debugging purposes.
    """
    def __init__(self, x=0, y=0):
        self.power = Power.OFF
        self.position = {"x": x, "y": y}


    def __str__(self):
        return f"[Light], Position: {self.position}, Power: {self.power}"


    def switch(self, power:Power):
        self.power = power
        return f"Changed {self}"  # allow for string printing change


    def toggle(self):
        self.power = ~self.power
        return f"Changed {self}"  # allow for string printing change


class LightSet():
    """Set of Lights (as in the Light class). x_amount and y_amount specifies the size of the grid (default 1000x1000)"""
    def __init__(self, x_amount=1000, y_amount=1000):
        self.lights = [[Light(x, y) for y in range(y_amount)] for x in range(x_amount)]  # https://stackoverflow.com/a/6667288
        self.size = {"x": x_amount, "y": y_amount}
        # print(self.lights)


    def count(self):
        off, on = 0, 0
        for x in self.lights:
            for light in x:
                # print(light)
                if light.power == Power.ON:
                    on += 1
                else:
                    off += 1
        return on


    def __str__(self):
        return f"[LightSet] Size: {self.size}, Count of lights with power: {self.count()}"


    def toggle_lights(self, start_x, start_y, end_x, end_y):
        """Toggles lights in the set on or off, in specified selection (x, y)"""

        selection_x = ((end_x + 1) - start_x)
        selection_y = ((end_y + 1) - start_y)
        # print(selection_x)
        # print(selection_y)

        for x in range(selection_x):
            for y in range(selection_y):
                light = self.lights[(start_x + x)][(start_y + y)]
                # print(light)
                light.toggle()
        # light.toggle()


    def switch_lights(self, power:Power, start_x, start_y, end_x, end_y):
        """Switch lights in the set to a specified power state, in specified selection (x, y)"""
        selection_x = ((end_x + 1) - start_x)
        selection_y = ((end_y + 1) - start_y)
        # print(selection_x)
        # print(selection_y)

        for x in range(selection_x):
            # print("a")
            for y in range(selection_y):
                # print("b")
                # print((start_x + x))
                # print(start_y + y)
                light = self.lights[(start_x + x)][(start_y + y)]
                # print(light)
                light.switch(power)
        # light.toggle()

file = sys.argv[1]
LightSet = LightSet(1000,1000)

with open(file, mode="r", encoding="utf-8") as file:
    for line in file:
        strip = line.strip()
        # print(strip)
        parse = express.search(strip)

        instruction = parse.group(1)
        start_x = int(parse.group(2))
        start_y = int(parse.group(3))
        end_x = int(parse.group(4))
        end_y = int(parse.group(5))

        power = None
        if instruction == "turn on":
            power = Power.ON
        elif instruction == "turn off":
            power = Power.OFF

        if power is None:  # should be a toggle
            LightSet.toggle_lights(start_x,start_y, end_x,end_y)
        else:
            LightSet.switch_lights(power, start_x,start_y, end_x,end_y)

        # print(parse.group(5))
        
        # print("-----")
print(LightSet)


# light = Light()
# print(light)
# light.switch()
# print(light)

# LightSet = LightSet(10,10)
# LightSet.toggle_lights(2,2, 4,4)
# print("------")
# print(LightSet.lights[3][3])
# print("---------")

# LightSet.switch_lights(Power.ON, 1,1, 1,1)
# print("------")
# print(LightSet.lights[1][2])

# LightSet.switch_lights(Power.ON, 499,499, 500,500)
# print("------")
# print(LightSet.lights[499][499])
# print(LightSet)
# print(LightSet.lights[2][0].toggle()) # x first, y second
