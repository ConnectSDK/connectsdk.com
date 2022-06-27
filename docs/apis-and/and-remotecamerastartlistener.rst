RemoteCameraStartListener
=========================
``com.connectsdk.service.capability.RemoteCameraControl.RemoteCameraStartListener``

Methods
-----------------

void **onPairing** ()
    Calls for paring.
    Paring is required when connecting to a TV for the first time.
    When a paring callback occurs, the app must notify the user by displaying a pop-up with information.


void **onStart** (boolean *result*)
    Calls when the remote camera is connected to the TV.
    In this state, the remote camera is only connected to the TV, and the camera screen is not displayed.

    **Parameters:**

    * result - Remote camera start result


 