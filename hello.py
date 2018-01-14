from flask import Flask, url_for, redirect, request, render_template
app = Flask(__name__)


@app.route('/hello')
def hell():
    return "check"

# building dynamic urls
@app.route('/hello/<name>')
def hello_name(name):
    return 'hello {}'.format(name)

# another way to add urls is to write 
# app.add_url_rule('hello', hell)

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/')
def hello_world():
    # return "Hello World"
    return "<h1>HELLO WORLD</h1>"


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_world'))
   else:
      return redirect(url_for('hello_name', name = name))


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


# ADDING AND RENDERING TEMPLATES
@app.route('/check/<user>')
def index(user):
    return render_template('hello.html', name=user)


@app.route('/change/<int:score>')
def change(score):
    return render_template('change.html', marks=score)


@app.route('/result/')
def result():
    d = {"phy": 50, "maths": 23, "chem": 17}
    return render_template('result.html', result=d)

@app.route('/static/')
def status():
    return render_template('static.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
