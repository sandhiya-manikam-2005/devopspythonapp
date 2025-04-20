from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'quiz_secret_key'  # Needed for session management

questions = [
    {
        'question': "What is the capital of France?",
        'options': ['Paris', 'Rome', 'Berlin', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': "Who wrote 'Hamlet'?",
        'options': ['Charles Dickens', 'William Shakespeare', 'Leo Tolstoy', 'Jane Austen'],
        'answer': 'William Shakespeare'
    },
    {
        'question': "What is the largest planet in our solar system?",
        'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Jupiter'
    },
    {
        'question': "What does CPU stand for?",
        'options': ['Central Processing Unit', 'Computer Processing Unit', 'Central Power Unit', 'Control Program Unit'],
        'answer': 'Central Processing Unit'
    },
    {
        'question': "Which element has the chemical symbol 'O'?",
        'options': ['Gold', 'Oxygen', 'Osmium', 'Oxide'],
        'answer': 'Oxygen'
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ['Venus', 'Jupiter', 'Mars', 'Neptune'],
        'answer': 'Mars'
    },
    {
        'question': "In which year did the World War II end?",
        'options': ['1945', '1939', '1918', '1965'],
        'answer': '1945'
    },
    {
        'question': "What is the boiling point of water at sea level in Celsius?",
        'options': ['90°C', '100°C', '110°C', '120°C'],
        'answer': '100°C'
    },
    {
        'question': "Which company developed the Python programming language?",
        'options': ['Google', 'Microsoft', 'Python Software Foundation', 'None of these'],
        'answer': 'None of these'
    },
    {
        'question': "Which gas do plants absorb from the atmosphere?",
        'options': ['Oxygen', 'Nitrogen', 'Carbon Dioxide', 'Hydrogen'],
        'answer': 'Carbon Dioxide'
    }
]

@app.route('/', methods=['GET', 'POST'])
def quiz():
    result = ''

    # Load question from session or pick a new one
    if 'current_question' not in session:
        session['current_question'] = random.choice(questions)

    q = session['current_question']

    if request.method == 'POST':
        selected = request.form.get('option')
        correct = q['answer']
        if selected == correct:
            result = '✅ Correct! 🎉'
            session.pop('current_question', None)  # Clear current to show next
            return render_template('quiz.html', question=None, result=result)  # Show message + Next button
        else:
            result = f'❌ Wrong! The correct answer was: <b>{correct}</b>. Try again.'

    return render_template('quiz.html', question=q, result=result)

@app.route('/next')
def next_question():
    session['current_question'] = random.choice(questions)
    return redirect(url_for('quiz'))

if __name__ == '__main__':
    app.run(debug=True)
