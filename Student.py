students = []

# ===== FUNCTIONS =====
def add_student():
    name = input("Enter name: ")
    math = float(input("Math score: "))
    physics = float(input("Physics score: "))
    english = float(input("English score: "))

    avg = (math + physics + english) / 3

    student = {
        "name": name,
        "math": math,
        "physics": physics,
        "english": english,
        "avg": avg
    }

    students.append(student)
    print("✅ Student added!\n")


def show_students():
    if not students:
        print("❌ No students yet.\n")
        return

    print("\n===== STUDENT LIST =====")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} | Avg: {s['avg']:.2f}")
    print()


def delete_student():
    show_students()
    if not students:
        return

    idx = int(input("Choose number to delete: ")) - 1

    if 0 <= idx < len(students):
        removed = students.pop(idx)
        print(f"🗑 Deleted {removed['name']}\n")
    else:
        print("❌ Invalid choice\n")


# ===== MAIN MENU =====
while True:
    print("====== MENU ======")
    print("1. Add student")
    print("2. Show students")
    print("3. Delete student")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Bye 👋")
        break
    else:
        print("❌ Invalid option\n")
