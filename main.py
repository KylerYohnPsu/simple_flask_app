from flask import Flask


app = (Flask(__name__))

@app.route('/')
def hello():
    return "THIS FLASK APP IS DEPLOYED MAMA"



if __name__ == '__main__':
    app.run(debug=False)

