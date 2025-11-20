def generate_profile(age):
    if age < 13:
        lifestage="Child"
        return lifestage
    elif age < 20:
        lifestage="Teenager"
        return lifestage
    else:
        lifestage="Adult"
        return lifestage
user_name = input("Hello! Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)
life_stage = generate_profile(current_age)

user_profile = {"name": user_name, "age": current_age, "stage": life_stage}
user_profile["hobbies"] = hobbies

print('---')
print('Profile Summary:')
print(f"Name: {user_profile["name"]}")
print(f"Age: {user_profile["age"]}")
print(f"Life stage: {user_profile["stage"]}")
if len(user_profile["hobbies"]) != 0:
    print(f"Favorite Hobbies ({len(user_profile["hobbies"])}):")
    for hobby in user_profile["hobbies"]:
        print(f"- {hobby}")
else:
    print("You didn't mention any hobbies.")
print('---')