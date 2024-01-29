user_input = input()
print("yes" if len(user_input.split()) == len(set(user_input.split())) else "no")
