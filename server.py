from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/testing', methods=['GET', 'POST'])
def testing():
  # Joke endpoint
  text = request.values['Body']
  print(text)
  if text in ["CAT", "DOG"]:
    req = requests.get('https://official-joke-api.appspot.com/jokes/programming/random')
    data = req.json() 
    setup = data[0]['setup']
    punchline = data[0]['punchline']

    # Cute cat pic endpoint
    if text == "CAT":
      cat_req = requests.get('https://aws.random.cat/meow')
      img_data = cat_req.json()
      img_url = img_data['file']

    elif text == "DOG":
      dog_req = requests.get('https://dog.ceo/api/breeds/image/random')
      img_data = dog_req.json()
      img_url = img_data['message']

    # Return 3 msgs: the setup, the punchline, then a random cat img
    return "<Response><Message>{s}</Message><Message>{p}</Message><Message><Media>{u}</Media></Message></Response>".format(s = setup, p = punchline, u = img_url)
  
  else:
    message = "Are you having a ruff day? Do you need some paw-sitivity? Text DOG or CAT to put a purr-fect smile on your face!"
    return "<Response><Message>{m}</Message></Response>".format(m = message)

app.run(host='0.0.0.0', debug=True)