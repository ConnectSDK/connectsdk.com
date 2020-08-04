DLNAService com.connectsdk.service.DLNAService
==============================================

*extends*\ `DeviceService </apis/1-6-0/android/DeviceService>`__

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
-  `AVTransport
   Service <http://upnp.org/specs/av/UPnP-av-AVTransport-v1-Service.pdf>`__
-  `MediaRenderer
   Device <http://upnp.org/specs/av/UPnP-av-MediaRenderer-v1-Device.pdf>`__
-  `RenderingControl
   Service <http://upnp.org/specs/av/UPnP-av-RenderingControl-v1-Service.pdf>`__

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
   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  serviceDescription
   -  serviceConfig

**DLNAService** (ServiceDescription *serviceDescription*, ServiceConfig *serviceConfig*, Context *context*, DLNAHttpServer *dlnaServer*)
   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  serviceDescription
   -  serviceConfig
   -  context
   -  dlnaServer

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getPriorityLevel** (Class<?extends CapabilityMethods > *clazz*)
   .. rubric:: Parameters:
      :name: parameters-2
      :class: method-detail-label

   -  clazz

void **setServiceDescription** (ServiceDescription *serviceDescription*)
   .. rubric:: Parameters:
      :name: parameters-3
      :class: method-detail-label

   -  serviceDescription

`MediaPlayer </apis/1-6-0/android/MediaPlayer>`__ **getMediaPlayer** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (final `MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-4
      :class: method-detail-label

   -  listener –

      (optional) final MediaInfoListener with methods to be called on
      success or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__> **subscribeMediaInfo** (`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-5
      :class: method-detail-label

   -  listener –

      (optional) MediaInfoListener with methods to be called on success
      or failure

void **displayMedia** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, final LaunchListener *listener*)
   .. rubric:: Parameters:
      :name: parameters-6
      :class: method-detail-label

   -  url

   -  mimeType

   -  title

   -  description

   -  iconSrc

   -  listener –

      (optional) final LaunchListener with methods to be called on
      success or failure

void **displayImage** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, LaunchListener *listener*)
   This method is deprecated. Use
   ``MediaPlayer::displayImage(MediaInfo mediaInfo, LaunchListener listener)``
   instead.

   .. rubric:: Parameters:
      :name: parameters-7
      :class: method-detail-label

   -  url

   -  mimeType

   -  title

   -  description

   -  iconSrc

   -  listener –

      (optional) LaunchListener with methods to be called on success or
      failure

void **displayImage** (`MediaInfo </apis/1-6-0/android/MediaInfo>`__ *mediaInfo*, LaunchListener *listener*)
   .. rubric:: Parameters:
      :name: parameters-8
      :class: method-detail-label

   -  mediaInfo

   -  listener –

      (optional) LaunchListener with methods to be called on success or
      failure

void **playMedia** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, boolean *shouldLoop*, LaunchListener *listener*)
   This method is deprecated. Use
   ``MediaPlayer::playMedia(MediaInfo mediaInfo, boolean shouldLoop, LaunchListener listener)``
   instead.

   .. rubric:: Parameters:
      :name: parameters-9
      :class: method-detail-label

   -  url

   -  mimeType

   -  title

   -  description

   -  iconSrc

   -  shouldLoop

   -  listener –

      (optional) LaunchListener with methods to be called on success or
      failure

void **playMedia** (`MediaInfo </apis/1-6-0/android/MediaInfo>`__ *mediaInfo*, boolean *shouldLoop*, LaunchListener *listener*)
   .. rubric:: Parameters:
      :name: parameters-10
      :class: method-detail-label

   -  mediaInfo

   -  shouldLoop

   -  listener –

      (optional) LaunchListener with methods to be called on success or
      failure

void **closeMedia** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-11
      :class: method-detail-label

   -  launchSession

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

`MediaControl </apis/1-6-0/android/MediaControl>`__ **getMediaControl** ()
   Get MediaControl implementation

   .. rubric:: Returns:
      :name: returns
      :class: method-detail-label

   MediaControl

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getMediaControlCapabilityLevel** ()
   Get a capability priority for current implementation

   .. rubric:: Returns:
      :name: returns-1
      :class: method-detail-label

   CapabilityPriorityLevel

void **play** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-12
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **pause** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-13
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **stop** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-14
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **rewind** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-15
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **fastForward** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-16
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

`PlaylistControl </apis/1-6-0/android/PlaylistControl>`__ **getPlaylistControl** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getPlaylistControlCapabilityLevel** ()

