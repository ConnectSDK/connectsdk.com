AirPlayService
==============
``com.connectsdk.service.AirPlayService``

*extends* :doc:`DeviceService <and-deviceservice>`

AirPlayService provides media playback/control & web app launching (iOS
only) capabilities for Apple TV devices.

AirPlay-enabled speakers are not currently supported by Connect SDK.

Properties
----------

final String X_APPLE_SESSION_ID = "X-Apple-Session-ID"

final String ID = "AirPlay"

Inner Classes
-------------

-  PlaybackPositionListener

Methods
-------

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPriorityLevel** (Class<?extends CapabilityMethods > *clazz*)
    **Parameters:**
    
    -  clazz

**AirPlayService** (ServiceDescription *serviceDescription*, ServiceConfig *serviceConfig*)
    **Parameters:**

    -  serviceDescription
    -  serviceConfig

:doc:`MediaControl <and-mediacontrol>` **getMediaControl** ()
    Get MediaControl implementation

    **Returns:** MediaControl

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaControlCapabilityLevel** ()
    Get a capability priority for current implementation

    **Returns:** CapabilityPriorityLevel

void **play** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **pause** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **stop** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **rewind** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **fastForward** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **previous** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    This method is deprecated. Use
    ``PlaylistControl::previous(ResponseListener<Object> listener)``
    instead.

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **next** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    This method is deprecated. Use
    ``PlaylistControl::next(ResponseListener<Object> listener)`` instead.

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **seek** (long *position*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  position – The new position, in milliseconds from the beginning of the stream
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getPosition** (final :doc: `PositionListener <and-positionlistener>` *listener*)
    **Parameters:**

    -  listener – (optional) final PositionListener with methods to be called on success or failure

void **getPlayState** (final :doc:`PlayStateListener <and-playstatelistener>` *listener*)
    AirPlay has the same response for Buffering and Finished states
    that's why this method always returns Finished state for video which
    is not ready to play.

    **Parameters:**

    -  listener – (optional) final PlayStateListener with methods to be called on success or failure

void **getDuration** (final :doc:`DurationListener <and-durationlistener>` *listener*)
    **Parameters:**

    -  listener – (optional) final DurationListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`PlayStateListener <and-playstatelistener>`> **subscribePlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)
    Subscribe for playback state changes

    **Parameters:**

    -  listener – receives play state notifications

    **Returns:** ServiceSubscription<PlayStateListener>

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
    **Parameters:**

    -  listener – (optional) MediaInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MediaInfoListener <and-mediainfolistener>`> **subscribeMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
    **Parameters:**

    -  listener – (optional) MediaInfoListener with methods to be called on success or failure

void **displayImage** (final String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, final LaunchListener *listener*)
    **Parameters:**

    -  url
    -  mimeType
    -  title
    -  description
    -  iconSrc
    -  listener – (optional) final LaunchListener with methods to be called on success or failure

void **displayImage** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, LaunchListener *listener*)
    **Parameters:**

    -  mediaInfo
    -  listener – (optional) LaunchListener with methods to be called on success or failure

void **playVideo** (final String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, boolean *shouldLoop*, final LaunchListener *listener*)
    **Parameters:**

    -  url
    -  mimeType
    -  title
    -  description
    -  iconSrc
    -  shouldLoop
    -  listener – (optional) final LaunchListener with methods to be called on success or failure

void **playMedia** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, boolean *shouldLoop*, LaunchListener *listener*)
    This method is deprecated. Use
    ``MediaPlayer::playMedia(MediaInfo mediaInfo, boolean shouldLoop, LaunchListener listener)``
    instead.

    **Parameters:**

    -  url
    -  mimeType
    -  title
    -  description
    -  iconSrc
    -  shouldLoop
    -  listener – (optional) LaunchListener with methods to be called on success or failure

void **playMedia** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, boolean *shouldLoop*, LaunchListener *listener*)
    **Parameters:**

    -  mediaInfo
    -  shouldLoop
    -  listener – (optional) LaunchListener with methods to be called on success or failure

void **closeMedia** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  launchSession
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **sendCommand** (final ServiceCommand<?> *serviceCommand*)
    **Parameters:**

    -  serviceCommand

void **sendPairingKey** (String *pairingKey*)
    **Parameters:**

    -  pairingKey

boolean **isConnectable** ()

boolean **isConnected** ()

void **connect** ()

void **disconnect** ()

void **onLoseReachability** (DeviceServiceReachability *reachability*)
    **Parameters:**

    -  reachability

static DiscoveryFilter **discoveryFilter** ()

Inherited Methods
-----------------

void **connect** ()
    Will attempt to connect to the DeviceService. The failure/success
    will be reported back to the DeviceServiceListener. If the connection
    attempt reveals that pairing is required, the DeviceServiceListener
    will also be notified in that event.

void **disconnect** ()
    Will attempt to disconnect from the DeviceService. The
    failure/success will be reported back to the DeviceServiceListener.

boolean **isConnected** ()
    Whether the DeviceService is currently connected

boolean **isConnectable** ()

void **cancelPairing** ()
    Explicitly cancels pairing in services that require pairing. In some
    services, this will hide a prompt that is displaying on the device.

void **sendPairingKey** (String *pairingKey*)
    Will attempt to pair with the DeviceService with the provided
    pairingData. The failure/success will be reported back to the
    DeviceServiceListener.

    **Parameters:**

    -  pairingKey – Data to be used for pairing. The type of this parameter will vary depending on what type of pairing is required, but is likely to be a string (pin code, pairing key, etc).

List<String> **getCapabilities** ()

boolean **hasCapability** (String *capability*)
    Test to see if the capabilities array contains a given capability.
    See the individual Capability classes for acceptable capability
    values.

    It is possible to append a wildcard search term ``.Any`` to the end
    of the search term. This method will return true for capabilities
    that match the term up to the wildcard.

    Example: ``Launcher.App.Any``

    **Parameters:**

    -  capability – Capability to test against

boolean **hasAnyCapability** (String... *capabilities*)
    Test to see if the capabilities array contains at least one
    capability in a given set of capabilities. See the individual
    Capability classes for acceptable capability values.

    See hasCapability: for a description of the wildcard feature provided
    by this method.

    **Parameters:**

    -  capabilities – Set of capabilities to test against

boolean **hasCapabilities** (List<String> *capabilities*)
    Test to see if the capabilities array contains a given set of
    capabilities. See the individual Capability classes for acceptable
    capability values.

    See hasCapability: for a description of the wildcard feature provided
    by this method.

    **Parameters:**

    -  capabilities – List of capabilities to test against

ServiceDescription **getServiceDescription** ()

ServiceConfig **getServiceConfig** ()

JSONObject **toJSONObject** ()

String **getServiceName** ()
    Name of the DeviceService (webOS, Chromecast, etc)

void **closeLaunchSession** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Closes the session on the first screen device. Depending on the
    sessionType, the associated service will have different ways of
    handling the close functionality.

    **Parameters:**

    -  launchSession – LaunchSession to close
    -  listener – (optional) listener to be called on success/failure

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
    **Parameters:**

    -  listener – (optional) MediaInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MediaInfoListener <and-mediainfolistener>`> **subscribeMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
    **Parameters:**

    -  listener – (optional) MediaInfoListener with methods to be called on success or failure

