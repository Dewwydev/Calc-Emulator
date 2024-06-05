class CalculatorEmulator:
    def __init__(self):
        self.memory = 0

    def add(self, x):
        self.memory += x

    def subtract(self, x):
        self.memory -= x

    def multiply(self, x):
        self.memory *= x

    def divide(self, x):
        if x != 0:
            self.memory /= x
        else:
            print("Error: Division by zero")

    def clear(self):
        self.memory = 0

    def get_result(self):
        return self.memory

if __name__ == "__main__":
    calculator = CalculatorEmulator()

    while True:
        print("\nCalculator Emulator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Clear")
        print("6. Get Result")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num = float(input("Enter number to add: "))
            calculator.add(num)
        elif choice == '2':
            num = float(input("Enter number to subtract: "))
            calculator.subtract(num)
        elif choice == '3':
            num = float(input("Enter number to multiply: "))
            calculator.multiply(num)
        elif choice == '4':
            num = float(input("Enter number to divide: "))
            calculator.divide(num)
        elif choice == '5':
            calculator.clear()
            print("Memory cleared")
        elif choice == '6':
            result = calculator.get_result()
            print(f"Result: {result}")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
