import psycopg2
from pprint import pprint
import sys

conn = None


class Add:
    def __init__(self) -> object:
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", password="Patriciag2013", dbname="LabelA")
            cur = conn.cursor()
            pprint({"Opened database successfully"})

            cur.execute('SELECT product_name FROM public."Products" limit 1') #TO DO: add products in cart -> Insert products into order_items table

            while True:
                row = cur.fetchone()
                if row is None:
                    break
                pprint("Products: " + row[0])
            #conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
                pprint({"Opened database unsuccessfully" + e})
                sys.exit(1)
        finally:
            if conn:
                conn.close()


class Edit:
    def __init__(self) -> object:
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", password="Patriciag2013", dbname="LabelA")
            cur = conn.cursor()
            pprint({"Opened database successfully"})

            cur.execute('SELECT product_name FROM public."Products" limit 1')  # TO DO: add products in cart -> Update products into order_items table

            while True:
                row = cur.fetchone()
                if row is None:
                    break
                pprint("Products: " + row[0])
            # conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
                pprint({"Opened database unsuccessfully" + e})
                sys.exit(1)
        finally:
            if conn:
                conn.close()
