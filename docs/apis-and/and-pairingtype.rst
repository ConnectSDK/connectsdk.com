PairingType
============================================================
``com.connectsdk.service.DeviceService.PairingType``

Enumerates available pairing types. It is used by a DeviceService for implementing pairing strategy.

Properties
----------

NONE
   DeviceService doesn't require pairing

FIRST_SCREEN
   In this mode user must confirm pairing on the first screen device (e.g. an alert on a TV)

PIN_CODE
   In this mode user must enter a pin code from a mobile device and send it to the first screen device

MIXED
   In this mode user can either enter a pin code from a mobile device or confirm pairing on the TV
