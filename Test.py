from flask import Flask

app= Flask(__name__)
@app.route('/')

def test():
    return  "Test repository to learn GitHub"

if __name__=="__main__":
    app.run(debug=True)