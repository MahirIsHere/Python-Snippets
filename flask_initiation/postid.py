from flask import Flask 

app = Flask(__name__)

#this can print the directory such as url/Mahir 
#output= "hello Mahir!"
@app.route("/<name>") 
def user(name):
    return f"hello {name}!"


if __name__ == '__main__':
    app.run()