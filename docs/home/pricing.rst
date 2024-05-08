Pricing and Credits
===================

Credits are consumed when using the API. Each credit corresponds to 1 USD and there are **no charges on top of provider costs**; as a result, consumed credits directly reflect the cost of a request.

You can manage your billing and payments though the :code:`Billing` section of your `Unify Console <https://console.unify.ai>`_. **Upon signing-up, you are automatically granted $50 in free credits!**

.. note::
    If you want to check your current balance, you can do so at any time through the console but also directly within your terminal by querying the `Get Credits Endpoint <https://unify.ai/docs/hub/reference/endpoints.html#get-credits>`_ of the API.

Top-up Code
-----------

You may have received a code to increase your number credits, if that's the case, you can
activate it doing a request to this endpoint:

.. code-block:: bash

    curl -X 'POST' \
    'https://api.unify.ai/v0/promo?code=<CODE>' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer <YOUR_UNIFY_KEY>'

Simply replace :code:`<CODE>` with your top up code and :code:`<YOUR_UNIFY_KEY>` with your API Key and
do the request 🚀
