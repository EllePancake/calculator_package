class Calculator:
    def __init__(self):
        # Initializes a Calculator object with an initial memory value of 0.
        self.memory: float = 0
   
    def add(self, value: float) -> None:
        # Adds the specified value to the memory.
        self.memory += value
        print("Memory:", self.memory)

    def subtract(self, value: float) -> None:
        #  Subtracts the specified value from the memory.
        self.memory -= value
        print("Memory:", self.memory)

    def multiply(self, value: float) -> None:
        # Multiplies the memory by the specified value.
        self.memory *= value
        print("Memory:", self.memory)

    def divide(self, value: float) -> None:
        # Divides the memory by the specified value.
        self.memory /= value
        print("Memory:", self.memory)

    def root(self, n: float) -> None:
        # Takes the n-th root of the memory.
        self.memory **= 1/n
        print("Memory:", self.memory)

    def reset(self) -> None:
        # Resets the memory to 0.
        self.memory = 0
        print("Memory has been reset:", self.memory)
