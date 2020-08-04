FireTVService com.connectsdk.service.FireTVService
==================================================

*extends*\ `DeviceService </apis/1-6-0/android/DeviceService>`__

FireTVService provides capabilities for FireTV devices. FireTVService
acts as a layer on top of Fling SDK, and requires the Fling SDK library
to function. FireTVService provides the following functionality:

-  Media playback

-  Media control

Using Connect SDK for discovery/control of FireTV devices will result in
your app complying with the Fling SDK terms of service.

Properties
----------

final String ID = "FireTV"

Inner Classes
-------------

-  ConvertResult
-  PlayStateSubscription
-  Subscription

Methods
-------

**FireTVService** (ServiceDescription *serviceDescription*, ServiceConfig *serviceConfig*)
   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  serviceDescription
   -  serviceConfig

void **connect** ()
   Prepare a service for usage

boolean **isConnected** ()
   Check if service is ready

boolean **isConnectable** ()
   Check if service implements connect/disconnect methods

void **disconnect** ()
   Disconnect a service and close all subscriptions

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getPriorityLevel** (Class<?extends CapabilityMethods > *clazz*)
   Get a priority level for a particular capability

   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  clazz

`MediaPlayer </apis/1-6-0/android/MediaPlayer>`__ **getMediaPlayer** ()
   Get MediaPlayer implementation

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getMediaPlayerCapabilityLevel** ()
   Get MediaPlayer priority level

void **getMediaInfo** (final `MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__ *listener*)
   Get MediaInfo available only during playback otherwise returns an
   error

   .. rubric:: Parameters:
      :name: parameters-2
      :class: method-detail-label

   -  listener –

      (optional) final MediaInfoListener with methods to be called on
      success or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__> **subscribeMediaInfo** (`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__ *listener*)
   Not supported

   .. rubric:: Parameters:
      :name: parameters-3
      :class: method-detail-label

   -  listener –

      (optional) MediaInfoListener with methods to be called on success
      or failure

void **displayImage** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, final LaunchListener *listener*)
   Display an image with metadata

   .. rubric:: Parameters:
      :name: parameters-4
      :class: method-detail-label

   -  url –

      media source

   -  mimeType

   -  title

   -  description

   -  iconSrc

   -  listener –

      (optional) final LaunchListener with methods to be called on
      success or failure

void **playMedia** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, boolean *shouldLoop*, LaunchListener *listener*)
   Play audio/video

   .. rubric:: Parameters:
      :name: parameters-5
      :class: method-detail-label

   -  url –

      media source

   -  mimeType

   -  title

   -  description

   -  iconSrc

   -  shouldLoop –

      skipped in current implementation

   -  listener –

      (optional) LaunchListener with methods to be called on success or
      failure

void **closeMedia** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, final `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Stop and close media player on FireTV. In current implementation it's
   similar to stop method

   .. rubric:: Parameters:
      :name: parameters-6
      :class: method-detail-label

   -  launchSession

   -  listener –

      (optional) final ResponseListener< Object > with methods to be
      called on success or failure

void **displayImage** (`MediaInfo </apis/1-6-0/android/MediaInfo>`__ *mediaInfo*, LaunchListener *listener*)
   Display an image with metadata

   .. rubric:: Parameters:
      :name: parameters-7
      :class: method-detail-label

   -  mediaInfo

   -  listener –

      (optional) LaunchListener with methods to be called on success or
      failure

void **playMedia** (`MediaInfo </apis/1-6-0/android/MediaInfo>`__ *mediaInfo*, boolean *shouldLoop*, LaunchListener *listener*)
   Play audio/video

   .. rubric:: Parameters:
      :name: parameters-8
      :class: method-detail-label

   -  mediaInfo

   -  shouldLoop –

      skipped in current implementation

   -  listener –

      (optional) LaunchListener with methods to be called on success or
      failure

`MediaControl </apis/1-6-0/android/MediaControl>`__ **getMediaControl** ()
   Get MediaControl capability. It should be used only during media
   playback.

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getMediaControlCapabilityLevel** ()
   Get MediaControl priority level

void **play** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Play current media.

   .. rubric:: Parameters:
      :name: parameters-9
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **pause** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Pause current media.

   .. rubric:: Parameters:
      :name: parameters-10
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **stop** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Stop current media and close FireTV application.

   .. rubric:: Parameters:
      :name: parameters-11
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **rewind** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Not supported

   .. rubric:: Parameters:
      :name: parameters-12
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **fastForward** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Not supported

   .. rubric:: Parameters:
      :name: parameters-13
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **previous** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Not supported

   .. rubric:: Parameters:
      :name: parameters-14
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **next** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Not supported

   .. rubric:: Parameters:
      :name: parameters-15
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **seek** (long *position*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Seek current media.

   .. rubric:: Parameters:
      :name: parameters-16
      :class: method-detail-label

   -  position –

      time in milliseconds

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getDuration** (final `DurationListener </apis/1-6-0/android/DurationListener>`__ *listener*)
   Get current media duration.

   .. rubric:: Parameters:
      :name: parameters-17
      :class: method-detail-label

   -  listener –

      (optional) final DurationListener with methods to be called on
      success or failure

void **getPosition** (final `PositionListener </apis/1-6-0/android/PositionListener>`__ *listener*)
   Get playback position

   .. rubric:: Parameters:
      :name: parameters-18
      :class: method-detail-label

   -  listener –

      (optional) final PositionListener with methods to be called on
      success or failure

void **getPlayState** (final `PlayStateListener </apis/1-6-0/android/PlayStateListener>`__ *listener*)
   Get playback state

   .. rubric:: Parameters:
      :name: parameters-19
      :class: method-detail-label

   -  listener –

      (optional) final PlayStateListener with methods to be called on
      success or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`PlayStateListener </apis/1-6-0/android/PlayStateListener>`__> **subscribePlayState** (final `PlayStateListener </apis/1-6-0/android/PlayStateListener>`__ *listener*)
   Subscribe to playback state. Only single instance of subscription is
   available. Each new call returns the same subscription object.

   .. rubric:: Parameters:
      :name: parameters-20
      :class: method-detail-label

   -  listener –

      (optional) final PlayStateListener with methods to be called on
      success or failure

static DiscoveryFilter **discoveryFilter** ()
   Get filter instance for this service which contains a name of service
   and id. It is used in discovery process

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
      :name: parameters-21
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
      :name: parameters-22
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
      :name: parameters-23
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
      :name: parameters-24
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
      :name: parameters-25
      :class: method-detail-label

   -  launchSession –

      LaunchSession to close

   -  listener –

      (optional) listener to be called on success/failure

`MediaPlayer </apis/1-6-0/android/MediaPlayer>`__ **getMediaPlayer** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-26
      :class: method-detail-label

   -  listener –

      (optional) MediaInfoListener with methods to be called on success
      or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__> **subscribeMediaInfo** (`MediaInfoListener </apis/1-6-0/android/MediaInfoListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-27
      :class: method-detail-label

   -  listener –

      (optional) MediaInfoListener with methods to be called on success
      or failure

