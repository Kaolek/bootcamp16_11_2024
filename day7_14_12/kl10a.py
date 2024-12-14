class PrintMedia:
    def print_media(self):
        print("Drukowana treść")


class DigitalMedia:
    def digital_media(self):
        print("Cyfrowa treść")


class Book(PrintMedia):
    pass


class Ebook(DigitalMedia):
    pass


class MultimediaBook(Book, Ebook):
    pass


multimedia_book = MultimediaBook()
print(MultimediaBook.__mro__)

multimedia_book.print_media()
multimedia_book.digital_media()