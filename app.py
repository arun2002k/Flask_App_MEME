from flask import Flask
name = 'main'
app = Flask(name)


@app.route('/')
def hello_world():

    return 'Helloooooooo World'

if name == 'main':
    app.run()