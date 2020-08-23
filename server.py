from flask import Flask
import requests

app = Flask(__name__)

@app.route('/testing', methods=['GET', 'POST'])
def testing():
  # Joke endpoint
  req = requests.get('https://official-joke-api.appspot.com/jokes/programming/random')
  data = req.json() 
  setup = data[0]['setup']
  punchline = data[0]['punchline']
  # Cute cat pic endpoint
  cat_req = requests.get('https://aws.random.cat/meow')
  img_data = cat_req.json()
  img_url = img_data['file']
  # Return 3 msgs: the setup, the punchline, then a random cat img
  return "<Response><Message>{s}</Message><Message>{p}</Message><Message><Media>{u}</Media></Message></Response>".format(s = setup, p = punchline, u = img_url)

app.run(host='0.0.0.0', debug=True)