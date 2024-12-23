from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQL Database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://HP:MamtaKiPu%24%24yHaiTight%23000@localhost/Product"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    path = db.Column(db.String(200), nullable=False)

class Electronics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Fashion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Kitchen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)


# Initialize the Database (only once on application startup)
with app.app_context():
    db.create_all()

    # Insert Initial Data (only once)
    if not Category.query.all():  # Only seed data if the table is empty
        category1 = Category(name='Electronics', image='/static/images/electro.jpg', path='/electronics')
        category2 = Category(name='Fashion', image='/static/images/fashion.jpg', path='/fashion')
        category3 = Category(name='Home & Kitchen', image='/static/images/home.png', path='/kitchen')
        category4 = Category(name='Books', image='/static/images/books.jpg', path='/books')

        db.session.add_all([category1, category2, category3, category4])
        db.session.commit()

    if not Electronics.query.all():  # Only seed data if the table is empty
        product1 = Electronics(name='SmartPhone', image='/static/images/iphone.jpg', price=149.99)
        product2 = Electronics(name='Laptop', image='/static/images/laptop.jpg', price=199.99)
        product3 = Electronics(name='Headphone', image='/static/images/headphone.jpg', price=299.99)


        db.session.add_all([product1, product2, product3])
        db.session.commit()

    if not Books.query.all():  # Only seed data if the table is empty
        book1 = Books(name='Soul', image='/static/images/soul.jpg', price=9.99)
        book2 = Books(name='Dune', image='/static/images/dune.jpg', price=12.99)
        book3 = Books(name='Recurssion', image='/static/images/recurssion.jpg', price=19.99)

        db.session.add_all([book1, book2, book3])
        db.session.commit()

    if not Fashion.query.all():  # Only seed data if the table is empty
        item1 = Fashion(name='Cargo', image='/static/images/cargo.jpg', price=29.99)
        item2 = Fashion(name='Skirt', image='/static/images/skirt.jpg', price=20.99)
        item3 = Fashion(name='Jacket', image='/static/images/jacket.jpg', price=32.99)

        db.session.add_all([item1, item2, item3])
        db.session.commit()

    if not Kitchen.query.all():  # Only seed data if the table is empty
        item1 = Kitchen(name='Mixxer', image='/static/images/mixxer.jpg', price=15.99)
        item2 = Kitchen(name='Tool', image='/static/images/tools.jpg', price=8.99)
        item3 = Kitchen(name='Bread Maker', image='/static/images/bread maker.jpg', price=12.99)

        db.session.add_all([item1, item2, item3])
        db.session.commit()



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/category')
def category():
    categories = Category.query.all()
    return render_template('category.html', categories=categories)

@app.route('/electronics')
def electronics():
    products = Electronics.query.all()
    return render_template('electronics.html', products=products)

@app.route('/fashion')
def fashion():
    products = Fashion.query.all()
    return render_template('fashion.html', products=products)

@app.route('/kitchen')
def kitchen():
    products = Kitchen.query.all()
    return render_template('home_kitchen.html', products=products)

@app.route('/books')
def books():
    products = Books.query.all()
    return render_template('books.html', books=products)

# Creating Custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
