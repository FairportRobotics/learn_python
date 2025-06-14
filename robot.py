"""
CHALLENGE 1

Create a class called `Motor` that has the following attributes:
- `name`: a string representing the name of the motor
- `power`: a float representing the power.  Make the default value 0.0

Create the following methods:
- `__init__`: initializes the `name` and `power` attributes
- `get_power`: returns the current value of the `power` attribute
- `set_power`: sets the value of the `power` attribute to a new value
- `stop`: sets the `power` attribute to 0.0
- `go`: sets the `power` attribute to a given value
"""


class Motor:
    def __init__(self, name: str, power: float = 0.0) -> None:
        self.name = name
        self.power = power

    def get_power(self) -> float:
        return self.power

    def set_power(self, power: float) -> None:
        self.power = power

    def stop(self) -> None:
        self.power = 0.0

    def go(self, power: float) -> None:
        self.set_power(power)


""" 
CHALLENGE 2

Create a class called `Robot` that has the following attributes:
- `name`: a string representing the name of the robot

Create the following methods:
- `__init__`: initializes the `name` attribute, and creates 4 motors with the names "left_front", "right_front", "left_back", and "right_back"
- `go`: sets the power of all motors to a given value
- `stop`: sets the power of all motors to 0.0
"""


class Robot:
    def __init__(self, name: str) -> None:
        self.name = name
        self.left_front = Motor("left_front")
        self.left_back = Motor("left_back")
        self.right_front = Motor("right_front")
        self.right_back = Motor("right_back")

    def stop(self) -> None:
        self.left_back.stop()
        self.left_front.stop()
        self.right_front.stop()
        self.right_back.stop()

    def go(self, power: float) -> None:
        self.left_back.go(power)
        self.left_front.go(power)
        self.right_back.go(power)
        self.right_front.go(power)
