RemoteCameraControlDelegate
=============

RemoteCameraControlDelegate allows your app to receive remote camera status information.

Methods
-------

\- (void)remoteCameraDidPair
   Calls when the remote camera and TV are first connected (You have to guide the user to accept the connection on the TV.)

\- (void)remoteCameraDidStart:(BOOL)\ *result*
   Calls to pass success or failure of connection with TV after starting remote camera function

   **Parameters:**

   - result – Connection result with TV

\- (void) **remoteCameraDidStop**:(BOOL)\ *result*
   Calls to pass the result of a remote camera stop request.

   **Parameters:**

   - result – Remote camera stop result

\- (void) **remoteCameraDidPlay**
   Calls when data transmission starts by requesting remote camera execution from TV.

\- (void) **remoteCameraDidChange**:(RemoteCameraProperty)\ *property*
   Calls when a camera setting is changed by TV App request.
   For the property types, refer to  :doc:`RemoteCameraProperty <ios-remotecameraproperty>`.

   **Parameters:**

   - property – Remote camera property

\- (void) **remoteCameraErrorDidOccur**:(RemoteCameraError)\ *error*
   Calls when an error occurs after starting the remote camera.
   For error types, refer to :doc:`RemoteCameraError <ios-remotecameraerror>`.

   **Parameters:**

   - error – Remote camera error
