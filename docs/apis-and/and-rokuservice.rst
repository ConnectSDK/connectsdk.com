RokuService
==============================================
``com.connectsdk.service.RokuService``

*extends* :doc:`DeviceService <and-deviceservice>`

RokuService provides many capabilities for Roku devices. Communication
with Roku devices occurs over HTTP.

* List, launch, & close apps
* Media playback
* Media control
* Text input control
* Key control (fiveway)

These APIs should work on all Roku devices -- they have been tested on
Roku 2, Roku 3, and Roku Streaming Stick all runnning Roku 5.3 or later.

To learn more about the Roku External Control APIs, visit the `Roku
External Control
Guide <http://sdkdocs.roku.com/display/sdkdoc/External+Control+Guide>`__.

Properties
----------

final String ID = "Roku"


Inner Classes
-------------

* RokuLaunchSession


Methods
-------

static void **registerApp** (String *appId*)

    **Parameters:**
        * appId

static DiscoveryFilter **discoveryFilter** ()

**RokuService** (ServiceDescription *serviceDescription*, ServiceConfig *serviceConfig*)

    **Parameters:**
        * serviceDescription
        * serviceConfig

void **setServiceDescription** (ServiceDescription *serviceDescription*)

     **Parameters:**
         * serviceDescription


:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPriorityLevel** (Class<?extends CapabilityMethods > *clazz*)

    **Parameters:**
        * clazz

:doc:`Launcher <and-launcher>` **getLauncher** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getLauncherCapabilityLevel** ()

void **launchApp** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener* )

    **Parameters:**
        * appId
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchAppWithInfo** ( :doc:`AppInfo <and-appinfo>` *appInfo*, :doc:`Launcher <and-launcher>`. :doc:`AppLaunchListener <and-applaunchlistener>` *listener* )

    **Parameters:**
        * appInfo
        * listener – (optional) Launcher.AppLaunchListener with methods to be called on success or failure

void **launchAppWithInfo** (final :doc:`AppInfo <and-appinfo>` *appInfo* , Object *params*, final :doc:`Launcher <and-launcher>`. :doc:`AppLaunchListener <and-applaunchlistener>` *listener* )

    **Parameters:**
        * appInfo
        * params
        * listener – (optional) final Launcher.AppLaunchListener with methods to be called on success or failure

void **closeApp** ( :doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener* )

    **Parameters:**
        * launchSession
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getAppList** (final :doc:`AppListListener <and-applistlistener>` *listener*)

     **Parameters:**
         * listener – (optional) final AppListListener with methods to be called on success or failure

void **getRunningApp** ( :doc:`AppInfoListener <and-appinfolistener>` *listener* )

    **Parameters:**
        * listener – (optional) AppInfoListener with methods to be called on success or failure


:doc:`ServiceSubscription <and-servicesubscription>` < :doc:`AppInfoListener <and-appinfolistener>` >
**subscribeRunningApp** ( :doc:`AppInfoListener <and-appinfolistener>` *listener* )

    **Parameters:**
        * listener – (optional) AppInfoListener with methods to be called on success or failure



void **getAppState** ( :doc:`LaunchSession <and-launchsession>` *launchSession*,
:doc:`AppStateListener <and-appstatelistener>` *listener* )

     **Parameters:**
         * listener – (optional) AppStateListener with methods to be called on success or failure



:doc:`ServiceSubscription <and-servicesubscription>` < :doc:`AppStateListener <and-appstatelistener>` > **subscribeAppState**
( :doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`AppStateListener <and-appstatelistener>` *listener* )

    **Parameters:**
        * launchSession
        * listener – (optional) AppStateListener with methods to be called on success or failure



