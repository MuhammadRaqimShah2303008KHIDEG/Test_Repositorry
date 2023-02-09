from flask import Flask

app= Flask(__name__)
@app.route('/')

def test():
    return  "Test repository to learn GitHub"

@app.route('/another_route')

def another_route():
    return  "Test repository to learn GitHub USING ANOTHER ROUTING TECHNIQUE "

if __name__=="__main__":
    app.run(debug=True)