.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================
Sale Invoicing Fee
===================
Adds an extra fee product to a sale order based on which online payment
method was used (or will be used) to pay it. Works both from the backend
(manually setting the payment method on an order) and from any channel
that sets it programmatically, such as a webshop checkout.

This is the channel-agnostic base module: it only defines the data model
and the logic to add/replace the fee line on a sale order; it has no
website/checkout UI of its own. See ``website_sale_invoicing_fee`` for the
webshop checkout integration.

Configuration
=============
1. Go to **Invoicing > Configuration > Payment Methods**
2. Open the payment method that should carry an extra fee
3. Set the **Extra fee product** field

Optionally, set a customer's usual payment method on their contact form
(**Sales & Purchase** tab, **Usual Payment Method (Webshop)**) so new
orders for that customer default to it.

Usage
=====
Set ``sale.order.payment_method_id`` (visible on the order form as
**Selected Payment Method (Webshop)**) to the ``payment.method`` the
order will be/was paid with. The order's fee line is kept in sync
automatically:

- A fee line is added if the payment method has an extra fee product
  and no matching line exists yet
- Any stale fee line from a previously selected payment method is
  removed
- Calling it again with the same or no payment method is a no-op /
  clears the fee, respectively

New orders default ``payment_method_id`` from the customer's **Usual
Payment Method**, if set, exactly like ``payment_term_id`` defaults from
the customer's payment terms. Any later change (backend or webshop)
overrides that default.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
