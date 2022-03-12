from flask import jsonify, request, Blueprint
from app import db
from sqlalchemy import desc, literal
from app.models.models import Book, BookAuthor, BookLocation, BookSubject, Format, BookLanguage, Language, Subject, Bookshelf, Author

mod_book = Blueprint('book', __name__, url_prefix='/books')

Session = db.session

PER_PAGE = 25

FILTERS = {"book_id", "lang", "mime_type", "topic", "author", "title"}

def validate_fields(args):
    return set(args)-FILTERS

@mod_book.route("/search/<int:page>", methods=["GET"])
@mod_book.route("/search")
def filter_books(page: int = 1):
    query_params = request.args
    err = validate_fields(query_params.keys())

    if query_params and not err:
        books = Session.query(Book)

        if query_params.get("book_id"):
            books = books.filter(Book.id==query_params["book_id"])
        if query_params.get("lang"):
            books = books.join(BookLanguage).join(Language).filter(literal(f"%{query_params['lang']}%").contains(Language.code))
        if query_params.get("mime_type"):
            books = books.join(Format).filter(Format.mime_type==query_params["mime_type"])
        if query_params.get("title"):
            books = books.filter(Book.title.ilike(f"%{query_params['title']}%"))
        if query_params.get("author"):
            books = books.join(BookAuthor).join(Author).filter(Author.name.ilike(f"%{query_params['author']}%"))
        if query_params.get("topic"):
            subject_match = books.join(BookSubject
                                ).join(Subject
                                ).filter(
                                    (Subject.name.ilike(f"%{query_params['topic']}%")))
            books = subject_match.union(
                        books.join(BookLocation
                            ).join(Bookshelf
                            ).filter(
                            (Bookshelf.name.ilike(f"%{query_params['topic']}%"))))
            
        count = books.count()
        books = books.order_by(
                Book.download_count.is_(None),
                desc(Book.download_count)
            ).paginate(page, PER_PAGE, error_out=False)
        return jsonify({
            "total_count": count,
            "books": [
                book.serialize() for book in books.items
            ]
        }
        )
    return {"message": f"Invalid field(s) present: {err}"}
