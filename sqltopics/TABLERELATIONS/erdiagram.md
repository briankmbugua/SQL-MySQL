# ER Diagram
ER Diagram stand for Entity Relationship Diagram, also known as ERD is a diagram that displays the relationship of entity sets stored in a database.

ER diagrams are created based on three basic concepts:

# Entities.
- entities: Real-world objects or things your database stores information about.They represent the core data types you want to keep track of. For example in a library database entities could be books, authors, members, and loans.Each entity is unique and has its own distinct identity.
- entity set: An entity set is a group of similar kind of entities.
- Weak Entities - A weak entity is a type of entity which doesn't have its key attribute.It can be identified uniquely by considering the primary key of another entity.For that, weak entity sets need to have participation.

## Strong Entity Set
- has a unique identifier(primary key) for each member.
- Represented by a single rectangel.
- Key attributes are underlined
- Members are called "dominant entities"
## Weak Entity set
- Lacks sufficient attributes for a primary key.
- Relies on the strong entity set for identification.
- Represented by a double rectangle
- key attributes have dashed underlines
- Members are called "subordinate entities."
## Relationships
- Strong-Strong: Diamond symbol connects two strong sets
- Strong-Weak: Double diamond symbol connects are strong set to a weak set.
- Connecting Lines: Strong entity set uses single lines, while weak enitity set uses double lines for identifying relationships.

# Atrributes
- attributes: Define the characteristics or properties that describe each entity.Attributes for a book might include title, author, publication year, genre etc.
## Simple Attribute
Most fundamental building block of data.It's an indivisible piece of information, like a student's contact number.It can't be broken down any further.Also called an "atomic values" e.g Student ID, book title, product price.
## Composite Atrribute
Can be split into smaller, meaningful parts.E.g students fullname is a composite attribute comprising first name, middle name and last name.
Address(street, city, country), date(day, month, year)




- relationships: Depict how different entities are connected to each other.They show ho information flows between them.E.g a book can be written by an author(one-to-many).A member can borrow multiple books(many-to-many relationship)


