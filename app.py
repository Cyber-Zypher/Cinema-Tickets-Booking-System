import pymysql

# Connect to the database
db = pymysql.connect(host='localhost', user='UNAME', password='PASSWORD', database='DB_NAME')
cursor = db.cursor()

# User registration
def register_user(username, password):
    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        db.commit()
        print("User registered successfully!")
    except Exception as e:
        db.rollback()
        print("Error:", e)

# User login
def login(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    return user

# Movie selection
def list_movies():
    query = "SELECT * FROM movies"
    cursor.execute(query)
    movies = cursor.fetchall()
    return movies

# Seat reservation
def reserve_seat(movie_id, user_id, seat_number):
    try:
        query = "INSERT INTO reservations (movie_id, user_id, seat_number) VALUES (%s, %s, %s)"
        cursor.execute(query, (movie_id, user_id, seat_number))
        db.commit()
        print("Seat reserved successfully!")
    except Exception as e:
        db.rollback()
        print("Error:", e)

def fetch_reserved_seats(user_id):
    try:
        query = "SELECT movies.name, reservations.seat_number FROM reservations JOIN movies ON reservations.movie_id = movies.id WHERE reservations.user_id = %s"
        cursor.execute(query, (user_id,))
        reserved_seats = cursor.fetchall()
        return reserved_seats
    except Exception as e:
        print("Error:", e)
        return []

# Main function
def main():
    user = None  # Initialize user as None
    
    while True:
        print("1. Register\n2. Login\n3. List Movies\n4. Reserve Seat\n5. Exit\n6. My Reservations.")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login(username, password)  # Assign user if login is successful
            if user:
                print("Login successful!")
            else:
                print("Login failed!")
        elif choice == 3:
            movies = list_movies()
            for movie in movies:
                print(f"ID: {movie[0]}, Name: {movie[1]}, Time: {movie[2]}")
        elif choice == 4:
            if user:
                movie_id = int(input("Enter movie ID: "))
                seat_number = int(input("Enter seat number: "))
                user_id = user[0]  # Use the logged-in user's ID
                reserve_seat(movie_id, user_id, seat_number)
            else:
                print("Please log in first.")
        elif choice == 5:
            break
        elif choice == 6:
            if user:
                user_id = user[0]
                reserved_seats = fetch_reserved_seats(user_id)
                if reserved_seats:
                    print("Your reserved seats:")
                    for movie_name, seat_number in reserved_seats:
                        print(f"Movie: {movie_name}, Seat: {seat_number}")
                else:
                    print("You have no reserved seats.")
            else:
                print("Please log in first.")
        else:
            print("Invalid choice. Please try again.")

    db.close()

if __name__ == "__main__":
    main()