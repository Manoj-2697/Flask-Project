from flask import Flask, render_template

app1 = Flask(__name__, template_folder='templates/app1', static_folder='static/app1')
app2 = Flask(__name__, template_folder='templates/app2', static_folder='static/app2')
app3 = Flask(__name__, template_folder='templates/app3', static_folder='static/app3')

@app1.route('/')
def home1():
    return render_template('index.html', title='App 1', message='Welcome to App 1!')

@app2.route('/')
def home2():
    return render_template('index.html', title='App 2', message='Welcome to App 2!')

@app3.route('/')
def home3():
    return render_template('index.html', title='App 3', message='Welcome to App 3!')

if __name__ == '__main__':
    import threading
    def run_app(app, port):
        app.run(host='0.0.0.0', port=port)
    threading.Thread(target=run_app, args=(app1, 8080)).start()
    threading.Thread(target=run_app, args=(app2, 8081)).start()
    threading.Thread(target=run_app, args=(app3, 8082)).start()
