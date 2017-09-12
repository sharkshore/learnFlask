from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/hello')
def hello():
	return 'hello,Flask222'

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		return '登录成功'
	else:
		return '登录失败'


if __name__ == '__main__':
	app.run(debug=True)


url_for('static',filename='style.css')
