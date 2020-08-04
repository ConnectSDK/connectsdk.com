DeviceServiceListener com.connectsdk.service.DeviceService.DeviceServiceListener
================================================================================

Methods
-------

void **onConnectionRequired** (`DeviceService </apis/1-6-0/android/DeviceService>`__ *service*)
   If the DeviceService requires an active connection (websocket,
   pairing, etc) this method will be called.

   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  service –

      DeviceService that requires connection

void **onConnectionSuccess** (`DeviceService </apis/1-6-0/android/DeviceService>`__ *service*)
   After the connection has been successfully established, and after
   pairing (if applicable), this method will be called.

   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  service –

      DeviceService that was successfully connected

void **onCapabilitiesUpdated** (`DeviceService </apis/1-6-0/android/DeviceService>`__ *service*, List<String> *added*, List<String> *removed*)
   There are situations in which a DeviceService will update the
   capabilities it supports and propagate these changes to the
   DeviceService. Such situations include:

   -  on discovery, DIALService will reach out to detect if certain apps
      are installed

   -  on discovery, certain DeviceServices need to reach out for version
      & region information

   For more information on this particular method, see
   ConnectableDeviceDelegate's
   connectableDevice:capabilitiesAdded:removed: method.

   .. rubric:: Parameters:
      :name: parameters-2
      :class: method-detail-label

   -  service –

      DeviceService that has experienced a change in capabilities

   -  added –

      List<String> of capabilities that are new to the DeviceService

   -  removed –

      List<String> of capabilities that the DeviceService has lost

void **onDisconnect** (`DeviceService </apis/1-6-0/android/DeviceService>`__ *service*, Error *error*)
   This method will be called on any disconnection. If error is nil,
   then the connection was clean and likely triggered by the responsible
   DiscoveryProvider or by the user.

   .. rubric:: Parameters:
      :name: parameters-3
      :class: method-detail-label

   -  service –

      DeviceService that disconnected

   -  error –

      Error with a description of any errors causing the disconnect. If
      this value is nil, then the disconnect was clean/expected.

void **onConnectionFailure** (`DeviceService </apis/1-6-0/android/DeviceService>`__ *service*, Error *error*)
   Will be called if the DeviceService fails to establish a connection.

   .. rubric:: Parameters:
      :name: parameters-4
      :class: method-detail-label

   -  service –

      DeviceService which has failed to connect

   -  error –

      Error with a description of the failure

void **onPairingRequired** (`DeviceService </apis/1-6-0/android/DeviceService>`__ *service*, `PairingType </apis/1-6-0/android/PairingType>`__ *pairingType*, Object *pairingData*)
   If the DeviceService requires pairing, valuable data will be passed
   to the delegate via this method.

   .. rubric:: Parameters:
      :name: parameters-5
      :class: method-detail-label

   -  service –

      DeviceService that requires pairing

   -  pairingType –

      PairingType that the DeviceService requires

   -  pairingData –

      Any data that might be required for the pairing process, will
      usually be nil

void **onPairingSuccess** (`DeviceService </apis/1-6-0/android/DeviceService>`__ *service*)
   .. rubric:: Parameters:
      :name: parameters-6
      :class: method-detail-label

   -  service

void **onPairingFailed** (`DeviceService </apis/1-6-0/android/DeviceService>`__ *service*, Error *error*)
   If there is any error in pairing, this method will be called.

   .. rubric:: Parameters:
      :name: parameters-7
      :class: method-detail-label

   -  service –

      DeviceService that has failed to complete pairing

   -  error –

      Error with a description of the failure
