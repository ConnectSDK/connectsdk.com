ScreenMirroringControl
===========================================================
``com.connectsdk.service.capability.ScreenMirroringControl``

*extends CapabilityMethods*

The ScreenMirroringControl capability protocol serves to define the methods required for displaying mobile app screen to LG TV.

Properties
----------

final String Any = "ScreenMirroringControl.Any"

final String ScreenMirroring = "ScreenMirroringControl.ScreenMirroring"

final String[] Capabilities = { ScreenMirroring }

Inner Classes
-------------

* :doc:`ScreenMirroringStartListener <and-screenmirroringstartlistener>`
* :doc:`ScreenMirroringStopListener <and-screenmirroringstoplistener>`
* :doc:`ScreenMirroringErrorListener <and-screenmirroringerrorlistener>`
* :doc:`ScreenMirroringError <and-screenmirroringerror>`

Methods
-------

static int **getSdkVersion** (Context *context*)
    Returns the SDK version as an integer. (e.g., 301002)

    **Parameters:**

    * context - Application context

static boolean **isCompatibleOsVersion** ()
    Checks if the OS version can run the screen mirroring function.
    The screen mirroring function is supported on Android 10 (Q, API Level 29) or higher.

static boolean **isRunning** (Context *context*)
    Checks if the screen mirroring function is running.

    **Parameters:**

    * context - Application context

static boolean	**isSupportScreenMirroring** (String *deviceId*)
    Checks if the TV supports the screen mirroring function. Currently, only webOS22 TVs are supported.

    **Parameters:**

    * deviceId - Device ID value of the TV

void **startScreenMirroring** (Context *context*, Intent *projectionData*, ScreenMirroringStartListener *onStartListener*)
    Starts the screen mirroring. Each step is passed through the  :doc:`ScreenMirroringStartListener <and-screenmirroringstartlistener>` callback.
    Before calling this function, user permission for screen capture must be obtained. This data can be passed as an argument.

    **Parameters:**

    * context – Application context
    * projectionData - Data to use mediaProjection
    * onStartListener - (optional) ScreenMirroringonStartListener with methods to be called on success or failure

void **startScreenMirroring** (Context *context*, Intent *projectionData*, Class *secondScreenClass*, ScreenMirroringStartListener *onStartListener*)
    Starts screen mirroring in the same way as the API above. There is a secondScreenClass parameter for dual screens.

    **Parameters:**

    * context – Application context
    * projectionData - Data to use mediaProjection
    * secondScreenClass - Screen object to use dual screen
    * onStartListener - (optional) ScreenMirroringonStartListener with methods to be called on success or failure

void **stopScreenMirroring** (Context *context*, ScreenMirroringStopListener *stopListener*)
    Stops the screen mirroring. The result is delivered through the  :doc:`ScreenMirroringStopListener <and-screenmirroringstoplistener>` callback.

    **Parameters:**

    * context – Application context
    * stopListener - (optional) ScreenMirroringStopListener with methods to be called on success or failure

void **setErrorListener** (Context *context*, ScreenMirroringErrorListener *errorListener*)
    Designates a :doc:`ScreenMirroringErrorListener <and-screenmirroringerrorlistener>` to check if an error occurs during execution.

    **Parameters:**

    * context – Application context
    * errorListener - ScreenMirroringErrorListener to be called when an error occurs