void **launchBrowser** (String *url*, :doc:`Launcher <and-launcher>`. :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * url
        * listener – (optional) Launcher.AppLaunchListener with methods to be called on success or failure



void **launchYouTube** (String *contentId*, :doc:`Launcher <and-launcher>`. :doc:`AppLaunchListener <and-applaunchlistener>` *listener* )

    **Parameters:**
        * contentId
        * listener – (optional) Launcher.AppLaunchListener with methods to be called on success or failure


void **launchYouTube** (String *contentId*, float *startTime*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * contentId
        * startTime
        * listener – (optional) AppLaunchListener with methods to be called on success or failure


void **launchNetflix** (final String *contentId*, final :doc:`Launcher <and-launcher>`. :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * contentId
        * listener – (optional) final Launcher.AppLaunchListener with methods to be called on success or failure


void **launchHulu** (final String *contentId*, final :doc:`Launcher <and-launcher>`. :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
           * contentId
           * listener – (optional) final Launcher.AppLaunchListener with methods to be called on success or failure


void **launchAppStore** (final String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * appId
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

:doc:`KeyControl <and-keycontrol>` **getKeyControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getKeyControlCapabilityLevel** ()

void **up** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **down** (final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

void **left** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **right** ( :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **ok** (final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

void **back** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **home** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`MediaControl <and-mediacontrol>` **getMediaControl** ()

    Get MediaControl implementation

    **Returns:** MediaControl

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaControlCapabilityLevel** ()

    Get a capability priority for current implementation

    **Returns:** CapabilityPriorityLevel

void **play** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **pause** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **stop** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **rewind** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **fastForward** ( :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **previous** ( :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    This method is deprecated. Use ``PlaylistControl::previous(ResponseListener<Object> listener)`` instead.

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **next** ( :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    This method is deprecated. Use ``PlaylistControl::next(ResponseListener<Object> listener)`` instead.

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getDuration** (:doc:`DurationListener <and-durationlistener>` *listener*)

    Get the current media duration in milliseconds

    **Parameters:**
        * listener – (optional) DurationListener with methods to be called on success or failure

void **getPosition** (:doc:`PositionListener <and-positionlistener>` *listener*)

    Get the current playback position in milliseconds

    **Parameters:**
        * listener – (optional) PositionListener with methods to be called on success or failure

void **seek** (long *position*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * position – The new position, in milliseconds from the beginning of the stream
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MediaInfoListener <and-mediainfolistener>`>
**subscribeMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

void **displayImage** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*,
:doc:`MediaPlayer <and-mediaplayer>`.LaunchListener *listener*)

    **Parameters:**
        * url
        * mimeType
        * title
        * description
        * iconSrc
        * listener – (optional) MediaPlayer.LaunchListener with methods to be called on success or failure

void **displayImage** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, :doc:`MediaPlayer <and-mediaplayer>`.LaunchListener *listener*)

    **Parameters:**
        * mediaInfo
        * listener – (optional) MediaPlayer.LaunchListener with methods to be called on success or failure

void **playMedia** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, boolean *shouldLoop*,
:doc:`MediaPlayer <and-mediaplayer>`.LaunchListener *listener*)

    **Parameters:**
       * url
       * mimeType
       * title
       * description
       * iconSrc
       * shouldLoop
       * listener – (optional) MediaPlayer.LaunchListener with methods to be called on success or failure

void **playMedia** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, boolean *shouldLoop*, :doc:`MediaPlayer <and-mediaplayer>`.LaunchListener *listener*)

    **Parameters:**
        * mediaInfo
        * shouldLoop
        * listener – (optional) MediaPlayer.LaunchListener with methods to be called on success or failure

void **closeMedia** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * launchSession
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`TextInputControl <and-textinputcontrol>` **getTextInputControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getTextInputControlCapabilityLevel** ()

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`TextInputStatusListener <and-textinputstatuslistener>`>
**subscribeTextInputStatus** (:doc:`TextInputStatusListener <and-textinputstatuslistener>` *listener*)

    **Parameters:**
        * listener – (optional) TextInputStatusListener with methods to be called on success or failure

void **sendText** (String *input*)

    **Parameters:**
        * input

void **sendKeyCode** (:doc:`KeyCode <and-keycode>` *keyCode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * keyCode
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **sendEnter** ()

void **sendDelete** ()

void **unsubscribe** (URLServiceSubscription<?> *subscription*)

    **Parameters:**
        * subscription

void **sendCommand** (final ServiceCommand<?> *mCommand*)

    **Parameters:**
        * mCommand

void **getPlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)

    Get the current state of playback

    **Parameters:**
        * listener – (optional) PlayStateListener with methods to be called on success or failure


:doc:`ServiceSubscription <and-servicesubscription>` < :doc:`PlayStateListener <and-playstatelistener>`> **subscribePlayState** ( :doc:`PlayStateListener <and-playstatelistener>` *listener*)

    Subscribe for playback state changes

    **Parameters:**
        * listener – receives play state notifications

    **Returns:** ServiceSubscription<PlayStateListener>

boolean **isConnectable** ()

boolean **isConnected** ()

void **connect** ()

void **disconnect** ()

void **onLoseReachability** (DeviceServiceReachability *reachability*)

    **Parameters:**
        * reachability

:doc:`DIALService <and-dialservice>` **getDIALService** ()

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
        * pairingKey – Data to be used for pairing. The type of this parameter will vary depending on what type of pairing is required, but is likely to be a string (pin code, pairing key, etc).

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
        * capability – Capability to test against

boolean **hasAnyCapability** (String... *capabilities*)
    Test to see if the capabilities array contains at least one
    capability in a given set of capabilities. See the individual
    Capability classes for acceptable capability values.

    See hasCapability: for a description of the wildcard feature provided by this method.

    **Parameters:**
        * capabilities – Set of capabilities to test against

boolean **hasCapabilities** (List<String> *capabilities*)

    Test to see if the capabilities array contains a given set of
    capabilities. See the individual Capability classes for acceptable
    capability values.

    See hasCapability: for a description of the wildcard feature provided
    by this method.

    **Parameters:**
        * capabilities – List of capabilities to test against

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
        * launchSession – LaunchSession to close
        * listener – (optional) listener to be called on success/failure

:doc:`Launcher <and-launcher>` **getLauncher** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getLauncherCapabilityLevel** ()

void **launchAppWithInfo** (:doc:`AppInfo <and-appinfo>` *appInfo*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    Launch an application on the device.

    **Related capabilities:**
        * ``Launcher.App``
        * ``Launcher.App.Params`` – if launching with params

    **Parameters:**
        * appInfo – AppInfo object for the application
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchApp** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    Launch an application on the device.

    **Related capabilities:**
        * ``Launcher.App``

    **Parameters:**
        * appId – ID of the application
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **closeApp** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Close an application on the device.

    **Related capabilities:**
        * ``Launcher.App.Close``

    **Parameters:**
        * launchSession – LaunchSession of the target app
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getAppList** (:doc:`AppListListener <and-applistlistener>` *listener*)

    Gets a list of all apps installed on the device.

    **Related capabilities:**
        * ``Launcher.App.List``

    **Parameters:**
        * listener – (optional) AppListListener with methods to be called on success or failure

void **getRunningApp** (:doc:`AppInfoListener <and-appinfolistener>` *listener*)

    Gets an AppInfo object for the current running app on the device.

    **Related capabilities:**
        * ``Launcher.RunningApp``

    **Parameters:**
        * listener – (optional) AppInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppInfoListener <and-appinfolistener>`>
**subscribeRunningApp** (:doc:`AppInfoListener <and-appinfolistener>` *listener*)

    Subscribes to changes of the current running app. Every time the
    running app changes, the success block will be called with an AppInfo
    object for the current running app.

    **Related capabilities:**
        * ``Launcher.RunningApp.Subscribe``

    **Parameters:**
        * listener – (optional) AppInfoListener with methods to be called on success or failure

void **getAppState** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`AppStateListener <and-appstatelistener>` *listener*)

    Gets the target app's running status and on-screen visibility.

    **Related capabilities:**
        * ``Launcher.AppState``

    **Parameters:**
        * launchSession – LaunchSession of the target app
        * listener – (optional) AppStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppStateListener <and-appstatelistener>`>
**subscribeAppState** (:doc:`LaunchSession <and-launchsession>` *launchSession*,
:doc:`AppStateListener <and-appstatelistener>` *listener*)

    Subscribes to changes of the state of the target app. Every time the
    app's state changes, the success block will be called with info on
    the app's running status and on-screen visibility.

    **Related capabilities:**
        * ``Launcher.AppState.Subscribe``

    **Parameters:**
        * launchSession – LaunchSession of the target app
        * listener – (optional) AppStateListener with methods to be called on success or failure

void **launchBrowser** (String *url*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    Launch the web browser. Will launch deep-linked to provided URL, if
    supported on the target platform.

    **Related capabilities:**
        * ``Launcher.Browser``
        * ``Launcher.Browser.Params`` – if launching with url

    **Parameters:**
        * url
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchYouTube** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    Launch YouTube app. Will launch deep-linked to provided contentId, if
    supported on the target platform.

    **Related capabilities:**
        * ``Launcher.YouTube``
        * ``Launcher.YouTube.Params`` – if launching with contentId

    **Parameters:**
        * contentId – Video id to open
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchNetflix** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    Launch Netflix app. Will launch deep-linked to provided contentId, if supported on the target platform.

    **Related capabilities:**
        * ``Launcher.Netflix``
        * ``Launcher.Netflix.Params`` – if launching with contentId

    **Parameters:**
        * contentId – Video id to open
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchHulu** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    Launch Hulu app. Will launch deep-linked to provided contentId, if supported on the target platform.

    **Related capabilities:**
        * ``Launcher.Hulu``
        * ``Launcher.Hulu.Params`` – if launching with contentId

    **Parameters:**
        * contentId – Video id to open
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchAppStore** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    Launch the device's app store app, optionally deep-linked to a specific app's page.

    **Related capabilities:**
        * ``Launcher.AppStore``
        * ``Launcher.AppStore.Params``

    **Parameters:**
        * appId – (optional) ID of the application to show in the app store
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MediaInfoListener <and-mediainfolistener>`>
**subscribeMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

void **displayImage** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, LaunchListener *listener*)

    Display an image on the device. Not all devices support all of the parameters -- supply as many as you have available.

    **Related capabilities:**
        * ``MediaPlayer.Display.Image``
        * ``MediaPlayer.MediaData.Title``
        * ``MediaPlayer.MediaData.Description``
        * ``MediaPlayer.MediaData.Thumbnail``
        * ``MediaPlayer.MediaData.MimeType``

    **Parameters:**
        * mediaInfo – Object of MediaInfo class which includes all the information about an image to display.
        * listener – (optional) LaunchListener with methods to be called on success or failure

void **playMedia** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, boolean *shouldLoop*, LaunchListener *listener*)

    Play an audio or video file on the device. Not all devices support all of the parameters -- supply as many as you have available.

    **Related capabilities:**
        * ``MediaPlayer.Play.Video``
        * ``MediaPlayer.Play.Audio``
        * ``MediaPlayer.MediaData.Title``
        * ``MediaPlayer.MediaData.Description``
        * ``MediaPlayer.MediaData.Thumbnail``
        * ``MediaPlayer.MediaData.MimeType``

    **Parameters:**
        * mediaInfo – Object of MediaInfo class which includes all the information about an image to display.
        * shouldLoop – Whether to automatically loop playback
        * listener – (optional) LaunchListener with methods to be called on success or failure

void **closeMedia** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Close a running media session. Because media is handled differently
    on different platforms, it is required to keep track of LaunchSession
    and MediaControl objects to control that media session in the future.
    LaunchSession will be required to close the media and mediaControl
    will be required to control the media.

    **Related capabilities:**
        * ``MediaPlayer.Close``

    **Parameters:**
        * launchSession – LaunchSession object for use in closing media instance
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`MediaControl <and-mediacontrol>` **getMediaControl** ()

    Get MediaControl implementation

    **Returns:** MediaControl

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaControlCapabilityLevel** ()

    Get a capability priority for current implementation

    **Returns:** CapabilityPriorityLevel

void **play** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Send play command.

    **Related capabilities:**
        * ``MediaControl.Play``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **pause** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Send pause command.

    **Related capabilities:**
        * ``MediaControl.Pause``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **stop** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Send play command.

    **Related capabilities:**
        * ``MediaControl.Stop``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **rewind** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Send rewind command.

    **Related capabilities:**
        * ``MediaControl.Rewind``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **fastForward** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Send play command.

    **Related capabilities:**
        * ``MediaControl.FastForward``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **previous** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    This method is deprecated. Use ``PlaylistControl::previous(ResponseListener<Object> listener)`` instead.

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **next** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    This method is deprecated. Use ``PlaylistControl::next(ResponseListener<Object> listener)`` instead.

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **seek** (long *position*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Seeks to a new position within the current media item

    **Related capabilities:**
        * ``MediaControl.Seek``

    **Parameters:**
        * position – The new position, in milliseconds from the beginning of the stream
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getDuration** (:doc:`DurationListener <and-durationlistener>` *listener*)

    Get the current media duration in milliseconds

    **Parameters:**
         * listener – (optional) DurationListener with methods to be called on success or failure

void **getPosition** (:doc:`PositionListener <and-positionlistener>` *listener*)

    Get the current playback position in milliseconds

    **Parameters:**
        * listener – (optional) PositionListener with methods to be called on success or failure

void **getPlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)

    Get the current state of playback

    **Parameters:**
        * listener – (optional) PlayStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`PlayStateListener <and-playstatelistener>` > **subscribePlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)

    Subscribe for playback state changes

    **Parameters:**
        * listener – receives play state notifications

    **Returns:** ServiceSubscription<PlayStateListener>

:doc:`KeyControl <and-keycontrol>` **getKeyControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getKeyControlCapabilityLevel** ()

void **up** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends the up button key code to the TV.

    **Related capabilities:**
        * ``KeyControl.Up``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **down** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends the down button key code to the TV.

    **Related capabilities:**
        * ``KeyControl.Down``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **left** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends the left button key code to the TV.

    **Related capabilities:**
        * ``KeyControl.Left``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **right** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends the right button key code to the TV.

    **Related capabilities:**
        * ``KeyControl.Right``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **ok** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends the OK button key code to the TV.

    **Related capabilities:**
        * ``KeyControl.OK``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **back** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends the back button key code to the TV.

    **Related capabilities:**
        * ``KeyControl.Back``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **home** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends the home button key code to the TV.

    **Related capabilities:**
        * ``KeyControl.Home``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **sendKeyCode** (:doc:`KeyCode <and-keycode>` *keycode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends a key code value to the TV.

    **Related capabilities:**
        * ``KeyControl.Send.KeyCode``

    **Parameters:**
        * keycode
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`TextInputControl <and-textinputcontrol>` **getTextInputControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getTextInputControlCapabilityLevel** ()

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`TextInputStatusListener <and-textinputstatuslistener>`>
**subscribeTextInputStatus** (:doc:`TextInputStatusListener <and-textinputstatuslistener>` *listener*)

    Subscribe to information about the current text field.

    **Related capabilities:**
        * ``TextInputControl.Subscribe``

    **Parameters:**
        * listener – (optional) TextInputStatusListener with methods to be called on success or failure

void **sendText** (String *input*)

    Send text to the current text field.

    **Related capabilities:**
        * ``TextInputControl.Send.Text``

    **Parameters:**
        * input

void **sendEnter** ()

    Send enter key to the current text field.

    **Related capabilities:**
        * ``TextInputControl.Send.Enter``

void **sendDelete** ()

    Send delete event to the current text field.

    **Related capabilities:**
        * ``TextInputControl.Send.Delete``

void **onLoseReachability** (DeviceServiceReachability *reachability*)

    **Parameters:**
        * reachability

void **unsubscribe** (URLServiceSubscription<?> *subscription*)

    **Parameters:**
        * subscription

void **sendCommand** (ServiceCommand<?> *command*)

    **Parameters:**
        * command
