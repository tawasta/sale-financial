from odoo.addons.sale_stock.models.stock import (
    StockMove as SaleStockMove,
)
from odoo.addons.purchase_stock.models.stock_move import (
    StockMove as PurchaseStockMove,
)


def _get_source_document(self):
    res = PurchaseStockMove._get_source_document(self)
    if not self.purchase_line_id.order_id.sale_order_id:
        return self.sale_line_id.order_id or res
    else:
        return res


SaleStockMove._get_source_document = _get_source_document
