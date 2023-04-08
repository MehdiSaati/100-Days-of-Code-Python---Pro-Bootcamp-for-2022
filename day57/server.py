from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')

def home_page():
    current_year = datetime.datetime.now().year

    your_name = "Mehdi Saati"

    random_number = random.randint(1,10)

    return render_template("index.html", num=random_number, year= current_year, name = your_name)
@app.route('/guess/<name>')

def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    your_gender = gender_data["gender"]

    age_url = f"https://agify.io/?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    your_age = age_data["gender"]

    return render_template("guess.html", name = name , gender = your_gender, age= your_age)

@app.route('/blog/<num>')
def get_blog(num):
    print (num)
    blog_url = "https://api.npoint.io/f73c776a2c18e2bc2c81"
    response = requests.get(blog_url)
    all_post = response.json()

    return render_template("blog.html", posts=all_post)

if __name__ == "__main__":
   app.run(port=80, debug= True)
