import itertools
from src.database.schemas import PurchaseInSchema


def calculate_amount(items):
    amount = [item['qty'] * item['price'] for item in items]
    return sum(amount)


def build_payload(all_items):
    new_data = []
    purshase_data = [PurchaseInSchema().dump(item) for item in all_items]

    for data in purshase_data:
        items = itertools.chain(*[c['item'] for c in data['cart']])
        items = [{'qty': i['quantity'], 'price': i['price'], 'name': i['name']} for i in items]
        new_data.append({
            'user_id': data['user'],
            'items': items,
            'amount': calculate_amount(items)
        })
    return new_data


def prepare_item(item):
    item.pop('_id')
    new_item = {
        '_id': item['id'],
        'user': item['user'],
        'cart': {
            '_id': item['cart']['id'],
            'status': item['cart']['status'],
            'total': item['cart']['billing']['total'],
            'subtotal': item['cart']['billing']['subtotal'],
            'delivery': item['cart']['billing']['delivery'],
            'delivery_cost': item['cart']['delivery_settings']['delivery_cost'],
            'kind': item['cart']['delivery_settings']['kind'],
            'distribution_center': item['cart']['delivery_settings']['distribution_center'],
        },
        'distribution_center_id': item['distribution_center_id'],
        'order': item['order'],
        'delivery_status': item['delivery_status'],
        'payment_status': item['payment_status']
    }
    new_item['cart'].update({
        'items': [
            {
                '_id': item['item']['id'],
                'quantity': item['quantity'],
                'kind': item['kind'],
                'price': item['item']['price'],
                'unit': item['item']['unit'],
                'name': item['item']['name'],
                'weight': item['item']['weight']
            } for item in item['cart']['items']
        ]
    })
    return new_item
