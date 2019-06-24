import datetime
import sqlite3
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
import pandas as pd
import FinanceDataReader as fdr
from sqlalchemy import create_engine

# SQLite3 --------------------------------------------------------------------#
try:
    with sqlite3.connect("./sqlite.db") as conn:
        start = datetime.datetime(2019, 2, 1)
        end = datetime.datetime(2019, 3, 3)

        gs = fdr.DataReader("090430", start, end)
        print(gs)
        print(gs.index)
        print(gs["Open"])
        print(gs.ix["2019-02-13"])
        print(gs.describe())

        gs["Date"] = gs.index
        gs.index = range(1, (len(gs.index) + 1))
        print(gs)

        # gs.to_sql("TEST", conn, if_exists="fail", index=True, index_label="Id")
        gs.to_sql("TEST", conn, if_exists="replace", index=True, index_label="Id")
        # gs.to_sql("TEST", conn, if_exists="append", index=True, index_label="Id")
        conn.commit()
        df = pd.read_sql(('SELECT * FROM "TEST"'), conn)
        print(df)
        df = pd.read_sql(
            'SELECT * FROM "TEST" WHERE Id=? OR Id=?',
            conn,
            params=(3, 7),
            index_col="Id",
        )
        print(df)
finally:
    print("SQLite3: Dataframe SQL complete!")

# PyMySQL---------------------------------------------------------------------#
# try:
#     engine = create_engine(
#         "mysql+mysqldb://python:" + "1234" + "@localhost/mysql_db", encoding="utf-8"
#     )
#     with engine.connect() as conn:
#         start = datetime.datetime(2019, 5, 4)
#         end = datetime.datetime(2019, 5, 25)

#         gs = fdr.DataReader("034120", start, end)
#         print(gs)
#         print(gs.index)
#         print(gs["Open"])
#         print(gs.ix["2019-05-13"])
#         print(gs.describe())

#         gs["Date"] = gs.index
#         gs.index = range(1, (len(gs.index) + 1))
#         print(gs)

#         # gs.to_sql("test", conn, if_exists="fail", index=True, index_label="Id")
#         gs.to_sql("test", conn, if_exists="replace", index=True, index_label="Id")
#         # gs.to_sql("test", conn, if_exists="append", index=True, index_label="Id")
#         df = pd.read_sql(("select * from TEST"), conn)
#         print(df)
#         df = pd.read_sql(
#             "select * from TEST WHERE Id=%s OR Id=%s",
#             conn,
#             params=(3, 7),
#             index_col="Id",
#         )
#         print(df)
# finally:
#     engine.dispose()
#     print("MySQL: Dataframe SQL complete!")
