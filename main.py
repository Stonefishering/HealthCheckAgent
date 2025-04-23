from flask import Flask
app = Flask(__name__)

@app.route("/")
def health():
    return "HealthCheckAgent is alive."

if __name__ == "__main__":
    print("HealthCheckAgent started.")
    app.run(host="0.0.0.0", port=8101)

