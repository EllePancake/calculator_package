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
        self._validate_input(value)
        self.memory += value
        print("Memory:", round(self.memory, 6))

    def subtract(self, value: float) -> None:
        """
        Subtracts the specified value from the memory.

        Args:
            value (float): The value to be subtracted.
            
        Raises:
            ValueError: If the value is not a valid number.
        """
        self._validate_input(value)
        self.memory -= value
        print("Memory:", round(self.memory, 6))

    def multiply(self, value: float) -> None:
        """
        Multiplies the memory by the specified value.

        Args:
            value (float): The value to be multiplied with the memory.

        Raises:
            ValueError: If the value is not a valid number.
        """
        self._validate_input(value)
        self.memory *= value
        print("Memory:", round(self.memory, 6))

    def divide(self, value: float) -> None:
        """
        Divides the memory by the specified value.

        Args:
            value (float): The value to be divided by.

        Raises:
            ValueError: If the value is not a valid number.
            ZeroDivisionError: If the value is zero.
        """
        self._validate_input(value)
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        self.memory /= value
        print("Memory:", round(self.memory, 6))

    def root(self, n: float) -> None:
         """
        Takes the n-th root of the memory.

        Args:
            n (float): The root to be taken.

        Raises:
            ValueError: If the memory is a negative number.
            ValueError: If the value is not a valid number.
        """
        self._validate_input(n)
        if self.memory < 0:
            raise ValueError("Cannot take the root of a negative number.")
        
        self.memory **= 1/n
        print("Memory:", round(self.memory, 6))

    def reset(self) -> None:
         """
        Resets the memory to 0.
        """
        self.memory = 0
        print("Memory has been reset:", self.memory)
        
    def _validate_input(self, value: float) -> None:
        """
        Validates if the input value is a valid number.

        Args:
            value (float): The value to be validated.

        Raises:
            ValueError: If the value is not a valid number.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid input. Please enter a valid number.")
