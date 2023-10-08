
from faker import Faker
from app import app
from models import db, City

def seed_data():
    fake = Faker()
    with app.app_context():
        
        for _ in range(10):
            city = City(
                name=fake.city(),
                date_of_visit=fake.date_this_decade(),
                best_memories=fake.text(),
                accommodation=fake.company()
            )
            db.session.add(city)

        
        db.session.commit()

        print("Data seeding completed.")

if __name__ == '__main__':
    print("Starting seed...")
    seed_data()

        
