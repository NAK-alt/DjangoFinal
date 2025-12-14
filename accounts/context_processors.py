from decimal import Decimal

def cart_context(request):
    """
    Injects 'cart', 'cart_count', and 'cart_total' into the context of every template.
    """
    
    # 1. Get the cart dictionary directly from the session
    cart = request.session.get('cart', {})
    
    # 2. Calculate the summary variables
    # Use sum() to calculate total quantity
    cart_count = sum(item.get('quantity', 0) for item in cart.values())
    
    # Calculate the total price based on the individual item totals (your views save 'total')
    # Use Decimal for accurate final calculation of the total price
    total_price = Decimal(sum(item.get('total', 0.0) for item in cart.values()))
    
    # 3. Return the variables to be used in your header template
    return {
        'cart': cart,          
        'cart_count': cart_count,    
        'cart_total': total_price, 
    }