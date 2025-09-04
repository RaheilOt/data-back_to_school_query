# pylint:disable=C0111,C0103
# pylint:disable=C0111,C0103
import sqlite3

def students_from_city(db, city):
    """Return a list of students from a specific city"""
    query = "SELECT * FROM students WHERE birth_city = ?"
    db.execute(query, (city,))
    return db.fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect('data/school.sqlite')
    db = conn.cursor()
    # Test with different cities
    print("Students from Paris:")
    print(students_from_city(db, 'Paris'))
    
    print("\nStudents from London:")
    print(students_from_city(db, 'London'))
    conn.close()
