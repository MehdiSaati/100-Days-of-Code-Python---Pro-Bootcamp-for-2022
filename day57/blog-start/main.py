# Blog Capstone Project Part 1
from flask import Flask, render_template
from post import Post
import requests
import datetime as dt

posts = requests.get("https://api.npoint.io/9b81097a622d688871fa").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

def get_current_year():
    """Returns the current year as INT."""
    # get the current year to display in the footer
    return dt.datetime.now().year

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects, year=get_current_year())


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=get_current_year())

if __name__ == "__main__":
   app.run(port=80, debug= True)

 
 

