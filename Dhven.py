from flask import Flask, render_template

app = Flask(__name__)

@app.url_value_preprocessor
def pull_lang_code(endpoint, values):
    pass

@app.route('/')
def index():
    # You can pass your manifesto points or goals here
    goals = [
        "Improve student-teacher communication",
        "Organize more inter-school tech and sports events",
        "Introduce a transparent feedback system for school facilities"
    ]
    return render_template('index.html', goals=goals)

if __name__ == '__main__':
    app.run(debug=True, port=5005, use_reloader=False)