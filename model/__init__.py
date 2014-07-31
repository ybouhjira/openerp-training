from osv import osv, fields

class training_order(osv.osv):
  """Order class"""
  _name    = 'training.order'
  _columns = {
    'name' : fields.char('Name', size=30, required=True),
    'date' : fields.date('Date'),
    'client' : fields.many2one('res.partner','Client'),
  }

training_order()


class training_product(osv.osv):
  """Product class"""
  _name    = 'training.product'
  _columns = {
    'name' : fields.char('Name', size=30, required=True),
    'price' : fields.float('Price', digits=(12,2)),
  }
training_product()

class training_order_line(osv.osv):
  """Order line class"""

  def _get_price(self, cr, uid, ids, field_name=None, arg=None, context={}):
    res = {}
    for id in ids:
      res[id] = 10
    return res

  _name    = 'training.order_line'
  _columns = {
    'name' : fields.char('Name', size=30, required=True),
    'date' : fields.date('Date'),
    'product_id' : fields.many2one('training.product','Product'),
    'price' : fields.function(_get_price, string='Price', type='float') 
  }



training_order_line()