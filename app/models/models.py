from app import db


class Author(db.Model):
    __tablename__ = 'books_author'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)


class Book(db.Model):
    __tablename__ = 'books_book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    media_type = db.Column(db.String)
    gutenberg_id = db.Column(db.Integer)
    download_count = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'media_type': self.media_type,
            'download_count': self.download_count
        }


class BookAuthor(db.Model):
    __tablename__ = 'books_book_authors'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(
        'books_author.id'), nullable=False)


    def serialize(self):
        return {
            'author_id': self.author_id
        }


class BookLocation(db.Model):
    __tablename__ = 'books_book_bookshelves'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    bookshelf_id = db.Column(db.Integer, db.ForeignKey(
        'books_bookshelf.id'), nullable=False)

    def serialize(self):
        return {
            "bookshelf_id": self.bookshelf_id
        }


class BookLanguage(db.Model):
    __tablename__ = 'books_book_languages'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey(
        'books_language.id'), nullable=False)

    def serialize(self):
        return {
            "language_id": self.language_id
        }


class BookSubject(db.Model):
    __tablename__ = 'books_book_subjects'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey(
        'books_subject.id'), nullable=False)


    def serialize(self):
        return {
            "subject_id": self.subject_id
        }


class Bookshelf(db.Model):
    __tablename__ = 'books_bookshelf'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Format(db.Model):
    __tablename__ = 'books_format'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books_book.id'), nullable=False)
    mime_type = db.Column(db.String)
    url = db.Column(db.String)


class Language(db.Model):
    __tablename__ = 'books_language'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)

    def serialize(self):
        return {
            'lang': self.code
        }


class Subject(db.Model):
    __tablename__ = 'books_subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
