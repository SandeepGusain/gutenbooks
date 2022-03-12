from app import db


class Author(db.Model):
    __tablename__ = 'books_author'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)

    def serialize(self):
        return {
            'name': self.name
        }

class Book(db.Model):
    __tablename__ = 'books_book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    media_type = db.Column(db.String)
    gutenberg_id = db.Column(db.Integer)
    download_count = db.Column(db.Integer)
    author = db.relationship("BookAuthor", backref="books_book")
    bookshelf = db.relationship("BookLocation", backref="books_book")
    language = db.relationship("BookLanguage", backref="books_book")
    subject = db.relationship("BookSubject", backref="books_book")
    links = db.relationship("Format", backref="books_book")

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'download_count': self.download_count,
            'author': [author.serialize() for author in self.author],
            'bookshelf(s)': [location.serialize() for location in self.bookshelf],
            'language': [lang.serialize() for lang in self.language],
            'subject(s)': [topic.serialize() for topic in self.subject],
            'url(s)': [url.serialize()  for url in self.links]
        }


class BookAuthor(db.Model):
    __tablename__ = 'books_book_authors'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(
        'books_author.id'), nullable=False)
    author = db.relationship("Author", backref="books_book_authors")

    def serialize(self):
        return self.author.serialize()


class BookLocation(db.Model):
    __tablename__ = 'books_book_bookshelves'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    bookshelf_id = db.Column(db.Integer, db.ForeignKey(
        'books_bookshelf.id'), nullable=False)
    bookshelf = db.relationship("Bookshelf", backref="books_book_bookshelves")

    def serialize(self):
        return self.bookshelf.serialize()

class BookLanguage(db.Model):
    __tablename__ = 'books_book_languages'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey(
        'books_language.id'), nullable=False)
    language = db.relationship("Language", backref="books_book_languages")

    def serialize(self):
        return self.language.serialize()


class BookSubject(db.Model):
    __tablename__ = 'books_book_subjects'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey(
        'books_subject.id'), nullable=False)
    subject = db.relationship("Subject", backref="books_book_subjects")

    def serialize(self):
        return self.subject.serialize()


class Bookshelf(db.Model):
    __tablename__ = 'books_bookshelf'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def serialize(self):
        return self.name


class Format(db.Model):
    __tablename__ = 'books_format'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    mime_type = db.Column(db.String)
    url = db.Column(db.String)

    def serialize(self):
        return self.url

class Language(db.Model):
    __tablename__ = 'books_language'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)

    def serialize(self):
        return self.code


class Subject(db.Model):
    __tablename__ = 'books_subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def serialize(self):
        return self.name