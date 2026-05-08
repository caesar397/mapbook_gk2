from mapbook_lib.model import users
from mapbook_lib.controler import add_user, print_users, remove_user, update_user, update_user_post, get_user_map

def main():
    while True:
        print("========MENU==========")
        print("0 - Zakończ program")
        print("1 - Dodaj znajomego")
        print("2 - Wyświetl znajomych")
        print("3 - Usuń znajomego")
        print("4 - Aktualizuj znajomego")
        print("5 - Dodaj post")
        print("6 - Wyświetl mapę znajomych")
        choice = int(input("Wybierz opcję w menu: "))
        if choice == 0:
            break
        elif choice == 1:
            add_user(users)
        elif choice == 2:
            print_users(users)
        elif choice == 3:
            remove_user(users)
        elif choice == 4:
            update_user(users)
        elif choice == 5:
            update_user_post(users)
        elif choice == 6:
            get_user_map(users)
        else:
            print("Nieprawidłowa opcja menu!")

if __name__ == '__main__':
    main()