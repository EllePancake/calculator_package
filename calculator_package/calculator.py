class Calculator:
    def __init__(self):
        """
        Initializes a Calculator object with an initial memory value of 0.
        """
        self.memory: float = 0
   
    def add(self, value: float) -> None:
        """
        Adds the specified value to the memory.

        Args:
            value (float): The value to be added.

        Raises:
            ValueError: If the value is not a valid number.
        """
        self.memory += value
        print("Memory:", self.memory)

    def subtract(self, value: float) -> None:
        """
        Subtracts the specified value from the memory.

        Args:
            value (float): The value to be subtracted.
            
        Raises:
            ValueError: If the value is not a valid number.
        """
        self.memory -= value
        print("Memory:", self.memory)

    def multiply(self, value: float) -> None:
        """
        Multiplies the memory by the specified value.

        Args:
            value (float): The value to be multiplied with the memory.

        Raises:
            ValueError: If the value is not a valid number.
        """
        self.memory *= value
        print("Memory:", self.memory)

    def divide(self, value: float) -> None:
        """
        Divides the memory by the specified value.

        Args:
            value (float): The value to be divided by.

        Raises:
            ValueError: If the value is not a valid number.
        """
        self.memory /= value
        print("Memory:", self.memory)

    def root(self, n: float) -> None:
         """
        Takes the n-th root of the memory.

        Args:
            n (float): The root to be taken.

        Raises:
            ValueError: If the memory is a negative number.
            
        Raises:
            ValueError: If the value is not a valid number.
        """
        if self.memory < 0:
            raise ValueError("Cannot take the root of a negative number.")
        
        self.memory **= 1/n
        print("Memory:", self.memory)

    def reset(self) -> None:
         """
        Resets the memory to 0.
        """
        self.memory = 0
        print("Memory has been reset:", self.memory)
