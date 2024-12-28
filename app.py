from flask import Flask, render_template

app = Flask(__name__)

# List of anime quotes
anime_quotes = [
    {
        "name": "Naruto Uzumaki",
        "quote": "I'm not gonna run away, I never go back on my word! That's my nindo, my ninja way!",
        "image": "/static/images/naruto.jpg"
    },
    {
        "name": "Monkey D. Luffy",
        "quote": "If you don’t take risks, you can’t create a future!",
        "image": "/static/images/luffy.jpg"
    },
    {
        "name": "Levi Ackerman",
        "quote": "The only thing we're allowed to do is to believe that we won't regret the choice we made.",
        "image": "/static/images/levi.jpg"
    },
    {
        "name": "Goku",
        "quote": "Power comes in response to a need, not a desire. You have to create that need.",
        "image": "/static/images/goku.jpg"
    }
]

@app.route('/')
def home():
    return render_template('index.html', quotes=anime_quotes)

@app.route('/quote/<int:quote_id>')
def quote_page(quote_id):
    quote = anime_quotes[quote_id]
    return render_template('quote.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
