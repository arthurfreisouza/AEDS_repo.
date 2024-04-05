class Node:
    def __init__(self, value):
        self.value_ = value
        self.next_ = None

    def show_value(self):
        return (self.value_, self.next_)
    