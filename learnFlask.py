from flask import Flask, request, url_for, render_template

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

#判断get请求,还是post请求
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		return '登录成功'
	else:
		return '登录失败'

@app.route('/hellohtml')
@app.route('/hellohtml/<name>')
def hellohtml(name=None):
	app.logger.info('获取了一个请求',hellohtml)
	return render_template('hello.html',name=name)

#获取get请求参数
@app.route('/param')
def param():
	return request.args.get('name')



if __name__ == '__main__':
	app.run(debug=True)


url_for('static',filename='style.css')
