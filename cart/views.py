from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """Open cart page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add camp to cart"""
    quantity = request.POST.get('quantity')
    if quantity == '':
        quantity = 1
    quantity = int(quantity)

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('home'))


def adjust_cart(request, id):
    """
    Change items in cart
    """
    quantity = request.POST.get('quantity')
    if quantity == '':
        quantity = 1
    quantity = int(quantity)
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))