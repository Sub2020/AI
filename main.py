# Define the hourly pay rate
hourly_pay_rate = 50

# Calculate weekly minimum pay for working 40 hours
hours_worked_per_week = 40
weekly_minimum_pay = hourly_pay_rate * hours_worked_per_week

# Display the weekly minimum pay
print("Weekly minimum pay:")
print(f"${weekly_minimum_pay} for working {hours_worked_per_week} hours")

# Calculate overtime pay (assuming overtime is 50% more)
overtime_hours = 10  # Example: 10 hours of overtime
overtime_pay_rate = hourly_pay_rate * 1.5
overtime_pay = overtime_pay_rate * overtime_hours

# Display the overtime pay
print("Overtime:")
print(f"${overtime_pay} for working {overtime_hours} hours (50% more than regular rate)")

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self):
        self.menu_items = {
            1: MenuItem("Burger", 5.99),
            2: MenuItem("Pizza", 7.99),
            3: MenuItem("Salad", 3.99),
            4: MenuItem("Fries", 2.49),
            5: MenuItem("Soda", 1.49),
            6: MenuItem("Momo", 10.99),
        }

    def display_menu(self):
        print("Menu:")
        for num, item in self.menu_items.items():
            print(f"{num}. {item.name} - ${item.price:.2f}")

    def get_item_by_number(self, number):
        return self.menu_items.get(number)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)


def main():
    menu = Menu()
    order = Order()

    print("Welcome to the Menu Order Application!")
    while True:
        menu.display_menu()
        print("Enter the item number to add to your order (or 'q' to quit):")
        user_input = input()

        if user_input.lower() == "q":
            break

        try:
            item_number = int(user_input)
            item = menu.get_item_by_number(item_number)
            if item:
                order.add_item(item)
                print(f"{item.name} added to your order.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid item number or 'q' to quit.")

    print("Your order:")
    for item in order.items:
        print(f"{item.name} - ${item.price:.2f}")

    total = order.calculate_total()
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()

