from app import app, db
from app.models import Barista, Cafe


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Barista': Barista, 'Cafe': Cafe}
