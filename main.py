from flask import Flask, render_template, request

from hh_json import parse

# объявление главной переменной
app = Flask(__name__)


# вывод (редеринг) главной страницы
@app.get('/index')
@app.get('/')
def index():
    return render_template('index.html')


# вывод страницы формы
@app.route('/form/')
def form():
    return render_template('form.html')


@app.post('/result/')
def result():
    vac = request.form
    data = parse(**vac)
    dat = {**data, **vac}
    print(dat)
    return render_template('about.html', res=dat)