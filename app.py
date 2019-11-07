from flask import Flask, render_template, url_for, request
import markovify


app = Flask(__name__)

with open('static/datasets/texas-last-statement.txt') as f:
    text = f.read()

text_model = markovify.NewlineText(text, state_size=2)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        for i in range(1):
            statement = text_model.make_short_sentence(500)
        return render_template('index.html', statement=statement)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
