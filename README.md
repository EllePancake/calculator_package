# Calculator Package
Welcome to the Calculator package! This package provides a Calculator class that allows you to perform basic mathematical operations and manipulate a memory value.

Installation
You can install the Calculator package using pip. Open your terminal or command prompt and run the following command:
!pip install git+https://github.com/EllePancake/calculator_package.git

Usage
To use the Calculator package, follow the example below:
from calculator_package import Calculator

## Create an instance of the Calculator
calculator = Calculator()

## Perform addition
result = calculator.add(5, 3)
print(f"Addition result: {result}")

## Perform subtraction
result = calculator.subtract(10, 4)
print(f"Subtraction result: {result}")

## Perform multiplication
result = calculator.multiply(6, 2)
print(f"Multiplication result: {result}")

## Perform division
result = calculator.divide(20, 5)
print(f"Division result: {result}")

## Take the square root of a number
result = calculator.root(16, 2)
print(f"Square root result: {result}")

## Reset the memory
calculator.reset()
print("Memory reset")

## Get the current memory value
memory = calculator.get_memory()
print(f"Memory value: {memory}")
Documentation
Calculator Class
The Calculator class provides the following methods:

- add(x, y): Performs addition of two numbers x and y.
- subtract(x, y): Performs subtraction of two numbers x and y.
- multiply(x, y): Performs multiplication of two numbers x and y.
- divide(x, y): Performs division of two numbers x and y.
- root(x, n): Takes the nth root of a number x.
- reset(): Resets the memory value to 0.

Please refer to the source code and docstrings in the calculator.py file for detailed information on the usage and parameters of each method.

Contributing
If you would like to contribute to the Calculator package, you can fork this repository, make your changes, and submit a pull request. We welcome any improvements or new features that you would like to add.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
If you have any questions or suggestions regarding the Calculator package, feel free to contact me at LibertyMRodriguez.com.

I hope you find the Calculator package useful for your mathematical calculations! :) 
