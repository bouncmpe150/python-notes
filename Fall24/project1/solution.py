import turtle
# Grocery List Making Project (Using Recursion and Direct File Writing)

# 1. Creating the Grocery List and writing to file using recursion
def create_grocery_list_and_save(filename):
    f = open(filename, 'a')  # Open the file for writing and appending new items

    # First item input
    item = input("Enter an item (or type 'done' to finish): ")
    if item.lower() == 'done':
        f.close()  # Close the file if user is done
        print(f"Grocery list saved to {filename}.")
        return  # Exit the function

    quantity = input(f"Enter the quantity for {item}: ")
    category = input(f"Enter the category for {item}: ")

    # Write the item details directly to the file
    f.write(f"{item} - {quantity} - {category}\n")

    # Call the function again to process the next item
    create_grocery_list_and_save(filename)

# Creating grocery list and saving it to grocery_list.txt
create_grocery_list_and_save('grocery_list.txt')

# 2. Price Input from Stores using recursion and writing to file
def input_prices_and_save(filename, store_prices=None, store_number=1, num_stores=None):
    # Initialize file only on the first call
    if store_prices is None:
        store_prices = {}
    if num_stores is None:
        num_stores = int(input("\nHow many stores do you want to compare? "))

    # Base case: if we've processed all stores, return the store_prices
    if store_number > num_stores:
        # Write all store prices to the file
        with open(filename, 'w') as f:  # Open the file once for writing
            for store, prices in store_prices.items():
                f.write(f"{store}:\n")
                for item, price in prices.items():
                    f.write(f"  {item}: {price:.2f} TL\n")
        return store_prices

    print(f"Enter prices for Store {store_number}")
    store_name = input(f"Enter the name for Store {store_number}: ")
    store_prices[store_name] = {}

    # Recursive function to get prices for each item
    def input_item_prices(item_index=0):
        if item_index >= len(grocery_list):
            return  # Finished entering prices for this store

        item = grocery_list[item_index]['item']
        price = float(input(f"Enter the price for {item} at {store_name}: "))
        store_prices[store_name][item] = price

        # Recursive call for the next item
        input_item_prices(item_index + 1)

    input_item_prices()  # Start the recursive price input
    return input_prices_and_save(filename, store_prices, store_number + 1, num_stores)




 # Initialize grocery_list from the previously saved file
grocery_list = []
with open('grocery_list.txt', 'r') as f:
    def load_grocery_list(line_index=0):
        line = f.readline()
        if not line:  # Base case: no more lines
            return
        item, quantity, category = line.strip().split(' - ')
        grocery_list.append({"item": item, "quantity": quantity, "category": category})
        load_grocery_list(line_index + 1)  # Recursive call for the next line

    load_grocery_list()  # Load grocery list recursively

 # Saving prices to prices.txt
store_prices = input_prices_and_save('prices.txt')
print("Prices saved to prices.txt.")


# 3. Compare Prices using recursion
def compare_prices(grocery_list, store_prices, item_index=0, cheapest_stores=None):
    if cheapest_stores is None:
        cheapest_stores = {}

    if item_index >= len(grocery_list):
        return cheapest_stores

    item = grocery_list[item_index]['item']
    cheapest_store = None
    lowest_price = float('inf')

    def check_stores(store_index=0):
        nonlocal cheapest_store, lowest_price
        if store_index >= len(store_prices):
            return  # Base case: all stores processed

        store = list(store_prices.keys())[store_index]
        price = store_prices[store][item]
        if price < lowest_price:
            lowest_price = price
            cheapest_store = store

        check_stores(store_index + 1)  # Recursive call for the next store

    check_stores()  # Start checking stores
    cheapest_stores[item] = (cheapest_store, lowest_price)
    return compare_prices(grocery_list, store_prices, item_index + 1, cheapest_stores)


# Finding and displaying the cheapest store for each item
cheapest_stores = compare_prices(grocery_list, store_prices)


# Display cheapest store information
def display_cheapest_stores(cheapest_stores, index=0):
    if index >= len(cheapest_stores):
        return  # Base case: all items processed

    item = list(cheapest_stores.keys())[index]
    store, price = cheapest_stores[item]
    print(f"The cheapest store for {item} is {store} at {price:.2f}TL.")

    display_cheapest_stores(cheapest_stores, index + 1)  # Recursive call for the next item


