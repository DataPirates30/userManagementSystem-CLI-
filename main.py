from database import  create_user, get_all_users, update_user, delete_user
from file_handling import log_activity

def main():
    while True: 
        print("\nWelcome to User Management System!")
        print("1. Create User")
        print("2. Read All Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            create_user(name, email, age)
            print("User created successfully!")
        
        elif choice == "2":
            users = get_all_users()
            if users:
                print("\nUsers:")
                for user in users:
                    print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Age: {user['age']}\n")
            else:
                print("No users found!")
        
        elif choice == "3":
            id = int(input("Enter user ID: "))
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            update_user(id, name, email, age)
            print("User updated successfully!")
        
        elif choice == "4":
            id = int(input("Enter user ID: "))
            delete_user(id)
            print("User deleted successfully!")
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice! Please try again.")

if  __name__ == "__main__":
    main()