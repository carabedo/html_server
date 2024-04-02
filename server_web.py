from flask import Flask

from flask import render_template



web_app = Flask('test')


def home():
  return 'Hola mundo! Como estas? Bien?'

web_app.add_url_rule('/', 'home', home,methods=['GET'])


def about():
  return 'Este es mi primer servidor Web!'

web_app.add_url_rule('/about','about',about,methods=['GET'])



def test():
  return render_template('test.html')
web_app.add_url_rule('/test','test',test,methods=['GET'])

def gmail():
  return render_template('gmail.html')
web_app.add_url_rule('/gmail','gmail',gmail,methods=['GET'])

web_app.run(debug=True,host='0.0.0.0',port=5555)
