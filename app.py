from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/privacy-policy')
def privacy_policy():
    return render_template("privacy-policy.html")

@app.route('/termsOfUse')
def termsOfUse():
    return render_template("termsOfUse.html")

@app.route('/communitysGuidelines')
def communitysGuidelines():
    return render_template("communitysGuidelines.html")

@app.route('/subscriptionPolicy')
def subscriptionPolicy():
    return render_template("subscriptionPolicy.html")

if __name__ == "__main__":
    app.run()