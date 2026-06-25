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
        "Organize more inter-school events",
        "Introduce a transparent feedback system for school facilities",
        "Improve essential facilities"
    ]
    return render_template('index.html', goals=goals)

from flask import Flask, request, render_template, redirect

# ... keep your existing app setup lines here ...

@app.route('/submit-feedback', methods=['POST'])
def handle_feedback():
    # Extract the data from the form
    email = request.form.get('_replyto')
    grade = request.form.get('grade')
    message = request.form.get('message')
    
    # Save it directly into a text file on the server
    with open('feedback.txt', 'a') as f:
        f.write(self_format := f"Grade: {grade} | Email: {email}\nSuggestion: {message}\n{'-'*30}\n")
        
    # Take the student to a simple thank you page or back home
    return "<h3>Thank you! Your feedback has been logged.</h3><a href='/'>Go Back</a>"

@app.route('/secret-campaign-results')
def view_feedback():
    try:
        # Read the file and display it cleanly on the screen
        with open('feedback.txt', 'r') as f:
            content = f.read()
        return f"<h2>Campaign Feedback Stream</h2><pre>{content}</pre>"
    except FileNotFoundError:
        return "<h2>No feedback recorded yet!</h2>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
