#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """

if __name__ == '__main__':
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()

    cur.execute("""SELECT cities.name
    FROM cities LEFT JOIN states ON cities.state_id=states.id
    WHERE states.name LIKE %s ORDER BY cities.id ASC""", [format(sys.argv[4])])

    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    conn.close()