display_cheapest_stores(cheapest_stores)


# 4. Generate Shopping Plan using recursion
def generate_shopping_plan(cheapest_stores, item_index=0):
    # Open the file on the first call and write the header
    f = open('shopping_plan.txt', 'a')


    # Get the list of items from the cheapest_stores dictionary
    items = list(cheapest_stores.keys())

    # Base case: if we've processed all items, close the file and return
    if item_index >= len(items):
        f.write("Shopping Plan (Cheapest Options):\n")
        f.close()  # Close the file when done
        return

    # Get the current item, store, and price
    item = items[item_index]
    store, price = cheapest_stores[item]

    # Write the current item to the file
    f.write(f"Buy {item} at {store} for {price:.2f}\n")

    # Recursive call for the next item
    generate_shopping_plan(cheapest_stores, item_index + 1)


# Generate and save the shopping plan
generate_shopping_plan(cheapest_stores)
print("Shopping plan saved to shopping_plan.txt.")


# 5. Function – Calculate Total Cost using recursion
def calculate_total_cost(store_prices, grocery_list, store_list=None, index=0):
    if store_list is None:
        store_list = list(store_prices.keys())

    if index >= len(store_list):
        return {}

    store = store_list[index]
    total_cost = 0.0

    # Calculate total cost recursively
    def calculate_item_cost(item_index=0):
        nonlocal total_cost
        if item_index >= len(grocery_list):
            return  # Base case: all items processed
        total_cost += store_prices[store][grocery_list[item_index]['item']]
        calculate_item_cost(item_index + 1)  # Recursive call for the next item

    calculate_item_cost()  # Start the total cost calculation
    totals = calculate_total_cost(store_prices, grocery_list, store_list, index + 1)
    totals[store] = total_cost

    return totals

total_costs = calculate_total_cost(store_prices, grocery_list)



# 6. Visualizing the Costs using Turtle
def visualize_costs(cheapest_stores):
    turtle.title("Cheapest Grocery Options")
    turtle.bgcolor("white")
    turtle.speed(1)
    turtle.penup()

    num_items = len(cheapest_stores)  # Number of items
    max_height = max(price for _, price in cheapest_stores.values()) * 1.1  # Scale for height

    total_chart_width = 600  # Total width for the chart
    base_width = total_chart_width / (num_items + (num_items - 1) * 0.5)  # Width of each bar
    spacing = 0.5 * base_width  # Space between bars

    start_x = -total_chart_width / 2  # Center the chart horizontally
    y_offset = -100  # Vertical offset for the bottom of the bars

    # Define a color for each item based on its index
    colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#F0FF33"]  # Fixed color scheme

    def draw_bars(item_index=0):
        if item_index >= num_items:
            return  # Base case: all items processed

        item = list(cheapest_stores.keys())[item_index]
        store, price = cheapest_stores[item]
        height = (price / max_height) * 200  # Scale height to a max of 200 pixels

        # Move to the starting position for the bar
        turtle.goto(start_x + item_index * (base_width + spacing), y_offset)
        turtle.setheading(90)  # Point upwards

        # Set color and begin filling
        turtle.fillcolor(colors[item_index % len(colors)])
        turtle.begin_fill()

        turtle.pendown()
        turtle.forward(height)  # Draw upwards
        turtle.right(90)  # Turn right
        turtle.forward(base_width)  # Draw the top of the bar
        turtle.right(90)  # Turn downwards
        turtle.forward(height)  # Draw downwards
        turtle.right(90)  # Face left
        turtle.forward(base_width)  # Return to the bottom left of the bar
        turtle.end_fill()  # End filling the bar

        # Write the product name and price below the bar
        turtle.penup()
        turtle.goto(start_x + item_index * (base_width + spacing) + (base_width / 2), y_offset - 20)
        turtle.write(f"\n{item} at {store}: {price:.2f} TL", align="center",
                     font=("Arial", 12, "bold"))  # Adjusted font size and style

        # Reset the turtle heading to the default facing direction
        turtle.setheading(0)

        draw_bars(item_index + 1)  # Recursive call for the next item

    draw_bars()  # Start drawing bars
    turtle.hideturtle()
    turtle.done()


# Visualize costs with Turtle
visualize_costs(cheapest_stores)

