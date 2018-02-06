#from functions import *
from controllers.note import note
n = note()
routes = [
    (r'^$', n.index),
    (r'index/?$', n.index),
    (r'add/?$', n.add),
    (r'doAdd/?$', n.doAdd),
    (r'clear/?$', n.clear),
    (r'edit/?$', n.edit),
    (r'doEdit/?$', n.doEdit),
]
