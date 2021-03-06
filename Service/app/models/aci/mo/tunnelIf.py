
from ... rest import Rest
from ... rest import api_register
from . import ManagedObject

import logging

# module level logging
logger = logging.getLogger(__name__)

@api_register(parent="fabric", path="mo/tunnelIf")
class tunnelIf(ManagedObject):

    META_ACCESS = ManagedObject.append_meta_access({
        "namespace":"tunnelIf",
    })

    META = ManagedObject.append_meta({
        "id": {},
        "dest": {},
        "src": {},
        "operSt": {},
        "tType": {},
        "type": {},
    })

