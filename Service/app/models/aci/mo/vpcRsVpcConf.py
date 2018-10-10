
from ... rest import Rest
from ... rest import api_register
from . import ManagedObject

import logging

# module level logging
logger = logging.getLogger(__name__)

@api_register(parent="fabric", path="mo/vpcRsVpcConf")
class vpcRsVpcConf(ManagedObject):

    # vpcRsVpcConf may not be a reliable subscription, seems to work ok on E+
    TRUST_SUBSCRIPTION = True

    META_ACCESS = ManagedObject.append_meta_access({
        "namespace":"vpcRsVpcConf",
    })

    META = ManagedObject.append_meta({
        "tSKey": {},
        "parentSKey": {},
    })
