"""UniLED Models Database."""
from __future__ import annotations

from typing import Final

from .ble_ledchord import SP107E
from .ble_ledhue import SP110E
from .ble_banlanx1 import SP601E
from .ble_banlanx2 import SP611E, SP617E, SP620E
from .ble_banlanx3 import SP613E, SP614E
from .ble_banlanx4 import SP630E, SP648E

UNILED_TRANSPORT_BLE = "ble"
UNILED_TRANSPORT_NET = "net"

##
## Supported BLE Models
##
UNILED_BLE_MODELS: Final = [
    SP107E,
    SP110E,
    SP601E,
    SP611E,
    SP613E,
    SP614E,
    SP617E,
    SP620E,
    SP630E,
    SP648E,
]

##
## Supported NETwork Models
##
UNILED_NET_MODELS: Final = []

##
## All Supported Models
##
UNILED_MODELS: Final = {
    UNILED_TRANSPORT_BLE: UNILED_BLE_MODELS,
    UNILED_TRANSPORT_NET: UNILED_NET_MODELS,
}
