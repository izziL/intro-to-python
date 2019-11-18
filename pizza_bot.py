# Make a list of all the accepted toppings.
toppings = ["Grilled Chicken", "Pepperoni", "Beef", "Spicy Italian Sausage", "Bacon", "Sausage", "Canadian Bacon", "Mushrooms", "Green Olives", "Roma Tomatoes", "Pineapple", "Onions", "Black Olives", "Jalapeño Peppers", "Banana Peppers", "Green Peppers"]

# These are the pizzas the pizza bot will be making.
firstPizza = ["Sausage", "Pepperoni", "Onions", "Green Peppers"]
secondPizza = ["Spicy Italian Sausage", "Skittles", "Pork Chops", "Mushrooms", "Brownies"]
thirdPizza = ["Canadian Bacon", "Jalapeño Peppers, but not the gross pickled kind, because those give me a stomachache", "Grilled Onions", "Pineapple"]
fourthPizza = ["Pepperoni", "Spicy Italian Sausage", "Bacon", "Canadian Bacon"]
fifthPizza = ["Roma Tomatoes", "Mozzarella Slices"]
sixthPizza = ["Marshmallows", "Peanut Butter", "Hershey Kisses", "Pineapple", "Cinnamon"]

# The pizzabot funciton.
def pizzabot(pizzas):
    # Make a for loop to run it for each pizza in the list.
    for pizza in pizzas:
        # Pizzabot receives the order.
        print("I have received the order for your pizza!")
        # Pizzabot keeps track of the ingredients on the pizza.
        ingredientsOnPizza = []
        # Pizzabot decides if it can put an ingredient on a pizza.
        for ingredient in pizza:
            # If an ingredient can be added, it tells the customer this and add it to the list of ingredients on the pizza.
            if ingredient in toppings:
                ingredientsOnPizza.append(ingredient)
                print("I can put " + ingredient.lower() + " on the pizza.")
            # Otherwise, Pizzabot tells the customer that the ingredient can't be added.
            else:
                print("Sorry, I can't put " + ingredient.lower() + " on the pizza.")
        # Pizzabot bakes the pizza.
        print("I am now baking your pizza.")
        # Pizzabot tells the customer which toppings the completed pizza has.
        print("Your pizza is complete! It has the following ingredients on it:", end = " ")
        for topping in ingredientsOnPizza:
            print(topping.lower(), end = " ")
        print(".")

# Run the program for each pizza.
pizzasToMake = [firstPizza, secondPizza, thirdPizza, fourthPizza, fifthPizza, sixthPizza]
pizzabot(pizzasToMake)
