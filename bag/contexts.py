from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import ProductVariant


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for variant_id, quantity in bag.items():

        variant = get_object_or_404(ProductVariant, pk=variant_id)
        product = variant.product

        subtotal = quantity * variant.price
        total += subtotal
        product_count += quantity

        bag_items.append({
            'item_id': variant_id,
            'variant': variant,
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
