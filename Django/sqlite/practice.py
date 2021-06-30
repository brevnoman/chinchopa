import sqlite3


x= [["da", "net"], ["pravda", "krovda"], ["do", "does"]]

base = sqlite3.connect("new.db")

cursor = base.cursor()

base.execute(f"CREATE TABLE IF NOT EXISTS {'data'}(login text PRIMARY KEY, password text)")
base.commit()

cursor.execute("INSERT INTO data VALUES(?,?)", ("jora1976", "123qweasdzxc"))
base.commit()

cursor.execute("INSERT INTO data VALUES(?,?)", ("Leha1488", "zeigh_hello_world"))
base.commit()

cursor.executemany("INSERT INTO data VALUES(?,?)", x)
base.commit()

r = cursor.execute("SELECT login FROM data").fetchall()
k = cursor.execute("SELECT password FROM data").fetchall()
one = cursor.execute("SELECT password FROM data WHERE login == ?", ("jora1976",)).fetchone()
print(k)
print(r)
print(one)

cursor.execute("UPDATE data SET password == ? WHERE login == ?", ("dabudidabuday", "jora1976"))
base.commit()
one = cursor.execute("SELECT password FROM data WHERE login == ?", ("jora1976",)).fetchone()
print(one)

cursor.execute("UPDATE data SET password == ?", ("100",))
base.commit()
them_all = cursor.execute("SELECT * FROM data").fetchall()
print(them_all)
cursor.execute("DELETE FROM data WHERE login == ?", ("jora1976",))
base.commit()
base.execute("DROP TABLE IF EXISTS data")
base.commit()
base.close()