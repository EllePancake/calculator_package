class Calculator:
    def __init__(self):
        self.memory: float = 0

    def add(self, value: float) -> None:
        self.memory += value
        print("Memory:", self.memory)

    def subtract(self, value: float) -> None:
        self.memory -= value
        print("Memory:", self.memory)

    def multiply(self, value: float) -> None:
        self.memory *= value
        print("Memory:", self.memory)

    def divide(self, value: float) -> None:
        self.memory /= value
        print("Memory:", self.memory)

    def root(self, n: float) -> None:
        self.memory **= 1/n
        print("Memory:", self.memory)

    def reset(self) -> None:
        self.memory = 0
        print("Memory has been reset:", self.memory)