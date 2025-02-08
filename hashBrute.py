import hashlib
import itertools

# Comprehensive leetspeak dictionary with case swapping for uppercase and lowercase, symbols, and numbers
leet_dict = {
    'A': ['A', '4', '@', '^', 'a'], 'a': ['a', '4', '@', '^', 'A'],
    'B': ['B', '8', 'b', '6'], 'b': ['b', '8', 'B', '6'],
    'C': ['C', '<', 'c'], 'c': ['c', '<', 'C'],
    'D': ['D', 'd'], 'd': ['d', 'D'],
    'E': ['E', '3', '€', '£', 'e', '&'], 'e': ['e', '3', '€', '£', 'E', '&'],
    'F': ['F', '|=', 'ƒ', '/=', 'f'], 'f': ['f', '|=', 'ƒ', '/=', 'F'],
    'G': ['G', '6', '9', '&', 'g'], 'g': ['g', '6', '9', '&', 'G'],
    'H': ['H', '#', '|#', '|-|', 'h'], 'h': ['h', '#', '|#', '|-|', 'H'],
    'I': ['I', '!', 'i'], 'i': ['i', '!', 'I'],
    'J': ['J', '_/', ']', '._.', 'j'], 'j': ['j', '_/', ']', '._.', 'J'],
    'K': ['K', '|<', '|{', 'X', '1<', 'k'], 'k': ['k', '|<', '|{', 'X', '1<', 'K'],
    'L': ['L', '1', '|', '£', '7', '|_', 'l'], 'l': ['l', '1', '|', '£', '7', '|_', 'L'],
    'M': ['M', 'm'], 'm': ['m', 'M'],
    'N': ['N', 'n'], 'n': ['n', 'N'],
    'O': ['O', '*', '0', '()', '[]', 'o'], 'o': ['o', '0', '*', '()', '[]', 'O'],
    'P': ['P', '9', 'p'], 'p': ['p', '9', 'P'],
    'Q': ['Q', '9', '&', '2', '(_,)', 'O_', 'q'], 'q': ['q', '9', '2', '&', '(_,)', 'O_', 'Q'],
    'R': ['R', '12', '®', '2', 'Я', 'r'], 'r': ['r', '12', '®', '2', 'Я', 'R'],
    'S': ['S', '5', '$', 'z', '2', '§', 's'], 's': ['s', '5', '2', '$', 'z', '§', 'S'],
    'T': ['T', '7', '+', '†', '7`', 't'], 't': ['t', '7', '+', '†', '7`', 'T'],
    'U': ['U', '|_|', 'v', 'V', 'L|', 'u'], 'u': ['u', '|_|', 'v', 'V', 'L|', 'U'],
    'V': ['V', 'v'], 'v': ['v', 'V'],
    'W': ['W', 'VV', 'w'], 'w': ['w', 'VV', 'W'],
    'X': ['X', '?', '><', '%', 'x'], 'x': ['x', '?', '><', '%', 'X'],
    'Y': ['Y', 'j', 'J', '7', '`/', '¥', 'y'], 'y': ['y', 'j', 'J', '7', '`/', '¥', 'Y'],
    'Z': ['Z', '2', '7_', 's', '%', 'S', 'z'], 'z': ['z', '2', '7_', 's', '%', 'S', 'Z']
}


# Function to generate all leetspeak combinations (including case variations)
def generate_leetspeak_combinations(city_name):
    leet_combinations = []

    for char in city_name:
        if char in leet_dict:
            # If the character has a leetspeak equivalent, add both lowercase and uppercase versions to the list
            leet_combinations.append(leet_dict[char])
        else:
            # If the character has no leetspeak equivalent, just add the character itself
            leet_combinations.append(char)
    
    # Generate all combinations by taking the Cartesian product of all transformations
    return [''.join(combination) for combination in itertools.product(*leet_combinations)]

# Function to check if a hash match is found for a city name
def find_leetspeak_match(input_file, target_hash):
    # Open the file containing city names
    with open(input_file, 'r') as file:
        cities = file.readlines()
    
    for city in cities:
        city = city.strip()  # Remove any surrounding whitespace or newlines
        
        # Generate all leetspeak combinations for the city name
        combinations = generate_leetspeak_combinations(city)
        
        for leet_city in combinations:
            # Compute the SHA-1 hash of the leetspeak city name
            city_hash = hashlib.sha1(leet_city.encode()).hexdigest()
            
            # Print the leetspeak and hash for reference (optional)
            print(f"City: {city} -> Leetspeak: {leet_city} -> SHA-1: {city_hash}")
            
            # Check if the hash matches the target
            if city_hash == target_hash:
                print(f"Match found! City: {city} -> Leetspeak: {leet_city}")
                return city, leet_city  # Return the matching city and its leetspeak version
    
    print("No match found.")
    return None, None

# Example usage
input_file = 'cities.txt'  # Path to your text file containing city names
target_hash = '5f6b9145ac86d19e917a08e6c20de0c907472a90'  # Replace with the target SHA-1 hash you want to match

find_leetspeak_match(input_file, target_hash)
