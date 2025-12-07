from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib import messages

from products.models import ProductVariant


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a variant to the shopping bag """

    variant_id = request.POST.get('variant_id')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if not variant_id:
        messages.error(request, "No size selected.")
        return redirect(redirect_url)

    variant = get_object_or_404(ProductVariant, pk=variant_id)
    bag = request.session.get('bag', {})

    # Add or update
    if variant_id in bag:
        bag[variant_id] += quantity
    else:
        bag[variant_id] = quantity

    request.session['bag'] = bag

    messages.success(
        request,
        (
            f"Added {variant.product.name} ({variant.size}) "
            f" x {quantity} to your bag!"
        ), extra_tags="bag"
    )

    return redirect(redirect_url)


def adjust_bag(request, variant_id):
    """Adjust quantity of a variant in the bag"""

    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity'))

    variant = get_object_or_404(ProductVariant, pk=variant_id)

    if quantity > 0:
        bag[variant_id] = quantity
        messages.success(
            request,
            f"Updated {variant.product.name} ({variant.size}) to {quantity}.",
            extra_tags="bag"
        )
    else:
        bag.pop(variant_id, None)
        messages.success(
            request,
            f"Removed {variant.product.name} ({variant.size}) from your bag.",
            extra_tags="bag"
        )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, variant_id):
    """Remove an item from the shopping bag"""

    try:
        variant = get_object_or_404(ProductVariant, pk=variant_id)
        bag = request.session.get('bag', {})

        variant_id = str(variant_id)
        bag.pop(variant_id, None)
        request.session['bag'] = bag

        messages.success(
            request,
            f"Removed {variant.product.name} ({variant.size}) from your bag.",
            extra_tags="bag"
        )

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
