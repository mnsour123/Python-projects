import random

name = input("What is your name: ")
print("Welcome", name, "to this journey!")

inventory = []

answer = input(
    "You stumble upon a lonely road. The wind is cold, and the sky is turning dark.\n"
    "Suddenly, you reach a dead end.\n"
    "Do you want to (A) climb the wall or (B) look for a hidden path? "
).lower()

if answer == "a":
    print("You place your hands on the rough stones and climb. Halfway up, the wall begins to shake...")
    choice = input("Do you (A) jump down or (B) keep climbing? ").lower()

    if choice == "a":
        print("You jump down safely, but a mysterious hooded figure appears.")
        print("The figure hands you a small glowing key.")
        inventory.append("glowing key")
        print("Inventory:", inventory)

    elif choice == "b":
        print("You reach the top and discover an abandoned tower.")
        print("Inside, you find a rusty sword.")
        inventory.append("rusty sword")
        print("Inventory:", inventory)

    else:
        print("Invalid choice, the journey fades away...")

elif answer == "b":
    print("You brush aside the bushes and discover a narrow hidden trail leading underground.")
    choice = input("Do you (A) enter the tunnel or (B) stay outside? ").lower()

    if choice == "a":
        print("Inside the tunnel, ancient carvings whisper your name...")
        print("You find an old map and take it with you.")
        inventory.append("old map")
        print("Inventory:", inventory)

    elif choice == "b":
        print("You stay outside, but the ground begins to rumble...")
        print("A small pouch falls from the sky. Inside is a healing potion.")
        inventory.append("healing potion")
        print("Inventory:", inventory)

    else:
        print("Invalid choice, the journey fades away...")

else:
    print("You stand still, unsure. The world around you slowly disappears...")

print("\nAs you continue your journey...")

enemy = random.choice(["a wild wolf", "a bandit", "a shadow creature"])
print("Suddenly, you are confronted by", enemy + "!")

fight = input("Do you want to (A) fight or (B) run? ").lower()

if fight == "a":
    if "rusty sword" in inventory:
        print("You swing your rusty sword and defeat the enemy!")
    else:
        print("You try to fight with your bare hands but the enemy is too strong.")
        print("You barely escape with your life.")
elif fight == "b":
    print("You run as fast as you can and manage to escape.")
else:
    print("Frozen by fear, you do nothing. The enemy disappears into the shadows.")
