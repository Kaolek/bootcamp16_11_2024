from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///:parents_database.db', echo=True)
Base = declarative_base()


# 1:n - jeden do wielu
class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))  # maksymalna długość tekstu
    children = relationship("Child", backref='parent')  # backref - doda pole parent w klasie Child automatycznie
    # przy back_populates musieliśmy w klasie Child samodzielnie zdefiniować to pole z relacją


class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parents.id'))

    def __repr__(self):
        return f"id={self.id}, name={self.name}"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

parent = Parent(name="Rodzic")
child1 = Child(name="Dziecko 1", parent=parent)
child2 = Child(name="Dziecko 2", parent=parent)

session.add(parent)
session.add(child1)
session.add(child2)
# session.add_all(
#     [parent, child1, child2]
# )
session.commit()

our_parent = session.query(Parent).all()
print(our_parent)

our_parent_filtered = session.query(Parent).filter_by(name="Rodzic").first()
print(f"Rodzic: {our_parent_filtered.name}")
children = our_parent_filtered.children
for child in children:
    print(f"Dziecko: {child.name}")
    print(f"Dziecko: {child.parent.name}")