# crud.py
from utils import create, retrieve, update, delete

def main():
    while True:
        print("\nChoose an action:")
        print("1. Create a district")
        print("2. Retrieve a district")
        print("3. Update a district")
        print("4. Delete a district")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter district name: ")
            create({'name': name})
        elif choice == '2':
            id = int(input("Enter district id: "))
            district = retrieve(id)
            if district:
                print(district)
            else:
                print("District not found.")
        elif choice == '3':
            id = int(input("Enter district id: "))
            name = input("Enter new district name: ")
            update(id, name)
        elif choice == '4':
            id = int(input("Enter district id: "))
            delete(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
