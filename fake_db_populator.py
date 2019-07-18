from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user1 = User(
    name='vivin',
    email='vivin-christopher.h-s@capgemini.com'
)

session.add(user1)
session.commit()

category1 = Category(
    name='Snowboarding',
    user=user1
)

session.add(category1)
session.commit()

item1 = Item(
    name='Snowboard',
    description='It is exciting snowboard!',
    category=category1,
    user=user1
)

session.add(item1)
session.commit()

print('Finished populating the database!')
