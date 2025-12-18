# Program to demonstrate break, continue, and pass statements in Python

print("Demonstrating break statement:")
for i in range(1, 6):
    if i == 4:
        # break stops the loop completely when the condition is met
        print("Break encountered. Exiting the loop.")
        break
    print("Value of i:", i)

print("\nDemonstrating continue statement:")
for i in range(1, 6):
    if i == 3:
        # continue skips the current iteration and moves to the next one
        print("Continue encountered. Skipping value 3.")
        continue
    print("Value of i:", i)

print("\nDemonstrating pass statement:")
for i in range(1, 6):
    if i == 2:
        # pass does nothing; it is used as a placeholder
        pass
    print("Value of i:", i)
