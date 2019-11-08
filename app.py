from flask import Flask
# from textblob import TextBlob


app = Flask(__name__)

@app.route('/index')
def index():
    return app.make_response("This is wonderfull !")

# @app.route('/<message>')
# def index(message):

#     sentiment="positive"

#     # if (TextBlob(message).sentiment.polarity < 0.0):
#     #     sentiment="negative"

#     return app.make_response(sentiment)
