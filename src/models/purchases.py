from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from src.models import BaseModel


class Cart(BaseModel):
    __tablename__ = 'cart'
    _id = Column(String(30), nullable=False)
    status = Column(String(30), nullable=False)
    total = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    delivery = Column(Float, nullable=False)
    delivery_cost = Column(Float, nullable=False)
    kind = Column(String(30), nullable=False)
    distribution_center = Column(String(30), nullable=False)
    purchase_id = Column(Integer, ForeignKey('purchase.id'))
    item = relationship('Item')

    @classmethod
    def get_all(cls, session):
        return session.query(Cart).all()

    @staticmethod
    def save(new_obj, data):
        for item in data:
            new_obj.item.append(item)
        return new_obj


class Item(BaseModel):
    __tablename__ = 'item'
    _id = Column(String(30), nullable=False)
    quantity = Column(Integer)
    kind = Column(String(30), nullable=False)
    price = Column(Float, nullable=False)
    unit = Column(String(30), nullable=False)
    name = Column(String(150), nullable=False)
    weight = Column(Float, nullable=False)
    cart_id = Column(Integer, ForeignKey('cart.id'))

    @classmethod
    def get_all(cls, session):
        return session.query(Item).all()


class Purchase(BaseModel):
    __tablename__ = 'purchase'
    _id = Column(String(30), nullable=False)
    user = Column(String(30), nullable=False)
    cart = relationship('Cart')
    distribution_center_id = Column(String(30), nullable=False)
    order = Column(Integer, nullable=False)
    delivery_status = Column(String(30), nullable=False)
    payment_status = Column(String(30), nullable=False)

    @classmethod
    def get_all(cls, session):
        return session.query(Purchase). \
                select_from(Purchase).join(Cart, Cart.purchase_id == Purchase.id). \
                join(Item, Item.cart_id == Cart.id).all()

    @classmethod
    def get_all_by_user(cls, session, user_id):
        return session.query(Purchase).select_from(Purchase).\
                join(Cart, Cart.purchase_id == Purchase.id). \
                join(Item, Item.cart_id == Cart.id).\
                filter(Purchase.user == user_id).all()

    def save(self, data, session):
        items = data['cart'].pop('items')
        new_items = [Item(**item) for item in items]

        new_cart = Cart(**data['cart'])
        cart = new_cart.save(new_cart, new_items)

        del data['cart']
        new_purchase = self(**data)
        new_purchase.cart.append(cart)
        session.add(new_purchase)
        session.commit()
