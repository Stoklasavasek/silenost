from faker import Faker
from models import db, Person
from app import app

# Inicializace Fakeru
fake = Faker()

with app.app_context():
    # Kolik záznamů chcete vytvořit
    number_of_records = 20

    # Přidání záznamů do databáze
    for _ in range(number_of_records):
        fake_person = Person(
            name=fake.name(),
            age=fake.random_int(min=18, max=80)  # Věk v rozmezí 18–80 let
        )
        db.session.add(fake_person)
    
    # Uložení změn
    db.session.commit()
    print(f"{number_of_records} záznamů bylo úspěšně přidáno!")
