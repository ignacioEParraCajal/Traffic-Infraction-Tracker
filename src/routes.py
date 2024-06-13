from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)
from src.models import (
    Person,
    Vehicle,
    Official
)
from src.app import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/register_person', methods=['GET', 'POST'])
def register_person():
    if request.method == 'POST':
        name = request.form['nombre']
        email = request.form['email']
        nueva_persona = Person(name=name, email=email)
        db.session.add(nueva_persona)
        db.session.commit()
        return redirect(url_for('main.show_persons'))
    return render_template('person.html')


@main.route('/show_persons')
def show_persons():
    persons = Person.query.all()
    return render_template('show_person.html', persons=persons)
