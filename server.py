from flask import Flask

app = Flask(__name__)

@app.route('/testing', methods=['GET', 'POST'])
def testing():
  return 'Hello'

app.run(host='0.0.0.0', debug=True)