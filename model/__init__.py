from osv import osv, fields

class training_order(osv.osv):
  """Order class"""
  _name    = 'training.order'
  _columns = {
    'name' : fields.char('Name', size=30, required=True),
    'date' : fields.date('Date'),
    'client' : fields.char('Client', size=30, required=True),
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