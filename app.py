from flask import Flask, render_template
from flask_sse import sse
from  trevor_ai import update_message, start
from sharedObject import message

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost:6379/0"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/start_trevor_ai')
def start_trevor_ai():
    start()
    return {"message": "Ready"}  # Send an initial message
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/updateMessage')
def updateMessage():
    # Call the update_message function in MainLogic.py with the new value
    new_message = "New message value from Main Logic"
    update_message(new_message)

    # Notify connected clients about the change
    sse.publish({"message": message}, type='update')

    return f"Message updated to: {message}"
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
