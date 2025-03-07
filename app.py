from flask import Flask, render_template, request, jsonify
from google_sheets import save_review

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.json
    name = data.get("name")
    specialist = data.get("specialist")
    city = data.get("city")
    rating = data.get("rating")
    review = data.get("review")

    if not name or not review:
        return jsonify({"error": "Имя и отзыв обязательны"}), 400

    try:
        save_review(name, specialist, city, rating, review)
        return jsonify({"message": "Отзыв успешно сохранён!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
