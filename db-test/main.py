from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
sqldbname = 'db-test/db/website.db'

@app.route('/')
def index():
    conn = sqlite3.connect(sqldbname)

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM storages')
    
    data = cursor.fetchall()

    conn.close()

    return render_template('index.html', table=data)

@app.route('/searchData', methods=['GET','POST'])
def load_data_from_db(search_text):
    sqldbname = 'db-test/db/website.db'
    if search_text != "":
        conn = sqlite3.connect(sqldbname)
        cursor = conn.cursor()
        
        sqlcommand = ("SELECT * FROM storages "
            "WHERE model LIKE '%") + search_text + "%'"
        
        cursor.execute(sqlcommand)
        data = cursor.fetchall()

        conn.close()
        
        return data

def searchData():
    search_text = request.form['searchInput']
    html_table = load_data_from_db(search_text)
    
    print(html_table)
    
    return render_template('SearchWithCSSDataDB.html', search_text=search_text, table=html_table)

if __name__ == '__main__':
    app.run(debug=True)