void **previous** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   This method is deprecated. Use
   ``PlaylistControl::previous(ResponseListener<Object> listener)``
   instead.

   .. rubric:: Parameters:
      :name: parameters-17
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **next** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   This method is deprecated. Use
   ``PlaylistControl::next(ResponseListener<Object> listener)`` instead.

   .. rubric:: Parameters:
      :name: parameters-18
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **jumpToTrack** (long *index*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Play a track specified by index in the playlist

   .. rubric:: Parameters:
      :name: parameters-19
      :class: method-detail-label

   -  index –

      index in the playlist, it starts from zero like index of array

   -  listener –

      optional response listener

void **setPlayMode** (`PlayMode </apis/1-6-0/android/PlayMode>`__ *playMode*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Set order of playing tracks

   .. rubric:: Parameters:
      :name: parameters-20
      :class: method-detail-label

   -  playMode

   -  listener –

      optional response listener

void **seek** (long *position*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-21
      :class: method-detail-label

   -  position –

      The new position, in milliseconds from the beginning of the stream

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getDuration** (final `DurationListener </apis/1-6-0/android/DurationListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-22
      :class: method-detail-label

   -  listener –

      (optional) final DurationListener with methods to be called on
      success or failure

void **getPosition** (final `PositionListener </apis/1-6-0/android/PositionListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-23
      :class: method-detail-label

   -  listener –

      (optional) final PositionListener with methods to be called on
      success or failure

void **sendCommand** (final ServiceCommand<?> *mCommand*)
   .. rubric:: Parameters:
      :name: parameters-24
      :class: method-detail-label

   -  mCommand

`LaunchSession </apis/1-6-0/android/LaunchSession>`__ **decodeLaunchSession** (String *type*, JSONObject *sessionObj*)
   .. rubric:: Parameters:
      :name: parameters-25
      :class: method-detail-label

   -  type
   -  sessionObj

void **getPlayState** (final `PlayStateListener </apis/1-6-0/android/PlayStateListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-26
      :class: method-detail-label

   -  listener –

      (optional) final PlayStateListener with methods to be called on
      success or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`PlayStateListener </apis/1-6-0/android/PlayStateListener>`__> **subscribePlayState** (`PlayStateListener </apis/1-6-0/android/PlayStateListener>`__ *listener*)
   Subscribe for playback state changes

   .. rubric:: Parameters:
      :name: parameters-27
      :class: method-detail-label

   -  listener –

      receives play state notifications

   .. rubric:: Returns:
      :name: returns-2
      :class: method-detail-label

   ServiceSubscription<PlayStateListener>

void **unsubscribe** (URLServiceSubscription<?> *subscription*)
   .. rubric:: Parameters:
      :name: parameters-28
      :class: method-detail-label

   -  subscription

boolean **isConnectable** ()

boolean **isConnected** ()

void **connect** ()

void **disconnect** ()

void **onLoseReachability** (DeviceServiceReachability *reachability*)
   .. rubric:: Parameters:
      :name: parameters-29
      :class: method-detail-label

   -  reachability

void **subscribeServices** ()

void **resubscribeServices** ()

void **unsubscribeServices** ()

`VolumeControl </apis/1-6-0/android/VolumeControl>`__ **getVolumeControl** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getVolumeControlCapabilityLevel** ()

void **volumeUp** (final `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-30
      :class: method-detail-label

   -  listener –

      (optional) final ResponseListener< Object > with methods to be
      called on success or failure

void **volumeDown** (final `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-31
      :class: method-detail-label

   -  listener –

      (optional) final ResponseListener< Object > with methods to be
      called on success or failure

void **setVolume** (float *volume*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-32
      :class: method-detail-label

   -  volume

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getVolume** (final `VolumeListener </apis/1-6-0/android/VolumeListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-33
      :class: method-detail-label

   -  listener –

      (optional) final VolumeListener with methods to be called on
      success or failure

void **setMute** (boolean *isMute*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-34
      :class: method-detail-label

   -  isMute

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getMute** (final `MuteListener </apis/1-6-0/android/MuteListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-35
      :class: method-detail-label

   -  listener –

      (optional) final MuteListener with methods to be called on success
      or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`VolumeListener </apis/1-6-0/android/VolumeListener>`__> **subscribeVolume** (`VolumeListener </apis/1-6-0/android/VolumeListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-36
      :class: method-detail-label

   -  listener –

      (optional) VolumeListener with methods to be called on success or
      failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`MuteListener </apis/1-6-0/android/MuteListener>`__> **subscribeMute** (`MuteListener </apis/1-6-0/android/MuteListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-37
      :class: method-detail-label

   -  listener –

      (optional) MuteListener with methods to be called on success or
      failure

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

   .. rubric:: Parameters:
      :name: parameters-38
      :class: method-detail-label

   -  pairingKey –

      Data to be used for pairing. The type of this parameter will vary
      depending on what type of pairing is required, but is likely to be
      a string (pin code, pairing key, etc).

List<String> **getCapabilities** ()

boolean **hasCapability** (String *capability*)
   Test to see if the capabilities array contains a given capability.
   See the individual Capability classes for acceptable capability
   values.

   It is possible to append a wildcard search term ``.Any`` to the end
   of the search term. This method will return true for capabilities
   that match the term up to the wildcard.

   Example: ``Launcher.App.Any``

   .. rubric:: Parameters:
      :name: parameters-39
      :class: method-detail-label

   -  capability –

      Capability to test against

boolean **hasAnyCapability** (String... *capabilities*)
   Test to see if the capabilities array contains at least one
   capability in a given set of capabilities. See the individual
   Capability classes for acceptable capability values.

   See hasCapability: for a description of the wildcard feature provided
   by this method.

   .. rubric:: Parameters:
      :name: parameters-40
      :class: method-detail-label

   -  capabilities –

      Set of capabilities to test against

boolean **hasCapabilities** (List<String> *capabilities*)
   Test to see if the capabilities array contains a given set of
   capabilities. See the individual Capability classes for acceptable
   capability values.

   See hasCapability: for a description of the wildcard feature provided
   by this method.

   .. rubric:: Parameters:
      :name: parameters-41
      :class: method-detail-label

   -  capabilities –

      List of capabilities to test against

ServiceDescription **getServiceDescription** ()

ServiceConfig **getServiceConfig** ()

JSONObject **toJSONObject** ()

String **getServiceName** ()
   Name of the DeviceService (webOS, Chromecast, etc)

void **closeLaunchSession** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Closes the session on the first screen device. Depending on the
   sessionType, the associated service will have different ways of
   handling the close functionality.

   .. rubric:: Parameters:
      :name: parameters-42
      :class: method-detail-label

   -  launchSession –

      LaunchSession to close

   -  listener –

      (optional) listener to be called on success/failure

`PlaylistControl </apis/1-6-0/android/PlaylistControl>`__ **getPlaylistControl** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getPlaylistControlCapabilityLevel** ()

void **previous** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Jump playlist to the previous track.

   Play previous track in the playlist

   .. rubric:: Related capabilities:
      :name: related-capabilities
      :class: method-detail-label

   -  ``PlaylistControl.Previous``

   .. rubric:: Parameters:
      :name: parameters-43
      :class: method-detail-label

   -  listener –

      optional response listener

void **next** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Jump playlist to the next track.

   Play next track in the playlist

   .. rubric:: Related capabilities:
      :name: related-capabilities-1
      :class: method-detail-label

   -  ``PlaylistControl.Next``

   .. rubric:: Parameters:
      :name: parameters-44
      :class: method-detail-label

   -  listener –

      optional response listener

void **jumpToTrack** (long *index*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Jump the playlist to the designated track.

   Play a track specified by index in the playlist

   .. rubric:: Related capabilities:
      :name: related-capabilities-2
      :class: method-detail-label

   -  ``PlaylistControl.JumpToTrack``

   .. rubric:: Parameters:
      :name: parameters-45
      :class: method-detail-label

   -  index –

      index in the playlist, it starts from zero like index of array

   -  listener –

      optional response listener

void **setPlayMode** (`PlayMode </apis/1-6-0/android/PlayMode>`__ *playMode*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Set order of playing tracks

   .. rubric:: Parameters:
      :name: parameters-46
      :class: method-detail-label

   -  playMode

   -  listener –

      optional response listener

`MediaControl </apis/1-6-0/android/MediaControl>`__ **getMediaControl** ()
   Get MediaControl implementation

   .. rubric:: Returns:
      :name: returns-3
      :class: method-detail-label

   MediaControl

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getMediaControlCapabilityLevel** ()
   Get a capability priority for current implementation

   .. rubric:: Returns:
      :name: returns-4
      :class: method-detail-label

   CapabilityPriorityLevel

void **play** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Send play command.

   .. rubric:: Related capabilities:
      :name: related-capabilities-3
      :class: method-detail-label

   -  ``MediaControl.Play``

   .. rubric:: Parameters:
      :name: parameters-47
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **pause** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Send pause command.

   .. rubric:: Related capabilities:
      :name: related-capabilities-4
      :class: method-detail-label

   -  ``MediaControl.Pause``

   .. rubric:: Parameters:
      :name: parameters-48
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **stop** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Send play command.

   .. rubric:: Related capabilities:
      :name: related-capabilities-5
      :class: method-detail-label

   -  ``MediaControl.Stop``

   .. rubric:: Parameters:
      :name: parameters-49
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **rewind** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Send rewind command.

   .. rubric:: Related capabilities:
      :name: related-capabilities-6
      :class: method-detail-label

   -  ``MediaControl.Rewind``

   .. rubric:: Parameters:
      :name: parameters-50
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **fastForward** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Send play command.

   .. rubric:: Related capabilities:
      :name: related-capabilities-7
      :class: method-detail-label

   -  ``MediaControl.FastForward``

   .. rubric:: Parameters:
      :name: parameters-51
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **seek** (long *position*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Seeks to a new position within the current media item

   .. rubric:: Related capabilities:
      :name: related-capabilities-8
      :class: method-detail-label

   -  ``MediaControl.Seek``

   .. rubric:: Parameters:
      :name: parameters-52
      :class: method-detail-label

   -  position –

      The new position, in milliseconds from the beginning of the stream

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getDuration** (`DurationListener </apis/1-6-0/android/DurationListener>`__ *listener*)
   Get the current media duration in milliseconds

   .. rubric:: Parameters:
      :name: parameters-53
      :class: method-detail-label

   -  listener –

      (optional) DurationListener with methods to be called on success
      or failure

void **getPosition** (`PositionListener </apis/1-6-0/android/PositionListener>`__ *listener*)
   Get the current playback position in milliseconds

   .. rubric:: Parameters:
      :name: parameters-54
      :class: method-detail-label

   -  listener –

      (optional) PositionListener with methods to be called on success
      or failure

void **getPlayState** (`PlayStateListener </apis/1-6-0/android/PlayStateListener>`__ *listener*)
   Get the current state of playback

   .. rubric:: Parameters:
      :name: parameters-55
      :class: method-detail-label

   -  listener –

      (optional) PlayStateListener with methods to be called on success
      or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`PlayStateListener </apis/1-6-0/android/PlayStateListener>`__> **subscribePlayState** (`PlayStateListener </apis/1-6-0/android/PlayStateListener>`__ *listener*)
   Subscribe for playback state changes

   .. rubric:: Parameters:
      :name: parameters-56
      :class: method-detail-label

   -  listener –

      receives play state notifications

   .. rubric:: Returns:
      :name: returns-5
      :class: method-detail-label

   ServiceSubscription<PlayStateListener>

`MediaPlayer </apis/1-6-0/android/MediaPlayer>`__ **getMediaPlayer** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-57
      :class: method-detail-label

   -  listener –

      (optional) MediaInfoListener with methods to be called on success
      or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__> **subscribeMediaInfo** (`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-58
      :class: method-detail-label

   -  listener –

      (optional) MediaInfoListener with methods to be called on success
      or failure

void **displayImage** (`MediaInfo </apis/1-6-0/android/MediaInfo>`__ *mediaInfo*, LaunchListener *listener*)
   Display an image on the device. Not all devices support all of the
   parameters -- supply as many as you have available.

   .. rubric:: Related capabilities:
      :name: related-capabilities-9
      :class: method-detail-label

   -  ``MediaPlayer.Display.Image``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   .. rubric:: Parameters:
      :name: parameters-59
      :class: method-detail-label

   -  mediaInfo –

      Object of MediaInfo class which includes all the information about
      an image to display.

   -  listener –

      (optional) LaunchListener with methods to be called on success or
      failure

void **playMedia** (`MediaInfo </apis/1-6-0/android/MediaInfo>`__ *mediaInfo*, boolean *shouldLoop*, LaunchListener *listener*)
   Play an audio or video file on the device. Not all devices support
   all of the parameters -- supply as many as you have available.

   .. rubric:: Related capabilities:
      :name: related-capabilities-10
      :class: method-detail-label

   -  ``MediaPlayer.Play.Video``
   -  ``MediaPlayer.Play.Audio``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   .. rubric:: Parameters:
      :name: parameters-60
      :class: method-detail-label

   -  mediaInfo –

      Object of MediaInfo class which includes all the information about
      an image to display.

   -  shouldLoop –

      Whether to automatically loop playback

   -  listener –

      (optional) LaunchListener with methods to be called on success or
      failure

void **closeMedia** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Close a running media session. Because media is handled differently
   on different platforms, it is required to keep track of LaunchSession
   and MediaControl objects to control that media session in the future.
   LaunchSession will be required to close the media and mediaControl
   will be required to control the media.

   .. rubric:: Related capabilities:
      :name: related-capabilities-11
      :class: method-detail-label

   -  ``MediaPlayer.Close``

   .. rubric:: Parameters:
      :name: parameters-61
      :class: method-detail-label

   -  launchSession –

      LaunchSession object for use in closing media instance

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

`VolumeControl </apis/1-6-0/android/VolumeControl>`__ **getVolumeControl** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getVolumeControlCapabilityLevel** ()

void **volumeUp** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Sends the volume up command to the device.

   .. rubric:: Related capabilities:
      :name: related-capabilities-12
      :class: method-detail-label

   -  ``VolumeControl.UpDown``

   .. rubric:: Parameters:
      :name: parameters-62
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **volumeDown** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Sends the volume down command to the device.

   .. rubric:: Related capabilities:
      :name: related-capabilities-13
      :class: method-detail-label

   -  ``VolumeControl.UpDown``

   .. rubric:: Parameters:
      :name: parameters-63
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **setVolume** (float *volume*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Set the volume of the device.

   .. rubric:: Related capabilities:
      :name: related-capabilities-14
      :class: method-detail-label

   -  ``VolumeControl.Set``

   .. rubric:: Parameters:
      :name: parameters-64
      :class: method-detail-label

   -  volume –

      Volume as a float between 0.0 and 1.0

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getVolume** (`VolumeListener </apis/1-6-0/android/VolumeListener>`__ *listener*)
   Get the current volume of the device.

   .. rubric:: Related capabilities:
      :name: related-capabilities-15
      :class: method-detail-label

   -  ``VolumeControl.Get``

   .. rubric:: Parameters:
      :name: parameters-65
      :class: method-detail-label

   -  listener –

      (optional) VolumeListener with methods to be called on success or
      failure

void **setMute** (boolean *isMute*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Set the current volume.

   .. rubric:: Related capabilities:
      :name: related-capabilities-16
      :class: method-detail-label

   -  ``VolumeControl.Mute.Set``

   .. rubric:: Parameters:
      :name: parameters-66
      :class: method-detail-label

   -  isMute

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getMute** (`MuteListener </apis/1-6-0/android/MuteListener>`__ *listener*)
   Get the current mute state.

   .. rubric:: Related capabilities:
      :name: related-capabilities-17
      :class: method-detail-label

   -  ``VolumeControl.Mute.Get``

   .. rubric:: Parameters:
      :name: parameters-67
      :class: method-detail-label

   -  listener –

      (optional) MuteListener with methods to be called on success or
      failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`VolumeListener </apis/1-6-0/android/VolumeListener>`__> **subscribeVolume** (`VolumeListener </apis/1-6-0/android/VolumeListener>`__ *listener*)
   Subscribe to the volume on the TV.

   .. rubric:: Related capabilities:
      :name: related-capabilities-18
      :class: method-detail-label

   -  ``VolumeControl.Subscribe``

   .. rubric:: Parameters:
      :name: parameters-68
      :class: method-detail-label

   -  listener –

      (optional) VolumeListener with methods to be called on success or
      failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`MuteListener </apis/1-6-0/android/MuteListener>`__> **subscribeMute** (`MuteListener </apis/1-6-0/android/MuteListener>`__ *listener*)
   Subscribe to the mute state on the TV.

   .. rubric:: Related capabilities:
      :name: related-capabilities-19
      :class: method-detail-label

   -  ``VolumeControl.Mute.Subscribe``

   .. rubric:: Parameters:
      :name: parameters-69
      :class: method-detail-label

   -  listener –

      (optional) MuteListener with methods to be called on success or
      failure

void **onLoseReachability** (DeviceServiceReachability *reachability*)
   .. rubric:: Parameters:
      :name: parameters-70
      :class: method-detail-label

   -  reachability

void **unsubscribe** (URLServiceSubscription<?> *subscription*)
   .. rubric:: Parameters:
      :name: parameters-71
      :class: method-detail-label

   -  subscription

void **sendCommand** (ServiceCommand<?> *command*)
   .. rubric:: Parameters:
      :name: parameters-72
      :class: method-detail-label

   -  command
