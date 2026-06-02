data = ['Parth', 'Satyarth', 'Shivam', 'Rohit', 'Anshul']

def add_name(name):
    a = input("Enter the name to add: ")
    data.append(f'{a}')
    for i in data:
        print(i)

def remove_name(name):
    b = input("Enter the name to remove: ")
    data.remove(f'{b}')
    for i in data:
        print(i)

def search_name(name):
    c = input("Enter the name to search: ")
    if c.lower() in [n.lower() for n in data]:
        print(f"{c} is in the list.")
    else:
        print(f"{c} is not in the list.")

def main():
    while True:
        print("1. Add a name")
        print("2. Remove a name")
        print("3. Search for a name")
        print("4. Exit")
        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            add_name(data)
        elif choice == '2':
            remove_name(data)
        elif choice == '3':
            search_name(data)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

main()