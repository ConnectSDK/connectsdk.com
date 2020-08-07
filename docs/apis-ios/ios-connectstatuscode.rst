ConnectStatusCode
=================

Helpful status codes that augment the localizedDescriptions of NSErrors
that crop up throughout many places of the SDK. Most NSErrors that
Connect SDK provides will have a ConnectStatusCode.

Properties
----------

ConnectStatusCodeError
   Generic error, unknown cause

ConnectStatusCodeTvError
   The TV experienced an error

ConnectStatusCodeCertificateError
   SSL certificate error

ConnectStatusCodeSocketError
   Error with WebSocket connection

ConnectStatusCodeNotSupported
   Requested action is not supported

ConnectStatusCodeArgumentError
   There was a problem with the provided arguments, see error description for details

ConnectStatusCodeNotConnected
   Device is not connected
