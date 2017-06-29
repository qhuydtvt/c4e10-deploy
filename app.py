import os
from flask import *
import mlab
from mongoengine import *
from werkzeug.utils import secure_filename

app = Flask(__name__)
mlab.connect()

app.config["IMG_PATH"] = os.path.join(app.root_path, "images")

class Flower(Document):
    image = StringField()
    title = StringField()
    price = FloatField()



flower1 = Flower(
    image="https://www.vitacost.com/blog/wp-content/uploads/2016/05/Why-You-Need-More-Lavender-in-Your-Life-e1462955823730.jpg",
    title="Lavender",
    price=50000
)

# dump data

# flower1.save()

image = "https://s-media-cache-ak0.pinimg.com/736x/a3/47/10/a34710ee18cbeeabe8ca1ff4be65a2fd.jpg"
title = "Red rose"
price = 10000

flowers = [
    {
        "image": "https://s-media-cache-ak0.pinimg.com/736x/a3/47/10/a34710ee18cbeeabe8ca1ff4be65a2fd.jpg",
        "title": "Red rose",
        "price": 10000
    },
    {
        "image": "http://i.telegraph.co.uk/multimedia/archive/02899/tulipnegrita_2899511b.jpg",
        "title": "Tulipnegrita",
        "price": 20000
    },
    {
        "image": "https://www.vitacost.com/blog/wp-content/uploads/2016/05/Why-You-Need-More-Lavender-in-Your-Life-e1462955823730.jpg",
        "title": "Lavender",
        "price": 50000
    }
]


@app.route('/add-flower', methods=["GET", "POST"])
def add_flower():
    if request.method == "GET": # FORM Requested
        return render_template("add_flower.html")
    elif request.method == "POST": # User submitted FORM
        # 1: Get data (title, image, price)
        form = request.form

        title = form["title"]
        # image = form["image"]
        price = form["price"]

        image = request.files["image"]

        filename = secure_filename(image.filename)

        image.save(os.path.join(app.config["IMG_PATH"], filename))


        # 2: Save data into database
        new_flower = Flower(title=title,
                            image="/images/{0}".format(filename),
                            price=price)
        new_flower.save()

        return redirect(url_for("index"))


@app.route('/')
def index():
    return render_template("index.html", flowers=Flower.objects())


@app.route("/images/<image_name>")
def image(image_name):
    return send_from_directory(app.config["IMG_PATH"], image_name)

@app.route("/about")
def about():
    return "Hi, welcome to C4E. We are Huy be and Huy big. Hope you enjoy our class :) "

@app.route("/users/<username>")
def user(username):
    return "Hello, my name is " + username + ", welcome to my page <3"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return "{0} + {1} = {2}".format(a, b, a + b)

if __name__ == '__main__':
    app.run()
