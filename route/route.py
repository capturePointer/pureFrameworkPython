#from functions import *
from controllers.nodeController import nodeController
nodeObj = nodeController()
routes = [
    (r'^$', nodeObj.index),
    (r'node/?$', nodeObj.index),
    (r'node/index/?$', nodeObj.index),
    (r'node/add/?$', nodeObj.add),
    (r'node/doAdd/?$', nodeObj.doAdd),
    (r'node/clear/?$', nodeObj.clear),
    (r'node/edit/?$', nodeObj.edit),
    (r'node/doEdit/?$', nodeObj.doEdit),
]
