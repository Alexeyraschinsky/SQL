import sqlite3

conn = sqlite3.connect('dz.db')
crsr = conn.cursor()
conn.execute(
    '''create table if not exists tab_1(id integer primary key autoincrement, col_1 int)''')
conn.commit()
crsr.execute(
    '''select * from tab_1''')
d = crsr.fetchall()


class DATA:
    def bd(self, a=None, b=None, n=None):
        if a is not None and b is None and n is None:
            crsr.execute(
                '''insert into tab_1(col_1) values (3)''')
            conn.commit()
        elif a is not None and b is not None and n is None:
            if type(b) is int:
                crsr.execute(
                    '''delete from tab_1 where id = 1''')
                conn.commit()
            elif a is not None and b is not None and type(n) is int:
                crsr.execute('''update tab_1 col_1 = 77 where id = 3''')
                conn.commit()

a = DATA()
a.bd(8)
crsr.execute('''select * from tab_1''')
d = crsr.fetchall()
print(d)
