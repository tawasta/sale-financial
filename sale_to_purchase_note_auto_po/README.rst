.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================================================
Sale to Purchase Note for Automatic Purchase Orders
====================================================

* Adds the same customer reference note that the "Create Purchase Order"
  button (from ``sale_order_to_purchase_order``) writes on manually created
  purchase orders, but for purchase orders that Odoo generates
  **automatically** from a sale order (MTO/Buy replenishment, subcontracting,
  ...).
* Whenever such an automatically generated purchase order's procurement
  group traces back to a sale order, that purchase order's ``Sale Order``
  field is filled in, and if the sale order has a Customer Reference set,
  the purchase order's Notes field is filled with the company's
  ``sale_to_purchase_note_text`` followed by that reference.

Configuration
=============
* No configuration needed beyond what ``sale_order_to_purchase_order``
  already requires (the company's "Sale to purchase note text" field).

Usage
=====
* Confirm a sale order for a product configured so that Odoo automatically
  creates a purchase order for it (e.g. Buy + Make To Order routes, or a
  subcontracted Bill of Materials).
* If the sale order has a Customer Reference, the resulting purchase order's
  Notes field is filled in automatically.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Futural Oy

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
