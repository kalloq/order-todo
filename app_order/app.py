from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import OrderForm
from models import db, Product, Order

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    if Product.query.count() == 0:
        products = [
            Product(name='Produkt A', description='Opis produktu A'),
            Product(name='Produkt B', description='Opis produktu B'),
            Product(name='Produkt C', description='Opis produktu C'),
        ]
        db.session.add_all(products)
        db.session.commit()

@app.route('/')
def index():
    return redirect(url_for('place_order'))

@app.route('/place_order', methods=['GET', 'POST'])
def place_order():
    form = OrderForm()
    form.product.choices = [(p.id, p.name) for p in Product.query.all()]
    if form.validate_on_submit():
        order = Order(
            email=form.email.data,
            shipping_address=form.shipping_address.data,
            product_id=form.product.data
        )
        db.session.add(order)
        db.session.commit()
        flash('Zamówienie zostało złożone!', 'success')
        return redirect(url_for('place_order'))
    return render_template('place_order.html', form=form)

@app.route('/orders')
def orders():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
