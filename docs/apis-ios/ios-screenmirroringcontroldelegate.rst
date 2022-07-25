ScreenMirroringControlDelegate
=============

ScreenMirroringControlDelegate allows your app to receive screen mirroring status information.

Methods
-------

\- (void) **screenMirroringDidStart**:(BOOL) *result*
   Calls to pass the result of a screen mirroring start request.

   **Parameters:**

   - result – Screen mirroring start result

\- (void) **screenMirroringDidStop**:(BOOL)\ *result*
   Calls to pass the result of a screen mirroring stop request.

   **Parameters:**

   - result – Screen mirroring stop result

\- (void) **screenMirroringErrorDidOccur**:(ScreenMirroringError)\ *error*
   Calls when an error occurs after starting the screen mirroring.
   For error types, refer to :doc:`ScreenMirroringError <ios-screenmirroringerror>`.

   **Parameters:**

   - error – Screen mirroring error
