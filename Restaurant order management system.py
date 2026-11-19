# Restaurant Order Management System

menu = {
    "Burger": 100,
    "Pizza": 200,
    "Coffee": 50
}

tables = {i: [] for i in range(1, 21)}


def display_menu():
    print("\n------ RESTAURANT MENU ------")
    for item, price in menu.items():
        print(f"{item}: Rs.{price}")


def add_order():
    try:
        table = int(input("\nEnter table number (1-20): "))

        if table < 1 or table > 20:
            print("Invalid table number. Enter a number between 1 and 20.")
            return

    except ValueError:
        print("Invalid table number. Enter a whole number.")
        return

    while True:
        display_menu()
        item = input("\nEnter order item: ").strip().title()

        if item not in menu:
            print("Item not on the menu. Available: Burger, Pizza, Coffee")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Invalid quantity. Enter a whole number greater than 0.")
                continue

        except ValueError:
            print("Invalid quantity. Enter a whole number.")
            continue

        amount = menu[item] * quantity

        tables[table].append({
            "item": item,
            "quantity": quantity,
            "amount": amount
        })

        print(f"{item} x{quantity} added to Table {table} | Amount: {amount}")

        print("\nRunning Order:")
        for order in tables[table]:
            print(
                order["item"], "x", order["quantity"],
                "=", order["amount"]
            )

        more = input("\nAdd another item? (yes/no): ").strip().lower()

        if more != "yes":
            break


def view_order():
    try:
        table = int(input("Enter table number (1-20): "))
        if table not in tables:
            print("Invalid table number. Enter a number between 1 and 20.")
            return
    except ValueError:
        print("Invalid table number.")
        return

    if not tables[table]:
        print("No orders found for this table.")
        return

    print(f"\nRunning Order - Table {table}")
    for order in tables[table]:
        print(
            f"{order['item']} x{order['quantity']} = "
            f"Rs.{order['amount']}"
        )


def generate_bill():
    try:
        table = int(input("Enter table number (1-20): "))
        if table not in tables:
            print("Invalid table number. Enter a number between 1 and 20.")
            return
    except ValueError:
        print("Invalid table number.")
        return

    orders = tables[table]

    if not orders:
        print("No orders found for this table.")
        return

    print("\n========== FINAL BILL ==========")
    print("Table Number:", table)

    subtotal = 0

    for order in orders:
        print(
            f"{order['item']} x{order['quantity']} = "
            f"Rs.{order['amount']:.2f}"
        )
        subtotal += order["amount"]

    service_charge = subtotal * 0.10
    gst = subtotal * 0.05
    total = subtotal + service_charge + gst

    print("--------------------------------")
    print(f"Subtotal: Rs.{subtotal:.2f}")
    print(f"Service Charge (10%): Rs.{service_charge:.2f}")
    print(f"GST (5%): Rs.{gst:.2f}")
    print("--------------------------------")
    print(f"Total: Rs.{total:.2f}")
    print("================================")
    print("Thank you for visiting!")


def main():
    print("RESTAURANT ORDER MANAGEMENT SYSTEM")

    while True:
        print("\n1. Add Order")
        print("2. View Running Order")
        print("3. Generate Bill")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            add_order()

        elif choice == "2":
            view_order()

        elif choice == "3":
            generate_bill()

        elif choice == "4":
            print("Thank you! Application closed.")
            break

        else:
            print("Invalid choice. Please enter 1 to 4.")


if __name__ == "__main__":
    main()