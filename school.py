# pylint:disable=C0111,C0103
import sqlite3

def students_from_city(cursor, city):
    """
    Return a list of students from a specific city.

    Parameters:
    - cursor: SQLite database cursor
    - city: name of the city to filter students

    Returns:
    - List of tuples, each tuple represents a student record
    """
    # SQL query to select all students from the given city
    query = "SELECT * FROM students WHERE birth_city = ?"

    # Execute the query safely with parameter substitution
    cursor.execute(query, (city,))

    # Fetch all matching records and return
    return cursor.fetchall()

# ================================
# Test the function locally before running `make`
# ================================
if __name__ == "__main__":
    # Connect to the SQLite database
    conn = sqlite3.connect('data/school.sqlite')
    db = conn.cursor()

    # Test the function with different cities
    print("Students from Paris:")
    print(students_from_city(db, 'Paris'))

    print("\nStudents from London:")
    print(students_from_city(db, 'London'))

    # Close the database connection
    conn.close()
