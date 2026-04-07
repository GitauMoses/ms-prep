students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C",
    "Evan": "B",
    "Fiona": "A",
    "George": "D",
    "Hannah": "B",
    "Isaac": "C",
    "Julia": "D"
}

def group_by_grade(students):
    group = {}
    for name, grade in students.items():
        group.setdefault(grade,[]).append(name)
    return group

print(group_by_grade(students))
        