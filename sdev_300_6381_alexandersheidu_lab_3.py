import matplotlib.pyplot as plt
from PIL import Image

# Name: Alexander Sheidu
# Course: SDEV 300/6381
# Date: January 17, 2024


def menu():
    """This gets the menu and displays it and loops it for
each question."""

    # This is the items list
    items = ["Display", "Search", "Graph", "Update", "Exit"]
    # This is the loop
    for i in range(len(items)):
        print(str(i + 1) + ". " + items[i])

# Load states data


def load(file):
    """This loads the file, to be able to use the CSV file."""
    # Opens the file
    f = open(file, "r")
    lines = f.readlines()
    # Closes the file
    f.close()

    # Initialize the map
    map = {}
    for line in lines:
        tokens = line.strip().split(',')
        state_name = tokens[0].strip().lower()  # Convert state name to lowercase
        map[state_name] = [tokens[2].strip(), tokens[3].strip(), int(tokens[4].strip())]

    return map

def display(states):
    """This is for the display function, which displays the
    U.S. States in Alphabetical order along with the Capital,
    State Population, and Flower."""

    # Loop for all of the states
    for state in states:
        # Capitalize the first letter of each word
        display_name = state.title()

        print(display_name, end=': ')
        for str in states[state]:
            print(str, end=' ')
        print()

def display_flower_image(flower_name):
    """This function displays the image of the associated state flower."""
    # Assuming your image files are named after the states
    image_path = f"{flower_name.lower()}.png"  # Update the extension if necessary

    print("Image Path:", image_path)  # Add this line for debugging

    try:
        # Open and display the image using PIL and matplotlib
        img = Image.open(image_path)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    except FileNotFoundError:
        print(f"Image file not found for {flower_name}.")

def search(states):
    """This function is to search for the state and display the appropriate Capital,
    State Population, and the associated State Flower."""

    state = input("Please enter the name of the state to search: ").lower()
    state_info = states.get(state)

    if state_info:
        print(f"Capital: {state_info[0]}, State Population: {state_info[2]}, Flower: {state_info[1]}")

        # Display the state flower image automatically
        display_flower_image(state)
    else:
        print("State not found.")

def graph(states):
    """This is to get the Bar graph of the top 5 populated
    States showing their overall population."""
    sstates = sorted(states.items(), key=lambda x: x[1][2], reverse=True)
    # Empty arrays initialized
    x = []
    y = []
    for state in sstates[:5]:
        # Capitalize the first letter of each state name
        x.append(state[0].capitalize())
        y.append(state[1][2])

    plt.bar(x, y)
    plt.show()


def update(states):
    """This function is to update the population."""
    state = input(
        "Please enter the name of the state to update its population: ").lower()
    pop = int(input("Please enter its population to update: "))
    states[state][2] = pop


def main():
    """This function is the main function, which checks
to see which menu option is selected."""
    states = load("States.csv")
    print("Welcome to the States App")
    # Loop for each option
    while True:
        print("Please choose from the following options: ")
        menu()
        choice = input()
        # If else statement and cases for each option chosen
        if (not choice.isdigit()):
            print("Invalid choice, please choose again.")
        else:
            c = int(choice)
            match(c):
                case 1:
                    display(states)
                case 2:
                    search(states)
                case 3:
                    graph(states)
                case 4:
                    update(states)
                case 5:
                    break
                case _:
                    print("Invalid choice, please choose again.")
    # Thank you message
    print("Thank you for using the States App!")


# Check to see if the script is being executed as the main program
if __name__ == "__main__":
    # If true, execute the main function
    main()

