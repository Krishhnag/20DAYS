import random

# Define the string template with placeholders and required inputs
strg_inpt = {
    " Detective: Hello, I'm Detective {name1}. And you are?\n {name2}: {name2}\n Detective: You're here today under suspicion of robbery.\n {name2}: {Exclamation}\n Detective: That's right, {number} {objects} were stolen from {Storen}, and the crime scene has your {bodypart} written all over it.\n {name2}: {exclamation2}\n Detective: Where were you on the night of {festival}?\n {name2}: We were watching {movie}.\n Detective: The wireless security camera footage shows you {verb} just half a {distance} away from the crime scene.\n Alright. Alright. I'm through with playing games. Where are you from?\n {name2}: {country}"
    : ["name1", "name2", "Exclamation", "number", "objects", "Storen", "bodypart", "exclamation2", "festival", "movie", "verb", "distance", "country"]
}

# Randomly select a string template and its required inputs
selected_string, required_inputs = random.choice(list(strg_inpt.items()))

# Collect the required inputs for the selected string
user_data = {}
for input_field in required_inputs:
    user_data[input_field] = input(f"Please enter {input_field.replace('_', ' ')}: ")

# Format the selected string with user inputs
formatted_string = selected_string.format(**user_data)

# Output the final result
print(f"\nGenerated string:\n{formatted_string}")
