import csv
import pymysql

# Connect to the database
db = pymysql.connect(host='localhost', user='UNAME', password='PASSWORD', database='DB_NAME')
cursor = db.cursor()

# Insert movies from CSV into the database
def insert_movies_from_csv():
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            insert_movie(row['name'], row['time'])

# Insert movies into the database
def insert_movie(name, time):
    try:
        query = "INSERT INTO movies (name, time) VALUES (%s, %s)"
        cursor.execute(query, (name, time))
        db.commit()
        print(f"Movie '{name}' loaded successfully!")
    except Exception as e:
        db.rollback()
        print("Error:", e)

if __name__ == "__main__":
    insert_movies_from_csv()
    db.close()
