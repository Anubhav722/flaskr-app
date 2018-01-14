from flask import Flask
app = Flask(__name__)


@app.route('/hello/')
def hell():
    return "check"

# another way to add urls is to write 
# app.add_url_rule('hello', hell)

@app.route('/')
def hello_world():
    # return "Hello World"
    return "<h1>HELLO WORLD</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
