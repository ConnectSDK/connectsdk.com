DeviceServicePairingType
========================

Type of pairing that is required by a particular DeviceService. This
type will be passed along with the DeviceServiceDelegate
deviceService:pairingRequiredOfType:withData: message.

Properties
----------

DeviceServicePairingTypeNone
   DeviceService does not require pairing

DeviceServicePairingTypeFirstScreen
   DeviceService requires user interaction on the first screen (ex. pairing alert)

DeviceServicePairingTypePinCode
   First screen is displaying a pairing pin code that can be sent through the DeviceService

DeviceServicePairingTypeMixed
   DeviceService can pair with multiple pairing types (ex. first screen OR pin)

DeviceServicePairingTypeAirPlayMirroring
   DeviceService requires AirPlay mirroring to be enabled to connect

DeviceServicePairingTypeUnknown
   DeviceService pairing type is unknown
