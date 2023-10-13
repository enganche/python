from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'hihihaha'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        password = session['password']

    else:
        username = 'User'
        password = 'none'
        
    lst = [
        "We live",
        "We love",
        "We lie"
    ]
    return render_template("index.html", username=username, password=password, seq=lst);

@app.route('/data')
def loadData():
    import pandas as pd 
    df = pd.read_csv('data.csv')

    html_table = df.iloc[:20].to_html(classes='data', escape=False)

    return html_table

def data():
    html_table = loadData()

    return render_template(
        'page_data.csv',
        tables=html_table,
        titles=html_table.columns.values
        )

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_text = request.form['searchInput']

    return render_template("search.html", search_text=search_text)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username

        password = request.form['password']
        session['password'] = password

        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    username_error = ""
    password_error = ""

    if not username:
        username = "Username is required"
    if not password:
        password = "Password is required"

    if username_error or password_error:
        return render_template('registration.html', username_error=username_error, password_error=password_error, registration_success="")

    print(f'Registered: Username: {username}, Password: {password}')
    registration_success = "Registration Successful!"

    return render_template('registration.html', username_error=username_error, password_error=password_error, registration_success=registration_success)

app.run(host='0.0.0.0', port=5000)