void **displayImage** (`MediaInfo </apis/1-6-0/android/MediaInfo>`__ *mediaInfo*, LaunchListener *listener*)
   Display an image on the device. Not all devices support all of the
   parameters -- supply as many as you have available.

   .. rubric:: Related capabilities:
      :name: related-capabilities
      :class: method-detail-label

   -  ``MediaPlayer.Display.Image``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   .. rubric:: Parameters:
      :name: parameters-28
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
      :name: related-capabilities-1
      :class: method-detail-label

   -  ``MediaPlayer.Play.Video``
   -  ``MediaPlayer.Play.Audio``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   .. rubric:: Parameters:
      :name: parameters-29
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
      :name: related-capabilities-2
      :class: method-detail-label

   -  ``MediaPlayer.Close``

   .. rubric:: Parameters:
      :name: parameters-30
      :class: method-detail-label

   -  launchSession –

      LaunchSession object for use in closing media instance

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
   Send play command.

   .. rubric:: Related capabilities:
      :name: related-capabilities-3
      :class: method-detail-label

   -  ``MediaControl.Play``

   .. rubric:: Parameters:
      :name: parameters-31
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
      :name: parameters-32
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
      :name: parameters-33
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
      :name: parameters-34
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
      :name: parameters-35
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **previous** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   This method is deprecated. Use
   ``PlaylistControl::previous(ResponseListener<Object> listener)``
   instead.

   .. rubric:: Parameters:
      :name: parameters-36
      :class: method-detail-label

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **next** (`ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   This method is deprecated. Use
   ``PlaylistControl::next(ResponseListener<Object> listener)`` instead.

   .. rubric:: Parameters:
      :name: parameters-37
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
      :name: parameters-38
      :class: method-detail-label

   -  position –

      The new position, in milliseconds from the beginning of the stream

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getDuration** (`DurationListener </apis/1-6-0/android/DurationListener>`__ *listener*)
   Get the current media duration in milliseconds

   .. rubric:: Parameters:
      :name: parameters-39
      :class: method-detail-label

   -  listener –

      (optional) DurationListener with methods to be called on success
      or failure

void **getPosition** (`PositionListener </apis/1-6-0/android/PositionListener>`__ *listener*)
   Get the current playback position in milliseconds

   .. rubric:: Parameters:
      :name: parameters-40
      :class: method-detail-label

   -  listener –

      (optional) PositionListener with methods to be called on success
      or failure

void **getPlayState** (`PlayStateListener </apis/1-6-0/android/PlayStateListener>`__ *listener*)
   Get the current state of playback

   .. rubric:: Parameters:
      :name: parameters-41
      :class: method-detail-label

   -  listener –

      (optional) PlayStateListener with methods to be called on success
      or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`PlayStateListener </apis/1-6-0/android/PlayStateListener>`__> **subscribePlayState** (`PlayStateListener </apis/1-6-0/android/PlayStateListener>`__ *listener*)
   Subscribe for playback state changes

   .. rubric:: Parameters:
      :name: parameters-42
      :class: method-detail-label

   -  listener –

      receives play state notifications

   .. rubric:: Returns:
      :name: returns-2
      :class: method-detail-label

   ServiceSubscription<PlayStateListener>

void **onLoseReachability** (DeviceServiceReachability *reachability*)
   .. rubric:: Parameters:
      :name: parameters-43
      :class: method-detail-label

   -  reachability

void **unsubscribe** (URLServiceSubscription<?> *subscription*)
   .. rubric:: Parameters:
      :name: parameters-44
      :class: method-detail-label

   -  subscription

void **sendCommand** (ServiceCommand<?> *command*)
   .. rubric:: Parameters:
      :name: parameters-45
      :class: method-detail-label

   -  command
