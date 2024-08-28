import requests

# Есть ли возможность при response раскладывать JSON в консоли по нескольким строчкам?

ADD_TASK = 1
DELETE_TASK = 2
GET_ALL_TASKS = 3
QUIT = 4


def main():
    choice = "string"
    while choice != QUIT:
        choice = menu()
        if choice == ADD_TASK:
            add_the_task()
        elif choice == DELETE_TASK:
            delete_the_task()
        elif choice == GET_ALL_TASKS:
            get_all_tasks()
    print("See you soon!")


def menu():
    print()
    print("Menu")
    print("-----")
    print('"1" - Add a new task.')
    print('"2" - Delete the task.')
    print('"3" - See all tasks.')
    print('"4" - Quit the program.')
    print("-----")
    choice = int(input("Enter you choice: "))
    print()
    while choice < ADD_TASK or choice > QUIT:
        choice = int(input("Enter a valid choice: "))
    return choice


def add_the_task():
    url_to_post = "http://127.0.0.1:5000/tasks"
    title = input("Enter the title of your task: ")
    description = input("Enter the description of your task: ")
    data = {"title": title, "description": description}

    response = requests.post(url_to_post, json=data)
    print(response.json())


def delete_the_task():
    number = int(input("Enter the number of task that you want to delete: "))
    url_to_delete = f"http://127.0.0.1:5000/tasks/{number}"
    response = requests.delete(url_to_delete)
    print(response.json())


def get_all_tasks():
    url_to_get = "http://127.0.0.1:5000/tasks"
    response = requests.get(url_to_get)
    print(response.json())


if __name__ == "__main__":
    main()
