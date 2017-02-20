import sys
import sqlite3
import os
import os.path


def main(dbname):
    con = sqlite3.connect(dbname)

    con.execute("CREATE TABLE IF NOT EXISTS rooms(id INTEGER PRIMARY KEY, name TEXT NOT NULL,"
                " description TEXT NOT NULL)")
    con.commit()

    path = "/home/matthew/PycharmProjects/text_adventure/rooms"

    for f in os.listdir(path):
        f_n = os.path.join(path, f)
        base, extension = os.path.splitext(f)
        if extension == '.json' and 'r' in base:
            with open(f_n, 'r') as fa:
                json = fa.read()
                if len(base) == 3:
                    s = base[1]+base[2]
                else:
                    s = base[1]

                print("Inserting room {0}".format(int(s)))
                
                con.execute("INSERT OR REPLACE INTO rooms(id, name, description)"
                            "VALUES(?, ?, ?);", (int(s), json.decode('utf8'), json.decode('utf8')))
                con.commit()

    con.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: {0} <database name>'.format(sys.argv[0]))
    else:
        main(sys.argv[1])
