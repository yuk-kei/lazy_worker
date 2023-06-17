import os
import random
import sys
import time

# Define grid size
GRID_SIZE = 10

# Define min numbers of shopping carts
MIN_CARTS = 3

# Define max numbers of shopping carts
MAX_CARTS = 11

# Store the number of shopping carts, default generate randomly
num_carts = 0

# Current used algorithm
curr_algo = "Random select"

# Auto Mode
is_auto = True

# Debug Mode
is_debug = False

# Whether the carts are generate randomly
given_carts_pos = False

# Whether the worker's pos are generate randomly
given_worker_pos = False

# Define worker location
# worker_pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
worker_pos = ()

# Store the original position of worker
# worker_org = tuple(worker_pos)
worker_org = ()

# Store position of carts
cart_positions = []

# Store nodes in path
path = []

# Store the route calculated by the current algorithm
routes = []

# Just for debug mode, store the path and path length for other algo option
other_routes = []
other_lens = 0

lens = 0
# Store instructions for each step
step_str = []

# Store carts collected
collected_carts = 0


class Graph:
    paths_n_lens = {}

    all_paths = []

    curr_lens = 0

    def __init__(self, width: int, height: int, cart_positions: list, worker_pos):
        self.width = width
        self.height = height
        self.cart_positions = cart_positions
        self.worker_pos = worker_pos
        self.cart_numbers = len(self.cart_positions)
        self.paths_n_lens = self.find_all_path()
        self.all_paths = list(self.paths_n_lens.keys())

    def find_shortest_path(self):
        """
        return the shortest path by dfs

        :param self: Represent the instance of the class
        :return: A list of nodes that represents the shortest path from start to end
        """

        sorted_res = dict(sorted(self.paths_n_lens.items(), key=lambda x: x[1]))
        sorted_all_paths = list(sorted_res.keys())
        shortest_path = sorted_all_paths[0]

        self.curr_lens = sorted_res.get(shortest_path)
        # print(self.curr_lens)
        return list(shortest_path)

    def find_random_path(self):
        """
        Find a random path from the list of all paths.
        It returns a list of nodes that make up the random path.

        :param self: Access the attributes of the class
        :return: A list of nodes that form a path in the graph
        """

        all_paths = list(self.paths_n_lens.keys())
        random_path = all_paths[random.randint(0, len(all_paths) - 1)]
        self.curr_lens = self.paths_n_lens.get(random_path)
        # print(self.curr_lens)
        return list(random_path)

    def find_all_path(self):
        """
        Find all possible paths from the worker's position to each cart, and then back to the worker's position.
        It does this by using a depth-first search algorithm with backtracking.
        It returns a dictionary containing every path as keys, and their corresponding distances as values.

        :param self: Access the class attributes
        :return: A dictionary containing all possible paths and their corresponding length
        """

        paths = []

        path_length = []
        used = [False] * self.cart_numbers

        new_path = [self.worker_pos]

        self.dfs_backtrack(paths, path_length, new_path, used, 0, self.worker_pos)
        path_n_distance = dict(zip(paths, path_length))

        # print(path_length)

        return path_n_distance

    def dfs_backtrack(self, res, path_length, curr_path, used, curr_length, pre_pos):
        """
        The dfs_backtrack helper function

        :param self: Refer to the instance of the class
        :param res: Store all the possible paths
        :param path_length: Store the length of each path
        :param curr_path: Store the current path
        :param used: Track which cart has been used
        :param curr_length: Keep track of the length of the current path
        :param pre_pos: Keep track of the previous position
        :return: A list of tuples, where each tuple is a path from the worker to all carts
        """

        if len(curr_path) == self.cart_numbers + 1:
            curr_path.append(self.worker_pos)
            res.append(tuple(curr_path))
            path_length.append(curr_length + calculate_distance(pre_pos, self.worker_pos))
            curr_path.pop()
            return

        for i in range(self.cart_numbers):

            if used[i]:
                continue

            curr_pos = self.cart_positions[i]

            curr_path.append(curr_pos)
            curr_distance = calculate_distance(pre_pos, curr_pos)
            used[i] = True

            curr_length += curr_distance
            self.dfs_backtrack(res, path_length, curr_path, used, curr_length, curr_pos)

            curr_path.pop()
            curr_length -= curr_distance
            used[i] = False


