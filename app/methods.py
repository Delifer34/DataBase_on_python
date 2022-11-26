import sqlite3 as sq
from sqlite3 import OperationalError
import sys

class DBases():
    def connect_to_base(self, namedatabase):
        try:
            self.con = sq.connect(namedatabase)
            self.cur = self.con.cursor()
        except NameError as err:
           print("No don't enter the name: ", err)
           

    def create_table(self, nametable):
        try:
            self.cur.execute("CREATE TABLE "+nametable+"(login TEXT,password TEXT)")
            self.con.commit()
        except OperationalError as err:
            print("Table already created!", err)
    
    def add_user(self, nametable, login, password):
        print(nametable,login,password)
        self.cur.execute(f"""INSERT INTO {nametable}(login,password) VALUES ("{login}", "{password}")""")
        self.con.commit()
    
    def show_info_table(self,nametable):
        self.cur.execute(f"""SELECT * FROM "{nametable}" """)

    def exit(self):
        sys.exit()