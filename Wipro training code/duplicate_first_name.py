# List of 20 students as (FirstName, Surname)
students = [
    ("Chandra", "Sekhar"),
    ("Chandra", "Swammy"),
    ("Sunita", "Iyer"),
    ("Raj", "Kapoor"),
    ("Cristiano", "Ronaldo"),
    ("Neha", "Shah"),
    ("Sunil", "Tiwari"),
    ("Suman", "Bose"),
    ("Deepak", "Joshi"),
    ("Sunil", "Gaitonde"),
    ("Cristiano", "Mukherjee"),
    ("Anita", "Desai"),
]

print("Students having SAME first name but DIFFERENT surname:\n")

# Compare each student with every other student
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        first1, last1 = students[i]
        first2, last2 = students[j]

        # Same first name but different surname
        if first1 == first2 and last1 != last2:
            print(first1, last1)
            print(first2, last2)
            print("------")
