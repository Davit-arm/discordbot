from flask import Flask
import random
import string

app = Flask(__name__)


facts_list = ['''Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс,
               когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.''',
               '''Согласно исследованию, проведенному в 2018 году,
                 более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.''','''Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того,
                   как они вышли с работы.''']

coin = ['orel','reshka']
def generate_password(length):
    elements = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(elements) for _ in range(length))
    return password


@app.route("/")
def hello_world():
    return '''<h1>Hello, World!</h1>
    <a href="/random">Посмотреть случайный факт!</a>
    <p><a href ="/coin">Monetka</a></p>'''
    
@app.route("/random")
def fact():
    return f'''<p>{random.choice(facts_list)}</p>'''

#@app.route("/parol")
#def parol():
    #return f'''<p>{generate_password(length)}</p>'''

@app.route("/coin")
def fcoin():
    return f'''<p>{random.choice(coin)}</p>'''

app.run(debug=True)


