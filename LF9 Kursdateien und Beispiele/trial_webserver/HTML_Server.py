from flask import Flask, render_template
import requests

# initialisiere Flask-Server
app = Flask(__name__)

# definiere Route für Hauptseite
@app.route('/')
def index():
 # gebe Antwort an aufrufenden Client zurück
 return render_template('Index.html')

@app.route('/eingaenge')
def eingaenge():
   return render_template('eingaenge.html')

@app.route('/ausgaenge')
def ausgaenge():
   return render_template('ausgaenge.html')

@app.route('/get', methods=['GET'])
def get_example():
   param1 = requests.args.get('param1')
   param2 = requests.args.get('param2')
   param3 = requests.args.get('param3')
   return f'GET request: Param1={param1}, Param2={param2}, Param3={param3}'

@app.route('/post', methods=['POST'])
def post_example():
   param1 = requests.args.get('param1')
   param2 = requests.args.get('param2')
   param3 = requests.args.get('param3')
   return f'POST request: Param1={param1}, Param2={param2}, Param3={param3}'

if __name__ == '__main__':
 # starte Flask-Server
    app.run(host='0.0.0.0', port=5000)