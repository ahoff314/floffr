from flask import Flask, render_template
app = Flask(__name__)
import os 

#remove debugger in prod please
app.debug = True

### ROUTES
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/rawr')
def rawr():
    return render_template('vapor.html')
### END ROUTES


    
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8080))
if __name__ == "__main__":
    app.run(host=host, port=port) 
    
    
