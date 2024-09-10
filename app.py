import random
from flask import Flask, render_template, jsonify, request
from scraper import Scraper

app = Flask(__name__)

# Route to render the main HTML page
@app.route('/')
def scoreboard():
    return render_template('scoreboard.html')

# Route to update the score dynamically
@app.route('/update_score')
def update_score():
    url = request.args.get('url')  # Get the URL from the input field
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    scraper = Scraper(url)
    scraper.fetch_content()
    scraper.get_first_innings_score()
    scraper.get_second_innings_score()

    score_data = {
        "target_score": scraper.target_score,
        "current_score": scraper.current_score,
        "overs": scraper.overs,
        "wickets": scraper.wickets
    }   

    return jsonify(score_data)

if __name__ == "__main__":
    app.run(debug=True)
