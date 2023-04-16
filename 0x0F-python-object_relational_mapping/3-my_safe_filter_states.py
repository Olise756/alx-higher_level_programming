#!/usr/bin/python3
"""
This script takes in an argument and
shows all values in the states
where `name` equals to the argument
from the database `hbtn_0e_0_usa`.

This script is protected from
MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the there.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        for x in rows:
            print(x)
