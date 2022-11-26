from app.methods import DBases

DB = DBases()

if __name__ == "__main__":
    print("Wellcome, what do you want?\n1)Create base\n2)Exit")
    enter = int(input("Enter: "))
    if enter == 1:
        namedatabase = input("Enter the name of your database: ")
        DB.connect_to_base(namedatabase)
        print("Done! Create table? Y/n")
        createtable = input()
        if createtable == "Y":
            nametable = input("Enter name of table: ")
            DB.create_table(nametable)
            print("Done! Add the user? Y/n")
            adduser = input()
            if adduser == "Y":
               login = input("Enter login: ")
               password = input("Enter password: ")
               DB.add_user(nametable,login,password)
               print("Done! Do you want to see your table? Y/n")
               showtable = input()
               if showtable == "Y":
                    DB.show_info_table(nametable)
               else:
                    DB.exit()
            else:
                DB.exit()
        else:
            DB.exit()
    if enter == 2:
        DB.exit()