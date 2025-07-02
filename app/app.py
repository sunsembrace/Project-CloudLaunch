from Flask import Flask #Import flask class  from flask module.

app = Flask(__name__) #Create an instance of the Flask class; my web app.

@app.route("/") #define a route (URL Endpoint) for the website the "/" means the homepage.
def hello(): #This function runs when someone visits "/"
    return "Hello, world!" #Send the text "Hello, world!" as the response to the browser.

if __name__ == "__main__": #This makes sure the app runs only if you run the script directly (not if imported).
    app.run(host="0.0.0.0", port= 5000) #0.0.0.0 menas all listens and accepts all network interfaces (required for docker). #port 5000 means app runs on this port.