def calculate_distance(pos1, pos2):
    """
    The calculate_distance function takes two tuples as arguments, each representing a position on the board.
    The function returns the Manhattan distance between these two positions.

    :param pos1: Store the position of one point, and pos2 is used to store the position of another point
    :param pos2: Calculate the distance between two points
    :return: The manhattan distance between two points
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def calculate_path_length(path_list):
    """
    The calculate_path_length function takes a list of nodes and returns the total distance between them.
    The function first calculates the distance between each node in the list, then adds it to a running total.
    Finally, it returns this value.

    :param path_list: Store the path of the salesman
    :return: The total length of a path
    """
    pre = path_list[0]
    dist = 0
    for i in range(1, len(path_list)):
        dist += calculate_distance(pre, path_list[i])
        pre = path_list[i]
    return dist


def clear_screen():
    """ Used to clear the terminal screen."""

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_banner():
    """ Used to print the banner."""

    print(" _                       _  _  ")
    print("| |     __ _      ___   | || | ")
    print("| |__  / _` |    |_ /    \_, | ")
    print("|____| \__,_|   _/__|   _|__/  ")
    print()
    print(" __ __ __  ___      _ _   | |__    ___      _ _ ")
    print(" \ V  V / / _ \    | '_|  | / /   / -_)    | '_|")
    print("  \_/\_/  \___/   _|_|_   |_\_\   \___|   _|_|_ ")
    print()


def display_welcome():
    """ Displays the welcome screen for the program."""

    clear_screen()
    print_banner()
    print('------------------------------------')
    print()
    print('Welcome to Lazy Shopping-cart-worker')
    print("Press 'space' and 'enter' to continue")
    print()
    print('------------------------------------')
    while True:
        # wait for space key to be pressed
        key = input()
        if key == ' ':
            break
        elif key == 'q':
            sys.exit(0)
        else:
            print("Invalid input")


def display_menu():
    """
    Displays the menu for the user to choose from.
    The function will display a list of options and then prompt the user to enter their choice.

    :return: The chosen screen
    """
    print('------------------------------------')
    print()
    print('Menu:')
    print('1. Go get carts')
    print('2. Settings')
    print('3. Exit')
    print()
    print('------------------------------------')
    while True:
        choice = get_menu_choice()

        if choice == '1':
            return go_get_carts()

        elif choice == '2':
            return setting()

        else:
            print('Exiting program...')
            sys.exit(0)


def get_menu_choice():
    """
    The get_menu_choice function prompts the user to enter a number corresponding to one of three menu options.
    The function then returns that choice as a string.

    :return: The user's choice
    """
    while True:
        choice = input('Press the corresponding number and enter to continue: ')
        if choice in ['1', '2', '3']:
            return choice
        else:
            print('Invalid choice. Please try again.')


def setting():
    """
    The setting function is used to change the setting of the program.
    The worker can choose whether they want to display in auto mode or not, and also
    what size of grid they want to play with.

    :return: Back to the menu
    """
    global GRID_SIZE
    global is_auto
    global is_debug
    global worker_pos
    global num_carts
    global worker_org
    global given_carts_pos
    global given_worker_pos
    global curr_algo
    global cart_positions
    clear_screen()
    print('------------------------------------')
    print('Welcome to the setting, please press the corresponding key and enter')
    print()
    print('Automated is on:', is_auto)
    if not given_worker_pos:
        print("Worker's position is: Random generate")
    else:
        print("Worker's position is: ", worker_pos)
    print('Current grid size: ', GRID_SIZE, '*', GRID_SIZE)
    print("Current algorithm is: ", curr_algo)
    print('Debug mode is on:', is_debug)
    print()
    print("If you want to change the auto mode, press '1' ")
    print("If you want to change the worker position, press '2' ")
    print("If you want to change the grid size, press '3' ")
    print("If you want to place the carts manually, press '4' ")
    print("If you want to change the path-finding algorithm, press '5'")
    print("If you want to turn on the debug mode, press '6' ")

    print("press 'r' return to menu")
    print('------------------------------------')

    while True:
        choice = input()

        if choice == '1':

            is_auto = not is_auto
            return setting()

        elif choice == '2':

            while True:
                print("please enter your desire worker position")
                print("worker's x-coordinate is:")
                worker_x = input()
                if worker_x.isnumeric():
                    converted_x = int(worker_x)
                    if 0 <= converted_x < GRID_SIZE:
                        print("worker's y-coordinate is:")
                        worker_y = input()
                        if worker_y.isnumeric():
                            converted_y = int(worker_y)
                            if 0 <= converted_y < GRID_SIZE:
                                worker_pos = (converted_x, converted_y)
                                worker_org = tuple(worker_pos)
                                print("worker's position is:", worker_pos)
                                given_worker_pos = True
                                print("Press any key to continue")
                                input()
                                return setting()
                            else:
                                print('worker y must less than the grid size')
                        else:
                            print("must be number")
                    else:
                        print('worker x must less than the grid size')

                else:
                    print("must be number")

        elif choice == '3':

            while True:
                print("please enter your desire grid size, support from 5x5 parking lot to 20x20")
                size = input()
                if size.isnumeric():
                    converted = int(size)
                    if 5 <= converted <= 20:
                        GRID_SIZE = converted
                        return setting()
                    else:
                        print('size cannot less than 5 or over 20')

                else:
                    print("size must be number")

        elif choice == '4':

            print("carts minium is", MIN_CARTS, " maximum is: ", MAX_CARTS)
            print("Warning: if you want to use brute force, the carts number must not greater than 10")
            num_carts = int(input("Enter the number of carts: "))
            carts = []

            # Loop over the number of carts and prompt the user to enter each position
            for i in range(num_carts):
                cart_input = input(f"Enter the position of cart {i + 1} (x,y): ")
                cart_pos = tuple(map(int, cart_input.split(',')))
                carts.append(cart_pos)

            cart_positions = list(carts)
            given_carts_pos = True
            # Print the list of cart positions
            print("Cart positions:", cart_positions)

        elif choice == '5':

            while True:
                print("If you want to choose path randomly, press '1' ")
                print("If you want to choose shortest path base on brute force(dfs), press '2' ")
                print("Warning: if you want to use brute force(dfs), the carts number must not greater than 10")
                chosen_algo = input()
                if chosen_algo == '1':
                    curr_algo = "Random select"
                    print("current algorithm set to choose path randomly")
                    time.sleep(1)
                    return setting()
                elif chosen_algo == '2':
                    curr_algo = "Brute force DFS"
                    print("current algorithm set to use brute force(dfs)")
                    time.sleep(1)
                    return setting()
                else:
                    print('Invalid input')

        elif choice == '6':

            is_debug = not is_debug
            return setting()

        elif choice == 'r':
            # handle option 2
            return display_menu()
        else:
            # handle option 3
            print('Invalid input...')


def go_get_carts():
    """
    It initializes a graph and refreshes the UI, then prompts user to press 'p' to begin get carts or 'b' to return
    to menu. If user presses p, it calls get_path() to begin display steps to collect carts

    :return: collect carts path or menu
    """
    global routes
    global curr_algo
    # global random_worker
    # global random_carts
    init_graph()
    refresh_UI()

    while True:

        print("Press 's' to start selecting carts")
        # print("Press 'r' to shuffle the worker and carts position")
        print("Press 'b' return to menu")
        key = input()

        if key == 's':

            if curr_algo == "Random select":
                routes = [worker_org]
                routes += cart_positions
                routes.append(worker_org)
            elif curr_algo == "Brute force DFS":
                graph = Graph(GRID_SIZE, GRID_SIZE, cart_positions, worker_pos)
                print("Initializing... please wait")
                routes = graph.find_shortest_path()

            return get_path()

        # elif key == 'r':
        #     random_carts = True
        #     random_worker = True

        elif key == 'b':
            # handle option 2
            print('Back to Menu')
            return display_menu()

        elif key == 'p':

            graph = Graph(GRID_SIZE, GRID_SIZE, cart_positions, worker_pos)
            print("Initializing... please wait")
            routes = graph.find_shortest_path()
            curr_algo = "Brute force DFS"

            return get_path()

        else:
            print('Invalid input...')


def init_graph():
    """
    Initializes the state and start a new round,
    Random generates the carts position and clear the previous record
    """

    global num_carts
    global collected_carts
    global worker_pos
    global worker_org
    global routes
    global other_routes
    global other_lens
    step_str.clear()
    path.clear()
    routes.clear()
    collected_carts = 0
    if not given_worker_pos:
        worker_pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        worker_org = tuple(worker_pos)

    if not given_carts_pos:
        cart_positions.clear()
        num_carts = random.randint(MIN_CARTS, MAX_CARTS)
        while len(cart_positions) < num_carts:
            pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if pos != worker_pos and pos not in cart_positions:
                cart_positions.append(pos)
                # cart_positions.sort()

    if is_debug:
        graph = Graph(GRID_SIZE, GRID_SIZE, cart_positions, worker_org)
        if curr_algo == "Random select":
            other_routes = graph.find_shortest_path()
            other_lens = graph.curr_lens
        elif curr_algo == "Brute force DFS":
            other_routes = graph.find_random_path()
            other_lens = graph.curr_lens


def refresh_UI():
    """ Clearing the screen, printing out the current state of the program."""

    clear_screen()
    global step_str
    global curr_algo
    print('-----------------------------------------------')
    if is_debug:
        print('Automated is on:', is_auto)
        print('Debug is on:', is_debug)
        print("Worker is originated at: ", worker_org)
        print("Carts positions are: ", cart_positions)
        print('Current grid size: ', GRID_SIZE, '*', GRID_SIZE)
        if len(routes) != 0:
            print("Total in: ", len(routes) - 1, "steps")
        print("Current step: ", collected_carts, "steps")
        print()
        print("path:")
        for s in routes:
            print(s, end=" -> ")

        print()
        if collected_carts > 0:
            print('Collected carts: ', collected_carts - 1)
        else:
            print('Collected carts: ', collected_carts)

        print("Current algorithm is: ", curr_algo)
        if len(routes) == len(cart_positions) + 2:
            print("Current path length is: ", calculate_path_length(routes))

            if curr_algo == "Random select":
                print("Path in Brute force DFS: ")
                for s in other_routes:
                    print(s, end=" -> ")
                print()
                print("Path length: ", other_lens)
            elif curr_algo == "Brute force DFS":
                print("Path in Random select: ")
                for s in other_routes:
                    print(s, end=" -> ")
                print()
                print("Path length: ", other_lens)
    else:
        print_banner()
    print('-----------------------------------------------')
    print_grid()


def print_grid():
    """ The print_grid function prints a grid of the current state of map. """

    global collected_carts
    for i in range(GRID_SIZE + 1):
        if i == 0:
            print(" ", end="  ")

        elif 0 < i < 10:
            print(i - 1, end="  ")
        elif i >= 10:
            print(i - 1, end=" ")
    print()
    for x in range(GRID_SIZE):
        if 0 <= x < 10:
            print(x, end="  ")
        elif x >= 10:
            print(x, end=" ")
        for y in range(GRID_SIZE):
            if (x, y) == worker_pos:
                print("\U0001F605", end=" ")
            elif (x, y) in cart_positions:
                print("\U0001F6D2", end=" ")
            elif (x, y) in path:
                print("*", end="  ")
            else:
                print("_", end="  ")
        print()
    print()


def find_next_path(cart_pos=worker_pos):
    """
    Find the next path for the worker to take.
    It takes in a cart position as an argument and uses that position to calculate how many steps it will take
    to get there.

    :param cart_pos: The position of the next cart
    """

    global worker_pos
    global step_str
    curr_worker = worker_pos
    x_dist = cart_pos[0] - curr_worker[0]
    y_dist = cart_pos[1] - curr_worker[1]
    x_dir = "down" if x_dist > 0 else "up"
    y_dir = "right" if y_dist > 0 else "left"
    x_moves = abs(x_dist)
    y_moves = abs(y_dist)
    new_x = curr_worker[0]
    new_y = curr_worker[1]
    for i in range(x_moves):
        visited = (new_x, new_y)
        path.append(visited)
        if x_dist > 0:
            new_x += 1
        elif x_dist < 0:
            new_x -= 1

    for i in range(y_moves):
        visited = (new_x, new_y)
        path.append(visited)
        if y_dist > 0:
            new_y += 1
        elif y_dist < 0:
            new_y -= 1
    worker_pos = cart_pos

    step = collected_carts
    # if cart_pos != worker_pos:
    #     step = collected_carts
    # else:
    #     step = collected_carts + 1

    message = 'Step ' + str(step) + ": Go to " + str(cart_pos) + ' (Move ' + str(x_dir) + " " + \
              str(x_moves) + " units. Move " + str(y_dir) + " " + str(y_moves) + ' units.)'

    step_str.append(message)

    refresh_UI()
    print("path:")
    for s in step_str:
        print(s)


def get_path():
    """
    The get_path function will iterate through all the cart positions and back to original place
    to generate a path for worker to collect all the shopping-carts.

    :return: Other screens
    """

    global routes
    global worker_pos
    global collected_carts

    # paths = list(cart_positions)
    # paths.append(worker_org)
    for i in range(1, len(routes)):
        collected_carts += 1
        cart_pos = routes[i]
        if is_auto:
            find_next_path(cart_pos)
            time.sleep(0.5)
        else:
            print("Press 'space' to continue, press 'r' to reset, press 'q' to quit")
            while True:
                key = input()
                if key == ' ':
                    find_next_path(cart_pos)
                    break
                elif key == 'r':
                    return go_get_carts()
                elif key == 'q':
                    return display_menu()
                else:
                    print("Invalid input")
    print()
    # print("Congratulations! You collected all the carts")
    # time.sleep(3)
    # find_next_path()
    #
    # print("Back to origin")
    print("Congratulations! You collected all the carts")
    print()
    print("press r to reset, press q return to menu")
    while True:
        key = input()
        if key == 'q':
            return display_menu()
        elif key == 'r':
            return go_get_carts()
        else:
            print("Invalid input")


def main():
    """
    The entry point of the program. It calls all other functions in order to display a menu,
    and then it allows users to select from that menu.
    """

    display_welcome()
    display_menu()


if __name__ == '__main__':
    main()
