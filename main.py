from flask import Flask
import random
app = Flask(__name__)

facts_list = ["Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.",
            "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
            "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.",
            "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время."]
@app.route("/")
def index():
    return f'<h1>Привет! Здесь ты можешь узнать пару интересных фактов о технологических зависимостях!</h1><a href="/random_fact">Посмотреть случайный факт!</a>'
@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)