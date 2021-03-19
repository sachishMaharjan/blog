from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
all_posts = response.json()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:id>')
def get_post(id):
    print(id)
    return render_template("post.html", posts=all_posts, id=id)




if __name__ == "__main__":
    app.run(debug=True)
