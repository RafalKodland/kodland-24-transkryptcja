#Import
from flask import Flask, render_template,request, redirect
#Podłączenie biblioteki bazy danych
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Podłączanie SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Tworzenie bazy danych 
db = SQLAlchemy(app)
#Tworzenie tabeli

#Zadanie nr 1. Utwórz bazę danych
class Card(db.Model):
    #Tworzenie pól kolumn
    #id
    id = db.Column(db.Integer, primary_key=True)
    #Tytuł
    title = db.Column(db.String(100), nullable=False)
    #Opis
    subtitle = db.Column(db.String(300), nullable=False)
    #Tekst
    text = db.Column(db.Text, nullable=False)

    #Wyprowadzanie obiektu i jego
    def __repr__(self):
        return f'<Card {self.id}>'


#Uruchomienie strony z zawartością
@app.route('/')
def index():
    #Wyprowadzanie obiektów z bazy danych
    #Zadanie #2. Zrób to tak, aby obiekty DB były pokazane w pliku Index.html
    cards = Card.query.order_by(Card.id).all()

    return render_template('index.html', cards=cards)

#Uruchomienie strony z kartą
@app.route('/card/<int:id>')
def card(id):
    #Zadanie #2. Użyj identyfikatora, aby wyświetlić właściwą kartę
    card = Card.query.get(id)

    return render_template('card.html', card=card)

#Uruchomienie strony z inicjalizacją karty
@app.route('/create')
def create():
    return render_template('create_card.html')

#Formularz karty
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        #Tworzenie obiektu do przekazania do bazy danych

        #Zadanie #2. Stwórz sposób przechowywania danych w bazie danych
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)