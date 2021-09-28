from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

  return '<h1><center>If all are congigure correct then it will show this message</center></h1>'

if __name__ == '__main__':

  app.run(host='0.0.0.0', port=5000)