with open("./input/Names/invited_names.txt","r") as invited_names:
    names_list = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.read()

for name in names_list:
    name = name.strip()
    new = contents.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="a") as final_file:
        final_file.write(new)
