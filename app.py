# /**
#  *
#  * project name : dp todo application
#  * author name  : mindula dilthushan
#  * author email : minduladilthushan1@gmail.com
#  *
#  */
from flask import Flask

app = Flask(__name__)

@app.route('/')
def root_route():
    return 'Welcome DP Todo Application !'


if __name__ == '__main__':
    app.run()
