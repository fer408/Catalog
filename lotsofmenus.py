from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import ItemType, Base, MenuItem, User

engine = create_engine('sqlite:///item.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='static/puppy.jpg')
session.add(User1)
session.commit()


# Menu for Dog Toys
item_type1 = ItemType(user_id=1,name="Dog Toys")

session.add(item_type1)
session.commit()



menuItem1 = MenuItem(user_id=1,name="Green chew toy", description="A green chew toy",
                     price="$7.50", type="Item", item=item_type1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1,name="Red Chew Toy", description="A red chewtoy for your best friend to play with",
                     price="$7.50", type="Item",  item=item_type1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,name="Blue Chew Toys", description="A blue chew toy",
                     price="$7.50", type="Item", item=item_type1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,name="Snake Toy", description="A plastic snake toy for your dog to play with",
                     price="$7.99", type="Item", item=item_type1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,name="Rat Toy", description="A plastic Rat toy for your dog",
                     price="$4.99", type="Item", item=item_type1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1,name="Black Chew Toy", description="A black chew toy",
                     price="$5.99", type="Item", item=item_type1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1,name="Big Hard Doggie Ball", description="A big hard ball for your dog to chew",
                     price="$10.49", type="Item", item=item_type1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1,name="Spider Toy", description="A plastic spider for your dog to play with",
                     price="$5.99", type="Item", item=item_type1)

session.add(menuItem8)
session.commit()


# Menu for Leashes
item_type2 = ItemType(user_id=1,name="Leashes")

session.add(item_type2)
session.commit()

menuItem1 = MenuItem(user_id=1,name="Green Leash", description="A green leash",
                     price="$17.50", type="Item", item=item_type2)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1,name="Red Leash", description="A red leash",
                     price="$17.50", type="Item", item=item_type2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,name="Blue Leash", description="A blue leash",
                     price="$17.50", type="Item", item=item_type2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,name="Black Leash", description="A black leash",
                     price="$7.99", type="Item", item=item_type2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,name="Iron Chain Leash", description="An iron chain leash",
                     price="$15.99", type="Item", item=item_type2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1,name="Deluxe Leash", description="A deluxe leash that gives move freedom of movement to your dog.",
                     price="$19.99", type="Item", item=item_type2)

session.add(menuItem6)
session.commit()


# Menu for Dog Treats and Food
item_type3 = ItemType(user_id=1,name="Dog Treats and Food")

session.add(item_type3)
session.commit()

menuItem1 = MenuItem(user_id=1,name="Scooby Snacks", description="Scoobie snacks for your dog",
                     price="$10.50", type="Item", item=item_type3)
session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1,name=" Big Bone", description="A chewy bone treat for your best bud.",
                     price="$7.00", type="Item", item=item_type3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,name="Bacon Treats", description="Bacony goodness for your dog",
                     price="$15.00", type="Item", item=item_type3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,name="Dog Food 5kg ", description="5 kilos of dog food",
                     price="$7.99", type="Item", item=item_type3)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,name="Dog Food 10kg", description="10 kilos of dog food",
                     price="$9.99", type="Item", item=item_type3)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1,name="Dog Food 15kg", description="15 kilos of dog food",
                     price="$12.99", type="Item", item=item_type3)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1,name="Dog Food 20kg", description="20 kilos of dog food",
                     price="$14.49", type="Item", item=item_type3)

session.add(menuItem7)
session.commit()

# Menu for Collars
item_type4 = ItemType(user_id=1,name="Dog Collars")

session.add(item_type4)
session.commit()

menuItem1 = MenuItem(user_id=1,name="Red Collar", description="A red collar",
                     price="$10.50", type="Item", item=item_type4)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1,name=" Green Collar", description="A green collar",
                     price="$10.00", type="Item", item=item_type4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,name="Black Collar", description="A black collar",
                     price="$10.00", type="Item", item=item_type4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,name="Silver Collar ", description="A silver collar",
                     price="$7.99", type="Item", item=item_type4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,name="Delux Collar", description="A fancy delux collar with diamonds encrusted",
                     price="$19.99", type="Item", item=item_type4)

session.add(menuItem5)
session.commit()

# Menu for Dog Treats and Food
item_type5 = ItemType(user_id=1,name="Dog Harness")

session.add(item_type5)
session.commit()

menuItem1 = MenuItem(user_id=1,name="Red Harness", description="A red Harness",
                     price="$10.50", type="Item", item=item_type5)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1,name=" Green Harness", description="A green Harness",
                     price="$10.00", type="Item", item=item_type5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,name="Black Harness", description="A black harness",
                     price="$10.00", type="Item", item=item_type5)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,name="Silver Harness", description="A silver harness",
                     price="$7.99", type="Item", item=item_type5)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,name="Delux Harness", description="A fancy delux collar with diamonds encrusted",
                     price="$29.99", type="Item", item=item_type5)

session.add(menuItem5)
session.commit()


print "added menu items!"