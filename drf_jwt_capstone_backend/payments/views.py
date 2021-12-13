from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import stripe
# from flask import Flask, redirect, request

stripe.api_key = 'sk_test_51K4ujtItkYHTAHY6d6rpStiwQv3F6Sk4FQnG1L0C7xmbBLd84AnzoiKlFZYI0VFCXHduaXCpra2EDkNZRnNw75M0008RyOxipo'

# app = Flask(__name__,
#             static_url_path='',
#             static_folder='public')

YOUR_DOMAIN = 'http://localhost:3000'

# @app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{price_1K4vYAItkYHTAHY6gmlKOIkt}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '?success=true',
            cancel_url=YOUR_DOMAIN + '?canceled=true',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

# if __name__ == '__main__':
#     app.run(port=4242)
        

