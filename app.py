from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    user_agent = request.headers.get('User-Agent')
    if is_mobile(user_agent):
        return render_template("mobile_index.html")
    else:
        return render_template("index.html")

@app.route('/about')
def about():
    user_agent = request.headers.get('User-Agent')
    if is_mobile(user_agent):
        return render_template("mobile_about.html")
    else:
        return render_template("about.html")


@app.route('/privacy-policy')
def privacy_policy():
    return render_template("privacy-policy.html")

@app.route('/Terms-Of-Use')
def termsOfUse():
    return render_template("termsOfUse.html")

@app.route('/Community\'s-Guidelines')
def communitysGuidelines():
    return render_template("communitysGuidelines.html")

@app.route('/Subscription-Policy')
def subscriptionPolicy():
    return render_template("subscriptionPolicy.html")

def is_mobile(user_agent):
    return True if 'Mobile' in user_agent else False

if __name__ == "__main__":
    app.run()