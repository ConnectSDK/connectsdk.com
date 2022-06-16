ScreenMirroringStartListener
=========================
``com.connectsdk.service.capability.ScreenMirroringControl.ScreenMirroringStartListener``


Methods
-----------------

void **onPairing** ()
    Calls for pairing.
    Paring is required when connecting to a TV for the first time.
    When a paring callback occurs, the app must notify the user by displaying a pop-up with information.


void **onStart** (boolean *result*, SecondScreen *secondScreen*)
    Calls when screen mirroring starts. The mirroring start result is passed as a result parameter.

    **Parameters:**

    * result - Screen mirroring start result
    * secondScreen - Virtual second screen for dual screen
