from flask import Flask, render_template
import sqlite3
import os 

app = Flask(__name__)


### SERVER  
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8080))
if __name__ == "__main__":
    app.run(host=host, port=port) 
    

