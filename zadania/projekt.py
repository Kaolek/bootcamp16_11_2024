from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import tkinter

engine = create_engine("sqlite:///library.db")
Base = declarative_base()



class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates='author')


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship("Author", back_populates='books')



Session = sessionmaker(bind=engine)
session = Session()

new_author = Author(name="Jan Kowalski",)
new_book = Book(title="Jak wygrać wybory?", author=new_author)


new_author2 = Author(name="Jan Nowak")
new_book2 = Book(title="Czy świat zmierza w dobrą stronę?", author=new_author)

new_author3 = Author(name="Jan Brzeziński")
new_book3 = Book(title="Róznice między ludźmi", author=new_author)


new_author4 = Author(name="Jan Stanowski")
new_book4 = Book(title="Co w życiu ma największą wartość", author=new_author)

session.add_all(
    [new_author, new_book]
)
session.add_all(
    [new_author2, new_book2]
)
session.add_all(
    [new_author3, new_book3]
)
session.add_all(
    [new_author4, new_book4]
)

Base.metadata.create_all(engine)
# session.commit()
