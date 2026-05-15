import json

TODO_FILE = "todos.json"

def load_todos():
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(todos, file, indent=2)
def show_todos(todos):
    if not todos:
        print("No todos yet.")
    for index, todo in enumerate(todos, 1):
        status = "done" if todo["done"] else "todo"
        print(f"{index}. [{status}] {todo['task']}")
def complete_todo(todos):
    show_todos(todos)
    try:
        todos[int(input("Number to complete: ")) - 1]["done"] = True
        save_todos(todos)
        print("Todo completed.")
    except (ValueError, IndexError):
        print("Please enter a valid todo number.")
def main():
    todos = load_todos()
    while True:
        print("\n1. Add todo  2. Complete todo  3. View todos  4. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            task = input("Todo: ").strip()
            if task:
                todos.append({"task": task, "done": False})
                save_todos(todos)
            print("Todo added." if task else "Todo cannot be empty.")
        elif choice == "2":
            complete_todo(todos)
        elif choice == "3":
            show_todos(todos)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()
