from marshmallow import Schema, fields, validate
from marshmallow.utils import INCLUDE


class ItemOutSchema(Schema):
    qty = fields.Float(required=True)
    price = fields.Float(required=True)
    name = fields.String(required=True, validate=[validate.Length(min=1, max=150)])


class PurchaseOutSchema(Schema):
    user_id = fields.String(required=True, validate=[validate.Length(min=1, max=50)])
    items = fields.Nested(ItemOutSchema, many=True)
    amount = fields.Float(required=True)


class ItemInSchema(Schema):
    class Meta:
        unknown = INCLUDE

    quantity = fields.Integer()
    kind = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
    price = fields.Float(required=True)
    unit = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
    name = fields.String(required=True, validate=[validate.Length(min=1, max=150)])
    weight = fields.Float(required=True)


class CartInSchema(Schema):
    class Meta:
        unknown = INCLUDE
    status = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
    total = fields.Float(required=True)
    subtotal = fields.Float(required=True)
    delivery = fields.Float(required=True)
    delivery_cost = fields.Float(required=True)
    kind = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
    distribution_center = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
    item = fields.Nested(ItemInSchema, many=True)


class PurchaseInSchema(Schema):
    class Meta:
        unknown = INCLUDE
    user = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
    cart = fields.Nested(CartInSchema, many=True)
    distribution_center_id = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
    order = fields.Integer(required=True)
    delivery_status = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
    payment_status = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
