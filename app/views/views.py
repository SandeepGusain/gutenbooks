from flask import jsonify, request, Blueprint
from app import db
from sqlalchemy import desc
from app.models.models import Book, Format, BookLanguage, Subject, Bookshelf, Author

mod_book = Blueprint('book', __name__, url_prefix='/books')

Session = db.session

PER_PAGE = 25

FILTERS = {"book_id", "lang", "mime_type", "topic", "author", "title"}

def invalidate_fields(args):
    return set(args)-FILTERS

@mod_book.route("/search/<int:page>", methods=["GET"])
def filter_books(page: int = 1):
    query_params = request.args
    err = invalidate_fields(query_params.keys())

    if query_params and not err:
        books = Session.query(Book).filter().order_by(
            Book.download_count.is_(None),
            desc(Book.download_count)
        )
        count = books.count()
        books = books.paginate(page, PER_PAGE, error_out=False)
        return jsonify({
            "total_count": count,
            "books": [
                book.serialize() for book in books.items
            ]
        }
        )
    return {"message": f"Invalid field present: {err}"}
