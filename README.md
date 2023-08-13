
# Cinema Tickets Reservation System
A Simple Movie tickets reservation system made with Python and MySQL Database.
The Code uses PyMySQL Python Library to function. This code has a very simple syntax which makes it easy to understand and beginner friendly.


## Install the required Libraries.

Clone the project

```
pip install pymysql
```
or
```
python -m pip install pymysql
```

## Initialize the Database

```
-- Table for movies
CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    time VARCHAR(100) NOT NULL
);

-- Table for users
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Table for reservations
CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    user_id INT,
    seat_number INT,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

```

## Instructions

- After installing the needed libraries. Edit the `data.csv` file to load the questions and its answers.

- Then, run the `load_data.py` script to load the questions and answers to the SQL database.

- Don't run the `load_data.py` more than once, It will cause duplicate questions and cause clutter on your database.

- Then Finally, run the `app.py` to play the quiz.

## Authors

- [@sidharth_everett](https://github.com/Cyber-Zypher)
- [@sindhu_vaibhav_KL](https://www.instagram.com/sindhuvaibhav2007/)
- [And our friends @Medusa Infosystems International](https://www.instagram.com/themedusaclan_official/)
