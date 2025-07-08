from flask import Flask, render_template

def run_app(app_num, port):
    if app_num == 1:
        app = Flask(__name__, template_folder='templates/app1', static_folder='static/app1')
        @app.route('/')
        def home():
            return render_template('index.html', title='App 1', message='Welcome to App 1!')
    elif app_num == 2:
        app = Flask(__name__, template_folder='templates/app2', static_folder='static/app2')
        @app.route('/')
        def home():
            return render_template('index.html', title='App 2', message='Welcome to App 2!')
    elif app_num == 3:
        app = Flask(__name__, template_folder='templates/app3', static_folder='static/app3')
        @app.route('/')
        def home():
            return render_template('index.html', title='App 3', message='Welcome to App 3!')
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

if __name__ == '__main__':
    import multiprocessing
    processes = []
    for app_num, port in zip([1, 2, 3], [8080, 8081, 8082]):
        p = multiprocessing.Process(target=run_app, args=(app_num, port))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
