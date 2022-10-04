# -*- coding: iso-8859-15 -*-


from flask import Flask, request, render_template, url_for
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index1():
    return app.send_static_file('index1.html')


@app.route('/Inicio', methods=['GET'])
def Inicio():
    return app.send_static_file('Inicio.html')


@app.route('/Ingresar', methods=['GET', 'POST'])
def Ingresar():
    return app.send_static_file('Ingresar.html')


@app.route('/Registrarse', methods=['GET'])
def Registrarse():
    return app.send_static_file('Registrarse.html')


@app.route('/HistorialClinico', methods=['GET'])
def HistorialClinico():
    return app.send_static_file('HistorialClinico.html')


@app.route('/processLogin', methods=['GET', 'POST'])
def processLogin():
       missing = []
       fields = ['email', 'passwd', 'login_submit']
       for field in fields:
            value = request.form.get(field, None)
            if value is None or value == '':
                missing.append(field)
       if missing:
            return render_template('errorLog.html', inputs=missing, next=url_for("Ingresar"))

       return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<title> Home - SocNet </title>' \
           '</head>' \
           '<body> <div id ="container">' \
		   '<a href="/"> SocNet </a> | <a href="home"> Home </a> | <a href="login"> Log In </a> | <a href="signup"> Sign Up </a>' \
           '<h1>Data from Form: Login</h1>' \
	       '<form><label>email: ' + request.form['email'] + \
	       '</label><br><label>passwd: ' + request.form['passwd'] + \
           '</label></form></div></body>' \
           '</html>'


@app.route('/processSignup', methods=['GET', 'POST'])
def processSignup():
       missing = []
       fields = ['nickname', 'email', 'passwd', 'confirm', 'signup_submit']
       for field in fields:
              value = request.form.get(field, None)
              if value is None or value == '':
                     missing.append(field)
       if missing:
              return render_template('errorSign.html', inputs=missing, next=url_for("Registrarse"))

       return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<title> Home - SocNet </title>' \
           '</head>' \
           '<body> <div id ="container">' \
		   '<a href="/"> SocNet </a> | <a href="home"> Home </a> | <a href="login"> Log In </a> | <a href="signup"> Sign Up </a>' \
           '<h1>Data from Form: Sign Up</h1>' \
           '<form><label>Nickame: ' + request.form['nickname'] + \
	       '</label><br><label>email: ' + request.form['email'] + \
	       '</label><br><label>passwd: ' + request.form['passwd'] + \
	       '</label><br><label>confirm: ' + request.form['confirm'] + \
           '</label></form></div></body>' \
           '</html>'


@app.route('/processHome', methods=['GET', 'POST'])
def processHome():
	missing = []
	fields = ['message', 'last', 'post_submit']
	for field in fields:
		value = request.form.get(field, None)
		if value is None:
			missing.append(field)
	if missing:
		return "Warning: Some fields are missing"

	return render_template('DevHome.html', last= fields[1], message= fields[0])


#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, port=80)