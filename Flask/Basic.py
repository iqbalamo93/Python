from flask import Flask, request

app = Flask(__name__)

@app.route('/')# Route 1
def home():
    return 'welcome to home'

@app.route('/Add')
def add():
    a = 10
    b = 10
    return str(a+b+29)

@app.route('/Add_dynamic_get',methods=['GET'])
def add_parm_post():
    a = request.args.get('a')
    b = request.args.get('b')

    return str(int(a)+int(b))


@app.route('/Add_dynamic_post',methods=['POST'])
def add_parm():
    a = request.form['a']
    b = request.form['b']

    return str(int(a)+int(b))

if __name__ =='__main__':
    app.run()
