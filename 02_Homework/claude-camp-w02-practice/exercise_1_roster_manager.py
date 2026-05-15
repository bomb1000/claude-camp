def add_student(roster):
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    join_date = input("Join date (YYYY-MM-DD): ").strip()
    if not name or not email or not join_date:
        print("Name, email, and join date are required.")
        return
    roster[name.lower()] = {"name": name, "email": email, "join_date": join_date}
    print(f"Added {name}.")


def find_student(roster):
    name = input("Name to search: ").strip().lower()
    student = roster.get(name)
    if not student:
        print("Student not found.")
        return
    print(f"{student['name']} | {student['email']} | {student['join_date']}")


def delete_student(roster):
    name = input("Name to delete: ").strip().lower()
    student = roster.pop(name, None)
    print(f"Deleted {student['name']}." if student else "Student not found.")


def main():
    roster = {}
    actions = {"1": add_student, "2": find_student, "3": delete_student}
    while True:
        print("\n1. Add student  2. Search student  3. Delete student  4. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "4":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(roster)
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
