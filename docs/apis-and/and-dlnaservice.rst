DLNAService
===========
``com.connectsdk.service.DLNAService``

*extends* :doc:`DeviceService <and-deviceservice>`

DLNAService is a rough control implementation for the UPnP AVTransport,
MediaRenderer, and RenderingControl services. DLNA commands & events
occur over HTTP.

This service currently exists for the sole purpose of providing media
control/playback functionality for the NetcastTVService.
DiscoveryManager is currently set up to ignore any DLNA devices that are
not manufactured by LG. It is not recommended to remove this
restriction, as the DLNAService implementation is not complete.

To learn more about the protocols in use by DLNAService, check out the
following documents.

-  `UPnP <http://upnp.org/>`__
-  `AVTransport Service <http://upnp.org/specs/av/UPnP-av-AVTransport-v1-Service.pdf>`__
-  `MediaRenderer Device <http://upnp.org/specs/av/UPnP-av-MediaRenderer-v1-Device.pdf>`__
-  `RenderingControl Service <http://upnp.org/specs/av/UPnP-av-RenderingControl-v1-Service.pdf>`__

Properties
----------

final String ID = "DLNA"
final String AV_TRANSPORT_URN = "urn:schemas-upnp-org:service:AVTransport:1"
final String CONNECTION_MANAGER_URN = "urn:schemas-upnp-org:service:ConnectionManager:1"
final String RENDERING_CONTROL_URN = "urn:schemas-upnp-org:service:RenderingControl:1"
final String PLAY_STATE = "playState"
final String DEFAULT_SUBTITLE_MIMETYPE = "text/srt"
final String DEFAULT_SUBTITLE_TYPE = "srt"

Inner Classes
-------------

-  PositionInfoListener

Methods
-------

**DLNAService** (ServiceDescription *serviceDescription*, ServiceConfig *serviceConfig*)
    **Parameters:**

    -  serviceDescription
    -  serviceConfig

**DLNAService** (ServiceDescription *serviceDescription*, ServiceConfig *serviceConfig*, Context *context*, DLNAHttpServer *dlnaServer*)
    **Parameters:**

    -  serviceDescription
    -  serviceConfig
    -  context
    -  dlnaServer

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPriorityLevel** (Class<?extends CapabilityMethods > *clazz*)
    **Parameters:**

    -  clazz

