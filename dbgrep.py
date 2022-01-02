import sys
import sqlite3

def get_match(db_path, word):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    schema = cursor.fetchall()
    for table in schema:
        cursor.execute("SELECT * FROM "+str(table[0])+ " ;")
        table_content = cursor.fetchall()
        for row in table_content:
            if word in str(row):
                print (table[0], row) 
    con.close()

def print_help():
    print ("Usage: dbgrep.py [text to search] [database path]")
    print ("Use quotes to join text or path containing spaces")
    print ("········· Example ·········")
    print ("python dbgrep.py hi my.db")    

def main(argv):
    if len(sys.argv) != 3:
        print_help()
        sys.exit()

    text_to_search = sys.argv[1]
    db_path = sys.argv[2]
    get_match(db_path, text_to_search)


if __name__ == "__main__":
    main(sys.argv)
