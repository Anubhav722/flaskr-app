from flask import Flask, url_for, redirect
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


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
