# TodList manager
import json 
def load_todo():
    try:
        with open("todo.txt", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_todo(todos):
    with open("todo.txt", 'w') as file:
        json.dump(todos,file)
def add_Todo(todos):
    todo = input("Enter Your Todo")
    todos.append({"todo":todo})
    save_todo(todos)
def get_all_todos(todos):
    for todo , index  in  enumerate(todos , start=1):
        print(f"{index}.  {todo}")
def delete_todo(todos):
    index = int(input("Enter Index no. to delete todo"))
    del todos[index-1]
    save_todo(todos)
def update_todo(todos):
    get_all_todos(todos)
    index  = int(input("Enter index of todo to update: "))
    new_todo = input("Enter New todo name: ")
    todos[index-1] = {"todo": new_todo}
    save_todo(todos)
def main():
    todos = load_todo()

    while True:
        print("\n TodoList Manager")
        print("Press 1 to Add Todo")
        print("Press 2 to delete Todo")
        print("Press 3 to get All Todos")
        print("Press 4 to update Todo")
        print("Press 5 to Exit")

        user_input = input("Enter Your Command: ")

        match user_input:
            case "1":
                add_Todo(todos)
            case "2":
                delete_todo(todos)
            case "3":
                get_all_todos(todos)
            case "4":
                update_todo(todos)
            case "5":
                break
            case _:
                print("Inavlid Command")
   

if __name__ == "__main__":
    main()