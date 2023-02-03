RemoteCameraControl
===========================================================
``com.connectsdk.service.capability.RemoteCameraControl``

*extends CapabilityMethods*

Properties
----------

String Any = "RemoteCameraControl.Any"

String RemoteCamera = "RemoteCameraControl.RemoteCamera"

String[] Capabilities = { RemoteCamera }

int LENS_FACING_FRONT = CameraCharacteristics.LENS_FACING_FRONT

int LENS_FACING_BACK = CameraCharacteristics.LENS_FACING_BACK

Inner Classes
-------------

* :doc:`RemoteCameraStartListener <and-remotecamerastartlistener>`
* :doc:`RemoteCameraStopListener <and-remotecamerastoplistener>`
* :doc:`RemoteCameraPlayingListener <and-remotecameraplayinglistener>`
* :doc:`RemoteCameraPropertyChangeListener <and-remotecamerapropertychangelistener>`
* :doc:`RemoteCameraErrorListener <and-remotecameraerrorlistener>`

Methods
-------

static int **getSdkVersion** (Context *context*)
    Returns the SDK version as an integer. (e.g., 301002)

    **Parameters:**

    * context - Application context

static boolean **isCompatibleOsVersion** ()
    Checks if the OS version can run the remote camera function.
    The remote camera function is supported on Android 7 (N, API Level 24) or higher.

static boolean **isRunning** (Context *context*)
    Checks if the remote camera function is running.

    **Parameters:**

    * context - Application context

static boolean	**isSupportRemoteCamera** (String *deviceId*)
    Checks if the TV supports the remote camera function. Currently, only webOS22 TVs are supported.

    **Parameters:**

    * deviceId - Device ID value of the TV

void **startRemoteCamera** (Context *context*, Surface *previewSurface*, boolean *micMute*, int *lensFacing*, RemoteCameraStartListener *startListener*);
    Starts the remote camera. Each step is passed through the :doc:`RemoteCameraStartListener <and-remotecamerastartlistener>` callback.

    **Parameters:**

    * context – Application context
    * previewSurface - SurfaceView to show a camera preview
    * micMute - Microphone mute settings
    * lensFacing - Camera lens direction
    * startListener - (optional) RemoteCameraStartListener with methods to be called on success or failure

void **stopRemoteCamera** (Context *context*, RemoteCameraStopListener *stopListener*);
    Stops the remote camera. The result is passed through the :doc:`RemoteCameraStopListener <and-remotecamerastoplistener>` callback.

    **Parameters:**

    * context – Application context
    * stopListener - (optional) RemoteCameraStopListener with methods to be called on success or failure

void **setMicMute** (Context *context*, boolean *micMute*)
    Sets the mute function of the microphone.

    **Parameters:**

    * context - Application context
    * micMute - Microphone mute settings

void **setLensFacing** (Context *context*, int *lensFacing*)
    Sets the front/rear camera lens use.

    **Parameters:**

    * context - Application context
    * lensFacing - Camera lens direction

void **setCameraPlayingListener** (Context *context*, RemoteCameraPlayingListener *playingListener*)
    Calls when starting play by selecting a remote camera on the TV.

    **Parameters:**

    * context - Application context
    * playingListener - RemoteCameraPlayingListener to be called when the camera playback starts on the TV

void **setPropertyChangeListener** (Context *context*, RemoteCameraPropertyChangeListener *propertyChangeListener*)
    Calls when camera properties such as brightness and white balance are changed.

    **Parameters:**

    * context - Application context
    * propertyChangeListener - RemoteCameraPropertyChangeListener to be called when camera properties are changed on the TV

void **setErrorListener** (Context *context*, ScreenMirroringErrorListener *errorListener*)
    Calls when an error occurs while running the remote camera.

    **Parameters:**

    * context – Application context
    * errorListener - RemoteCameraErrorListener to be called when an error occurs
