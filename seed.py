from models import db, Pet

# class Pet(db.Model):
#     """Pet Class"""
#     __tablename__ = "pets"
#     id = db.Column(db.Integer,
#                    primary_key=True,
#                    autoincrement=True)
#     name = db.Column(db.String,
#                      nullable=False)
#     species = db.Column(db.String,
#                         nullable=False)
#     photo_url = db.Column(db.String)
#     age = db.Column(db.String,
#                     nullable=False)
#     notes = db.Column(db.String)
#     available = db.Column(db.Boolean,
#                           nullable=False,
#                           default=True)

def setup_db():
    "Function for setting up database each time we run app.py"
    # Create all tables
    db.drop_all()
    db.create_all()

    # If table isn't empty, empty it
    Pet.query.delete()

    # Add pets
    pet1 = Pet(name="Sunshine",
               species="cat",
               age="mature",
               available=False)
    pet2 = Pet(name="Woolfy",
               species="dog",
               photo_url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/friendliest-dog-breeds-golden-1578596627.jpg",
               age="puppy",
               available=True)

    # Add new objects to session, so they'll persist
    db.session.add(pet1)
    db.session.add(pet2)

    # Commit--otherwise, this never gets saved!
    db.session.commit()
