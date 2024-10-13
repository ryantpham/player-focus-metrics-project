import sqlite3
import csv

def setup_database():
    # Connect to a new SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect('./data/trace_data.db')
    cursor = conn.cursor()

    # Create a table to hold the data
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subscriptions (
        Rando REAL,
        subitem_id TEXT,
        subid TEXT,
        created TEXT,
        sub_date TEXT,
        plan__nickname TEXT,
        plan__id TEXT,
        quantity INTEGER,
        status TEXT,
        plan__active BOOLEAN,
        plan__amount INTEGER,
        interval TEXT,
        cus_id TEXT,
        divs_division_id REAL,
        type TEXT,
        creation_time TEXT,
        tp_user_id INTEGER,
        ur_user_id REAL,
        u_user_id INTEGER,
        stripe_subscription_type TEXT,
        address__state TEXT,
        address__city TEXT
    )
    ''')

    # Read the CSV file and insert data into the table
    with open('./data/SQL_Redshift_Project_Data_Trace_Ryan.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            cursor.execute('INSERT INTO subscriptions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup complete.")