void **setServiceDescription** (ServiceDescription *serviceDescription*)
    **Parameters:**

    -  serviceDescription

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (final :doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
    **Parameters:**

    -  listener – (optional) final MediaInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MediaInfoListener <and-mediainfolistener>`> **subscribeMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
    **Parameters:**

    -  listener – (optional) MediaInfoListener with methods to be called on success or failure

void **displayMedia** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, final LaunchListener *listener*)
    **Parameters:**

    -  url
    -  mimeType
    -  title
    -  description
    -  iconSrc
    -  listener – (optional) final LaunchListener with methods to be called on success or failure

void **displayImage** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, LaunchListener *listener*)
    This method is deprecated. Use
    ``MediaPlayer::displayImage(MediaInfo mediaInfo, LaunchListener listener)``
    instead.

    **Parameters:**

    -  url
    -  mimeType
    -  title
    -  description
    -  iconSrc
    -  listener – (optional) LaunchListener with methods to be called on success or failure

void **displayImage** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, LaunchListener *listener*)
    **Parameters:**

    -  mediaInfo
    -  listener – (optional) LaunchListener with methods to be called on success or failure

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

:doc:`PlaylistControl <and-playlistcontrol>` **getPlaylistControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPlaylistControlCapabilityLevel** ()

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

void **jumpToTrack** (long *index*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Play a track specified by index in the playlist

    **Parameters:**

    -  index – index in the playlist, it starts from zero like index of array
    -  listener – optional response listener

void **setPlayMode** (:doc:`PlayMode <and-playmode>` *playMode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Set order of playing tracks

    **Parameters:**

    -  playMode
    -  listener – optional response listener

void **seek** (long *position*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  position – The new position, in milliseconds from the beginning of the stream
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getDuration** (final :doc:`DurationListener <and-durationlistener>` *listener*)
    **Parameters:**

    -  listener – (optional) final DurationListener with methods to be called on success or failure

void **getPosition** (final :doc:`PositionListener <and-positionlistener>` *listener*)
    **Parameters:**

    -  listener – (optional) final PositionListener with methods to be called on success or failure

void **sendCommand** (final ServiceCommand<?> *mCommand*)
    **Parameters:**

    -  mCommand

:doc:`LaunchSession <and-launchsession>` **decodeLaunchSession** (String *type*, JSONObject *sessionObj*)
    **Parameters:**

    -  type
    -  sessionObj

void **getPlayState** (final :doc:`PlayStateListener <and-playstatelistener>` *listener*)
    **Parameters:**

    -  listener – (optional) final PlayStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`PlayStateListener <and-playstatelistener>`> **subscribePlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)
    Subscribe for playback state changes

    **Parameters:**

    -  listener – receives play state notifications

    **Returns:** ServiceSubscription<PlayStateListener>

void **unsubscribe** (URLServiceSubscription<?> *subscription*)
    **Parameters:**

    -  subscription

boolean **isConnectable** ()

boolean **isConnected** ()

void **connect** ()

void **disconnect** ()

void **onLoseReachability** (DeviceServiceReachability *reachability*)
    **Parameters:**

    -  reachability

void **subscribeServices** ()

void **resubscribeServices** ()

void **unsubscribeServices** ()

:doc:`VolumeControl <and-volumecontrol>` **getVolumeControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getVolumeControlCapabilityLevel** ()

void **volumeUp** (final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

void **volumeDown** (final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

void **setVolume** (float *volume*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  volume

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getVolume** (final :doc:`VolumeListener <and-volumelistener>` *listener*)
    **Parameters:**

    -  listener – (optional) final VolumeListener with methods to be called on success or failure

void **setMute** (boolean *isMute*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  isMute
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getMute** (final :doc:`MuteListener <and-mutelistener>` *listener*)
    **Parameters:**

    -  listener – (optional) final MuteListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`VolumeListener <and-volumelistener>`> **subscribeVolume** (:doc:`VolumeListener <and-volumelistener>` *listener*)
    **Parameters:**

    -  listener – (optional) VolumeListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MuteListener <and-mutelistener>`> **subscribeMute** (:doc:`MuteListener <and-mutelistener>` *listener*)
    **Parameters:**

    -  listener – (optional) MuteListener with methods to be called on success or failure

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

:doc:`PlaylistControl <and-playlistcontrol>` **getPlaylistControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPlaylistControlCapabilityLevel** ()

void **previous** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Jump playlist to the previous track.

    Play previous track in the playlist

    **Related capabilities:**

    -  ``PlaylistControl.Previous``

    **Parameters:**

    -  listener – optional response listener

void **next** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Jump playlist to the next track.

    Play next track in the playlist

    **Related capabilities:**

    -  ``PlaylistControl.Next``

    **Parameters:**

    -  listener – optional response listener

void **jumpToTrack** (long *index*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Jump the playlist to the designated track.

    Play a track specified by index in the playlist

    **Related capabilities:**

    -  ``PlaylistControl.JumpToTrack``

    **Parameters:**

    -  index – index in the playlist, it starts from zero like index of array
    -  listener – optional response listener

void **setPlayMode** (:doc:`PlayMode <and-playmode>` *playMode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Set order of playing tracks

    **Parameters:**

    -  playMode
    -  listener – optional response listener

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

void **getPosition** (:doc:`PositionListener <and-positionlistener>` *listener*)
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

:doc:`VolumeControl <and-volumecontrol>` **getVolumeControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getVolumeControlCapabilityLevel** ()

void **volumeUp** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Sends the volume up command to the device.

    **Related capabilities:**

    -  ``VolumeControl.UpDown``

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **volumeDown** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Sends the volume down command to the device.

    **Related capabilities:**

    -  ``VolumeControl.UpDown``

    **Parameters:**

    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **setVolume** (float *volume*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Set the volume of the device.

    **Related capabilities:**

    -  ``VolumeControl.Set``

    **Parameters:**

    -  volume – Volume as a float between 0.0 and 1.0
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getVolume** (:doc:`VolumeListener <and-volumelistener>` *listener*)
    Get the current volume of the device.

    **Related capabilities:**

    -  ``VolumeControl.Get``

    **Parameters:**

    -  listener – (optional) VolumeListener with methods to be called on success or failure

void **setMute** (boolean *isMute*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Set the current volume.

    **Related capabilities:**

    -  ``VolumeControl.Mute.Set``

    **Parameters:**

    -  isMute
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getMute** (:doc:`MuteListener <and-mutelistener>` *listener*)
    Get the current mute state.

    **Related capabilities:**

    -  ``VolumeControl.Mute.Get``

    **Parameters:**

    -  listener – (optional) MuteListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`VolumeListener <and-volumelistener>`> **subscribeVolume** (:doc:`VolumeListener <and-volumelistener>` *listener*)
    Subscribe to the volume on the TV.

    **Related capabilities:**

    -  ``VolumeControl.Subscribe``

    **Parameters:**

    -  listener – (optional) VolumeListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MuteListener <and-mutelistener>`> **subscribeMute** (:doc:`MuteListener <and-mutelistener>` *listener*)
    Subscribe to the mute state on the TV.

    **Related capabilities:**

    -  ``VolumeControl.Mute.Subscribe``

    **Parameters:**

    -  listener – (optional) MuteListener with methods to be called on success or failure

void **onLoseReachability** (DeviceServiceReachability *reachability*)
    **Parameters:**

    -  reachability

void **unsubscribe** (URLServiceSubscription<?> *subscription*)
    **Parameters:**

    -  subscription

void **sendCommand** (ServiceCommand<?> *command*)
    **Parameters:**

    -  command
