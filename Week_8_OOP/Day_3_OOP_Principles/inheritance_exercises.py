"""
Try to recreate the class explained below:

We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

We can create a class called BlockedDoor that inherits from the base class Door.

We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those
functions, which simply raises an Error that a blocked door cannot be opened or closed.
"""


class Door():
    def __init__(self, is_opened):
        self.is_opened = is_opened

    def open_door(self):
        if self.is_opened:
            print('The Door is already open.')
        else:
            print('The Door has opened.')

    def close_door(self):
        if self.is_opened:
            print('The Door has closed.')
        else:
            print('The Door is already closed.')


class BlockedDoor(Door):
    def open_door(self):
        raise Exception('You cannot open a blocked door')

    def close_door(self):
        raise Exception('You cannot close a blocked door')


door = BlockedDoor(True)
door.open_door()
door.close_door()