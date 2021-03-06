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
    obj = self.browse(cr, uid, ids)

    for o in obj:
      print o.product_id.price * o.quantity
      res[o.id] = o.product_id.price * o.quantity

    return res

  def calculate_price(self, cr, uid, ids, product_id, quantity, context={}):
    product_obj = self.pool.get('training.product')
    product_dict = product_obj.read(cr,uid,[product_id],['price'])
    
    return {'value' : {'price' : product_dict[0]['price'] * quantity}}


  _name    = 'training.order_line'
  _columns = {
    'name' : fields.char('Name', size=30, required=True),
    'date' : fields.date('Date'),
    'product_id' : fields.many2one('training.product','Product'),
    'price' : fields.function(_get_price, string='Price', type='float'),
    'quantity' : fields.integer('Quantity'),
  }



training_order_line()