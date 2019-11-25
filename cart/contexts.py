from django.shortcuts import get_object_or_404
from camps.models import Camp

def cart_contexts(request):
    """
    Ensures that the cart contents are available when rendering
    the page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    camp_count = 0
    
    for id, quantity in cart.items():
        camp = get_object_or_404(Camp, pk=id)
        total += quantity * camp.price
        camp_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'camp': camp})
    
    return {'cart_items': cart_items, 'total': total, 'camp_count': camp_count}

