from flask import Flask

app = Flask(**name**)

@app.route("/")
def hello():
return "DevSecOps scanner test application"

@app.route("/health")
def health():
return "OK"

if **name** == "**main**":
app.run(host="0.0.0.0", port=5000)