void **displayImage** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, LaunchListener *listener*)
    Display an image on the device. Not all devices support all of the
    parameters -- supply as many as you have available.

    **Related capabilities:**

    -  ``MediaPlayer.Display.Image``
    -  ``MediaPlayer.MediaData.Title``
    -  ``MediaPlayer.MediaData.Description``
    -  ``MediaPlayer.MediaData.Thumbnail``
    -  ``MediaPlayer.MediaData.MimeType``

    **Parameters:**

    -  mediaInfo – Object of MediaInfo class which includes all the information about an image to display.
    -  listener – (optional) LaunchListener with methods to be called on success or failure

void **playMedia** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, boolean *shouldLoop*, LaunchListener *listener*)
    Play an audio or video file on the device. Not all devices support
    all of the parameters -- supply as many as you have available.

     **Related capabilities:**

    -  ``MediaPlayer.Play.Video``
    -  ``MediaPlayer.Play.Audio``
    -  ``MediaPlayer.MediaData.Title``
    -  ``MediaPlayer.MediaData.Description``
    -  ``MediaPlayer.MediaData.Thumbnail``
    -  ``MediaPlayer.MediaData.MimeType``

    **Parameters:**

    -  mediaInfo – Object of MediaInfo class which includes all the information about an image to display.
    -  shouldLoop – Whether to automatically loop playback
    -  listener – (optional) LaunchListener with methods to be called on success or failure

void **closeMedia** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Close a running media session. Because media is handled differently
    on different platforms, it is required to keep track of LaunchSession
    and MediaControl objects to control that media session in the future.
    LaunchSession will be required to close the media and mediaControl
    will be required to control the media.

    **Related capabilities:**

    -  ``MediaPlayer.Close``

    **Parameters:**

    -  launchSession – LaunchSession object for use in closing media instance
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`MediaControl <and-mediacontrol>` **getMediaControl** ()
    Get MediaControl implementation

   **Returns:** MediaControl

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaControlCapabilityLevel** ()
    Get a capability priority for current implementation

   **Returns:** CapabilityPriorityLevel

void **play** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Send play command.

    **Related capabilities:**

    -  ``MediaControl.Play``

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **pause** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Send pause command.

    **Related capabilities:**

    -  ``MediaControl.Pause``

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **stop** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Send play command.

    **Related capabilities:**

    -  ``MediaControl.Stop``

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **rewind** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Send rewind command.

    **Related capabilities:**

    -  ``MediaControl.Rewind``

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **fastForward** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Send play command.

    **Related capabilities:**

    -  ``MediaControl.FastForward``

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **previous** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    This method is deprecated. Use
    ``PlaylistControl::previous(ResponseListener<Object> listener)``
    instead.

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **next** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    This method is deprecated. Use
    ``PlaylistControl::next(ResponseListener<Object> listener)`` instead.

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **seek** (long *position*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Seeks to a new position within the current media item

    **Related capabilities:**

    -  ``MediaControl.Seek``

    **Parameters:**

    -  position – The new position, in milliseconds from the beginning of the stream
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getDuration** (:doc:`DurationListener <and-durationlistener>` *listener*)
    Get the current media duration in milliseconds

    **Parameters:**

    -  listener – (optional) DurationListener with methods to be called on success or failure

void **getPosition** (:doc: `PositionListener <and-positionlistener>` *listener*)
    Get the current playback position in milliseconds

    **Parameters:**

    -  listener – (optional) PositionListener with methods to be called on success or failure

void **getPlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)
    Get the current state of playback

    **Parameters:**

    -  listener – (optional) PlayStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`PlayStateListener <and-playstatelistener>`> **subscribePlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)
    Subscribe for playback state changes

    **Parameters:**

    -  listener – receives play state notifications

    **Returns:** ServiceSubscription<PlayStateListener>

void **onLoseReachability** (DeviceServiceReachability *reachability*)
    **Parameters:**

    -  reachability

void **unsubscribe** (URLServiceSubscription<?> *subscription*)
    **Parameters:**

    -  subscription

void **sendCommand** (ServiceCommand<?> *command*)
    **Parameters:**

    -  command
