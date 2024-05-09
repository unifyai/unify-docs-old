Setting-Up
==========

In this section, we'll go through how you can set-up your account pages to get started querying endpoints.

Billing
-------

The :code:`Billing` page is where you can set-up your payment information to recharge your account, and track your spending. 

By default, you can only top-up manually by clicking on :code:`Buy Credits`. **We recommend you set-up automatic refill** to avoid any disruption to your workflows when your credits run out.

.. image:: ../images/console_billing_no_payment.png
  :align: center
  :width: 650
  :alt: Console Billing No Payment.

Automatic refill
^^^^^^^^^^^^^^^^

Activating automatic refill requires you go through the dedicated :code:`Billing Portal` where you can add your preferred payment method, update your billing information, and download your invoices.

.. image:: ../images/console_portal_welcome.png
  :align: center
  :width: 650
  :alt: Console Portal Welcome.

Clicking on :code:`Add Payment Methods` then lets you introduce your card information.

.. image:: ../images/console_portal_setup.png
  :align: center
  :width: 650
  :alt: Console Portal Setup.

With your payment information set-up, you can now toggle automatic refill on and off as needed on the main billing page. 

Automatic refill lets you specify the cut-off amount at which your account is automatically refilled by the specified amount when it reaches it.

.. image:: ../images/console_billing_payment.png
  :align: center
  :width: 650
  :alt: Console Billing Payment.


Pricing and credits
^^^^^^^^^^^^^^^^^^^

Credits are consumed when you query endpoints. Because we **don't apply any charge on top of provider costs**, consumed credits directly reflect the cost of a request. Upon signing-up, you are automatically granted **$50 in free credits**!

.. note::
    You can check your current balance through the billing page but also also directly within your terminal by querying the `Get Credits Endpoint <https://unify.ai/docs/api/reference.html#get-credits>`_ of the API.

Top-up codes
^^^^^^^^^^^^

You may have received a code to increase your number credits, if that's the case, you can activate it doing a request to this endpoint:

.. code-block:: bash

    curl -X 'POST' \
    'https://api.unify.ai/v0/promo?code=<CODE>' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer <YOUR_UNIFY_KEY>'

Simply replace :code:`<CODE>` with your top up code and :code:`<YOUR_UNIFY_KEY>` with your API Key and do the request 🚀

(Optional) Customizing your profile
-----------------------------------

Depending on the sign-up method you chose, some of the entries in the :code:`Profile` sections will already be populated. Regardless, you can use this page to change your email address, add your personal information, and sign out in case you’d like to use another account.

.. image:: ../images/console_profile.png
  :align: center
  :width: 650
  :alt: Console Profile.

Round Up
--------

You're all set! In the next section, you will learn how to upload your own endpoints and datasets on the console.
