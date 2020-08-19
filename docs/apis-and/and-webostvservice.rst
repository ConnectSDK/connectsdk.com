WebOSTVService
====================================================

``com.connectsdk.service.WebOSTVService``

*extends* :doc:`DeviceService <and-deviceservice>`

WebOSTVService provides capabilities for LG Smart TVs running webOS
(model year 2014). The second screen gateway running on the webOS
provides different capabilities based on whether pairing is enabled or
not.

 * Web app launching & two-way communication
 * App launching
 * Media playback
 * Media control
 * Volume control
 * Text input control\*
 * Key control (fiveway)\*
 * Mouse control\*
 * Power control\*
 * TV control (change channels, get channel info)\*
 * External input control\*
 * Toast control\*

\* = requires pairing

Commands & subscriptions on webOS occur over a WebSocket connection.

webOS Version History
---------------------

The following version numbers represent the version of webOS released
for LG Smart TVs. The version numbers are associated with any changes to
the platform's second screen APIs in that particular version.

4.0.0
 * Initial release

4.0.1
 * No changes

4.0.2
 * Added app-to-app support
 * Added the ability to request pin or prompt pairing

4.0.3
 * Fixed a subscription bug in app-to-app

Properties
----------

**final String ID**
= "webOS TV"

**final String[] kWebOSTVServiceOpenPermissions**
= { "LAUNCH", "LAUNCH_WEBAPP", "APP_TO_APP", "CONTROL_AUDIO", "CONTROL_INPUT_MEDIA_PLAYBACK" }

**final String[] kWebOSTVServiceProtectedPermissions**
= { "CONTROL_POWER", "READ_INSTALLED_APPS", "CONTROL_DISPLAY", "CONTROL_INPUT_JOYSTICK", "CONTROL_INPUT_MEDIA_RECORDING", "CONTROL_INPUT_TV", "READ_INPUT_DEVICE_LIST", "READ_NETWORK_STATE", "READ_TV_CHANNEL_LIST", "WRITE_NOTIFICATION_TOAST" }

**final String[] kWebOSTVServicePersonalActivityPermissions**
= { "CONTROL_INPUT_TEXT", "CONTROL_MOUSE_AND_KEYBOARD", "READ_CURRENT_CHANNEL", "READ_RUNNING_APPS" }

Inner Classes
-------------

 * ACRAuthTokenListener
 * LaunchPointsListener
 * SecureAccessTestListener
 * ServiceInfoListener
 * SystemInfoListener
 * WebOSTVServicePermission

Methods
-------

**WebOSTVService** (ServiceDescription *serviceDescription*, ServiceConfig *serviceConfig*)

    **Parameters:**
        * serviceDescription
        * serviceConfig

void **setPairingType** (:doc:`PairingType <and-pairingtype>` *pairingType*)

    **Parameters:**
        * pairingType

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPriorityLevel** (Class<?extends CapabilityMethods > *clazz*)

    **Parameters:**
        * clazz

void **setServiceDescription** (ServiceDescription *serviceDescription*)

    **Parameters:**
        * serviceDescription

boolean **isConnected** ()

void **connect** ()

void **disconnect** ()

void **cancelPairing** ()

:doc:`Launcher <and-launcher>` **getLauncher** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getLauncherCapabilityLevel** ()

void **launchApp** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * appId
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchAppWithInfo** (:doc:`AppInfo <and-appinfo>` *appInfo*, :doc:`Launcher <and-launcher>`.\ :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * appInfo
        * listener – (optional) Launcher.AppLaunchListener with methods to be called on success or failure

void **launchAppWithInfo** (final :doc:`AppInfo <and-appinfo>` *appInfo*, Object *params*, final :doc:`Launcher <and-launcher>`.\ :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * appInfo
        * params
        * listener – (optional) final Launcher.AppLaunchListener with methods to be called on success or failure

void **launchBrowser** (String *url*, final :doc:`Launcher <and-launcher>`.\ :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * url
        * listener – (optional) final Launcher.AppLaunchListener with methods to be called on success or failure

void **launchYouTube** (String *contentId*, :doc:`Launcher <and-launcher>`.\ :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * contentId
        * listener – (optional) Launcher.AppLaunchListener with methods to be called on success or failure

void **launchYouTube** (final String *contentId*, float *startTime*, final :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * contentId
        * startTime
        * listener – (optional) final AppLaunchListener with methods to be called on success or failure

void **launchHulu** (String *contentId*, :doc:`Launcher <and-launcher>`.\ :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * contentId
        * listener – (optional) Launcher.AppLaunchListener with methods to be called on success or failure

void **launchNetflix** (String *contentId*, :doc:`Launcher <and-launcher>`.\ :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * contentId
        * listener – (optional) Launcher.AppLaunchListener with methods to be called on success or failure

void **launchAppStore** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * appId
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **closeApp** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * launchSession
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getAppList** (final :doc:`AppListListener <and-applistlistener>` *listener*)

    **Parameters:**
        * listener – (optional) final AppListListener with methods to be called on success or failure

void **getRunningApp** (:doc:`AppInfoListener <and-appinfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) AppInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppInfoListener <and-appinfolistener>`> **subscribeRunningApp** (:doc:`AppInfoListener <and-appinfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) AppInfoListener with methods to be called on success or failure

void **getAppState** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`AppStateListener <and-appstatelistener>` *listener*)

    **Parameters:**
        * launchSession
        * listener – (optional) AppStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppStateListener <and-appstatelistener>`> **subscribeAppState** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`AppStateListener <and-appstatelistener>` *listener*)

    **Parameters:**
        * launchSession
        * listener – (optional) AppStateListener with methods to be called on success or failure

:doc:`ToastControl <and-toastcontrol>` **getToastControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getToastControlCapabilityLevel** ()

void **showToast** (String *message*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * message
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showToast** (String *message*, String *iconData*, String *iconExtension*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * message
        * iconData
        * iconExtension
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForApp** (String *message*, :doc:`AppInfo <and-appinfo>` *appInfo*, JSONObject *params*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * message
        * appInfo
        * params
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForApp** (String *message*, :doc:`AppInfo <and-appinfo>` *appInfo*, JSONObject *params*, String *iconData*, String *iconExtension*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * message
        * appInfo
        * params
        * iconData
        * iconExtension
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForURL** (String *message*, String *url*, `ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * message
        * url
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForURL** (String *message*, String *url*, String *iconData*, String *iconExtension*, `ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * message
        * url
        * iconData
        * iconExtension
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`VolumeControl <and-volumecontrol>` **getVolumeControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getVolumeControlCapabilityLevel** ()

void **volumeUp** ()

void **volumeUp** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **volumeDown** ()

void **volumeDown** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **setVolume** (int *volume*)

    **Parameters:**
        * volume

void **setVolume** (float *volume*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * volume
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getVolume** (:doc:`VolumeListener <and-volumelistener>` *listener*)

    **Parameters:**
        * listener – (optional) VolumeListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`VolumeListener <and-volumelistener>`> **subscribeVolume** (:doc:`VolumeListener <and-volumelistener>` *listener*)

    **Parameters:**
        * listener – (optional) VolumeListener with methods to be called on success or failure

void **setMute** (boolean *isMute*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * isMute
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getMute** (:doc:`MuteListener <and-mutelistener>` *listener*)

    **Parameters:**
        * listener – (optional) MuteListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MuteListener <and-mutelistener>`> **subscribeMute** (:doc:`MuteListener <and-mutelistener>` *listener*)

    **Parameters:**
        * listener – (optional) MuteListener with methods to be called on success or failure

void **getVolumeStatus** (:doc:`VolumeStatusListener <and-volumestatuslistener>` *listener*)

    **Parameters:**
        * listener – (optional) VolumeStatusListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`VolumeStatusListener <and-volumestatuslistener>`> **subscribeVolumeStatus** (:doc:`VolumeStatusListener <and-volumestatuslistener>` *listener*)

    **Parameters:**
        * listener – (optional) VolumeStatusListener with methods to be called on success or failure

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MediaInfoListener <and-mediainfolistener>`> **subscribeMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

void **displayImage** (final String *url*, final String *mimeType*, final String *title*, final String *description*, final String *iconSrc*, final :doc:`MediaPlayer <and-mediaplayer>`.LaunchListener *listener*)

    **Parameters:**
        * url
        * mimeType
        * title
        * description
        * iconSrc
        * listener – (optional) final MediaPlayer.LaunchListener with methods to be called on success or failure

void **displayImage** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, :doc:`MediaPlayer <and-mediaplayer>`.LaunchListener *listener*)

    **Parameters:**
        * mediaInfo
        * listener – (optional) MediaPlayer.LaunchListener with methods to be called on success or failure

void **playMedia** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, boolean *shouldLoop*, :doc:`MediaPlayer <and-mediaplayer>`.LaunchListener *listener*)

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

void **fastForward** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called onsuccess or failure

void **previous** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    This method is deprecated. Use ``PlaylistControl::previous(ResponseListener<Object> listener)`` instead.

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **next** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    This method is deprecated. Use ``PlaylistControl::next(ResponseListener<Object> listener)`` instead.

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **seek** (long *position*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

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

:doc:`TVControl <and-tvcontrol>` **getTVControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getTVControlCapabilityLevel** ()

void **channelUp** ()

void **channelUp** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **channelDown** ()

void **channelDown** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **setChannel** (:doc:`ChannelInfo <and-channelinfo>` *channelInfo*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sets current channel

    **Parameters:**
        * channelInfo – must not be null

        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **setChannelById** (String *channelId*)

    **Parameters:**
        * channelId

void **setChannelById** (String *channelId*, `ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * channelId
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getCurrentChannel** (:doc:`ChannelListener <and-channellistener>` *listener*)

    **Parameters:**
        * listener – (optional) ChannelListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ChannelListener <and-channellistener>`> **subscribeCurrentChannel** (:doc:`ChannelListener <and-channellistener>` *listener*)

    **Parameters:**
        * listener – (optional) ChannelListener with methods to be called on success or failure

void **getChannelList** (:doc:`ChannelListListener <and-channellistlistener>` *listener*)

    **Parameters:**
        * listener – (optional) ChannelListListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ChannelListListener <and-channellistlistener>`> **subscribeChannelList** (final :doc:`ChannelListListener <and-channellistlistener>` *listener*)

    **Parameters:**
        * listener – (optional) final ChannelListListener with methods to be called on success or failure

void **getChannelCurrentProgramInfo** (:doc:`ProgramInfoListener <and-programinfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) ProgramInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ProgramInfoListener <and-programinfolistener>`> **subscribeChannelCurrentProgramInfo** (:doc:`ProgramInfoListener <and-programinfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) ProgramInfoListener with methods to be called on success or failure

void **getProgramInfo** (:doc:`ProgramInfoListener <and-programinfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) ProgramInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ProgramInfoListener <and-programinfolistener>`> **subscribeProgramInfo** (:doc:`ProgramInfoListener <and-programinfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) ProgramInfoListener with methods to be called on success or failure

void **getProgramList** (:doc:`ProgramListListener <and-programlistlistener>` *listener*)

    **Parameters:**
        * listener – (optional) ProgramListListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ProgramListListener <and-programlistlistener>`> **subscribeProgramList** (:doc:`ProgramListListener <and-programlistlistener>` *listener*)

    **Parameters:**
        * listener – (optional) ProgramListListener with methods to be called on success or failure

void **set3DEnabled** (final boolean *enabled*, final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * enabled
        * listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

void **get3DEnabled** (final :doc:`State3DModeListener <and-state3dmodelistener>` *listener*)

    **Parameters:**
        * listener – (optional) final State3DModeListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`State3DModeListener <and-state3dmodelistener>`> **subscribe3DEnabled** (final :doc:`State3DModeListener <and-state3dmodelistener>` *listener*)

    **Parameters:**
        * listener – (optional) final State3DModeListener with methods to be called on success or failure

:doc:`ExternalInputControl <and-externalinputcontrol>` **getExternalInput** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getExternalInputControlPriorityLevel** ()

void **launchInputPicker** (final :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    **Parameters:**
        * listener – (optional) final AppLaunchListener with methods to be called on success or failure

void **closeInputPicker** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * launchSession
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getExternalInputList** (final :doc:`ExternalInputListListener <and-externalinputlistlistener>` *listener*)

    **Parameters:**
        * listener – (optional) final ExternalInputListListener with methods to be called on success or failure

void **setExternalInput** (:doc:`ExternalInputInfo <and-externalinputinfo>` *externalInputInfo*, final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * externalInputInfo
        * listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

:doc:`MouseControl <and-mousecontrol>` **getMouseControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMouseControlCapabilityLevel** ()

void **connectMouse** ()

void **disconnectMouse** ()

void **click** ()

void **move** (final double *dx*, final double *dy*)

    **Parameters:**
        * dx
        * dy

void **move** (PointF *diff*)

    **Parameters:**
        * diff

void **scroll** (final double *dx*, final double *dy*)

    **Parameters:**
        * dx
        * dy

void **scroll** (PointF *diff*)

    **Parameters:**
        * diff

:doc:`TextInputControl <and-textinputcontrol>` **getTextInputControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getTextInputControlCapabilityLevel** ()

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`TextInputStatusListener <and-textinputstatuslistener>`> **subscribeTextInputStatus** (:doc:`TextInputStatusListener <and-textinputstatuslistener>` *listener*)

    **Parameters:**
        * listener – (optional) TextInputStatusListener with methods to be called on success or failure

void **sendText** (String *input*)

    **Parameters:**
        * input

void **sendKeyCode** (:doc:`KeyCode <and-keycode>` *keycode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * keycode
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **sendEnter** ()

void **sendDelete** ()

:doc:`PowerControl <and-powercontrol>` **getPowerControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPowerControlCapabilityLevel** ()

void **powerOff** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **powerOn** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`KeyControl <and-keycontrol>` **getKeyControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getKeyControlCapabilityLevel** ()

void **up** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **down** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **left** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **right** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

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

:doc:`WebAppLauncher <and-webapplauncher>` **getWebAppLauncher** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getWebAppLauncherCapabilityLevel** ()

void **launchWebApp** (final String *webAppId*, final :doc:`WebAppSession <and-webappsession>`.LaunchListener *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) final WebAppSession.LaunchListener with methods to be called on success or failure

void **launchWebApp** (String *webAppId*, boolean *relaunchIfRunning*, :doc:`WebAppSession <and-webappsession>`.LaunchListener *listener*)

    **Parameters:**
        * webAppId
        * relaunchIfRunning
        * listener – (optional) WebAppSession.LaunchListener with methods to be called on success or failure

void **launchWebApp** (final String *webAppId*, final JSONObject *params*, final :doc:`WebAppSession <and-webappsession>`.LaunchListener *listener*)

    **Parameters:**
        * webAppId
        * params
        * listener – (optional) final WebAppSession.LaunchListener with methods to be called on success or failure

void **launchWebApp** (final String *webAppId*, final JSONObject *params*, boolean *relaunchIfRunning*, final :doc:`WebAppSession <and-webappsession>`.LaunchListener *listener*)

    **Parameters:**
        * webAppId
        * params
        * relaunchIfRunning
        * listener – (optional) final WebAppSession.LaunchListener with methods to be called on success or failure

void **closeWebApp** (:doc:`LaunchSession <and-launchsession>` *launchSession*, final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * launchSession
        * listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

void **connectToWebApp** (final WebOSWebAppSession *webAppSession*, final boolean *joinOnly*, final :doc:`ResponseListener <and-responselistener>` <Object> *connectionListener*)

    **Parameters:**
        * webAppSession
        * joinOnly
        * connectionListener

void **pinWebApp** (String *webAppId*, final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

void **unPinWebApp** (String *webAppId*, final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

void **isWebAppPinned** (String *webAppId*, :doc:`WebAppPinStatusListener <and-webapppinstatuslistener>` *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) WebAppPinStatusListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`WebAppPinStatusListener <and-webapppinstatuslistener>`> **subscribeIsWebAppPinned** (String *webAppId*, :doc:`WebAppPinStatusListener <and-webapppinstatuslistener>` *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) WebAppPinStatusListener with methods to be called on success or failure

void **joinApp** (String *appId*, :doc:`WebAppSession <and-webappsession>`.LaunchListener *listener*)

    **Parameters:**
        * appId
        * listener – (optional) WebAppSession.LaunchListener with methods to be called on success or failure

void **connectToApp** (String *appId*, final :doc:`WebAppSession <and-webappsession>`.LaunchListener *listener*)

    **Parameters:**
        * appId
        * listener – (optional) final WebAppSession.LaunchListener with methods to be called on success or failure

void **joinWebApp** (final :doc:`LaunchSession <and-launchsession>` *webAppLaunchSession*, final :doc:`WebAppSession <and-webappsession>`.LaunchListener *listener*)

    **Parameters:**
        * webAppLaunchSession
        * listener – (optional) final WebAppSession.LaunchListener with methods to be called on success or failure

void **joinWebApp** (String *webAppId*, :doc:`WebAppSession <and-webappsession>`.LaunchListener *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) WebAppSession.LaunchListener with methods to be called on success or failure

void **sendMessage** (String *message*, :doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * message
        * launchSession
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **sendMessage** (JSONObject *message*, :doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * message
        * launchSessio
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getServiceInfo** (final ServiceInfoListener *listener*)

    **Parameters:**
        * listener – (optional) final ServiceInfoListener with methods to be called on success or failure

void **getSystemInfo** (final SystemInfoListener *listener*)

    **Parameters:**
        * listener – (optional) final SystemInfoListener with methods to be called on success or failure

void **secureAccessTest** (final SecureAccessTestListener *listener*)

    **Parameters:**
        * listener – (optional) final SecureAccessTestListener with methods to be called on success or failure

void **getACRAuthToken** (final ACRAuthTokenListener *listener*)

    **Parameters:**
        * listener – (optional) final ACRAuthTokenListener with methods to be called on success or failure

void **getLaunchPoints** (final LaunchPointsListener *listener*)

    **Parameters:**
        * listener – (optional) final LaunchPointsListener with methods to be called on success or failure

:doc:`PlaylistControl <and-playlistcontrol>` **getPlaylistControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPlaylistControlCapabilityLevel** ()

void **jumpToTrack** (long *index*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Play a track specified by index in the playlist

    **Parameters:**
        * index – index in the playlist, it starts from zero like index of array
        * listener – optional response listener

void **setPlayMode** (:doc:`PlayMode <and-playmode>` *playMode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Set order of playing tracks

    **Parameters:**
        * playMode
        * listener – optional response listener

void **sendCommand** (ServiceCommand<?> *command*)

    **Parameters:**
        * command

void **unsubscribe** (URLServiceSubscription<?> *subscription*)

    **Parameters:**
        * subscription

List<String> **getPermissions** ()

void **setPermissions** (List<String> *permissions*)

    **Parameters:**
        * permissions

void **getPlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)

    Get the current state of playback

    **Parameters:**
        * listener – (optional) PlayStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`PlayStateListener <and-playstatelistener>`> **subscribePlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)

    Subscribe for playback state changes

    **Parameters:**
        * listener – receives play state notifications

    **Returns:** ServiceSubscription<PlayStateListener>

boolean **isConnectable** ()

void **sendPairingKey** (String *pairingKey*)

    **Parameters:**
        * pairingKey

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

    See hasCapability: for a description of the wildcard feature provided
    by this method.

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

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppInfoListener <and-appinfolistener>`> **subscribeRunningApp** (:doc:`AppInfoListener <and-appinfolistener>` *listener*)

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

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppStateListener <and-appstatelistener>`> **subscribeAppState** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`AppStateListener <and-appstatelistener>` *listener*)

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

    Launch Netflix app. Will launch deep-linked to provided contentId, if
    supported on the target platform.

    **Related capabilities:**
        * ``Launcher.Netflix``
        * ``Launcher.Netflix.Params`` – if launching with contentId

    **Parameters:**
        * contentId – Video id to open
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchHulu** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    Launch Hulu app. Will launch deep-linked to provided contentId, if
    supported on the target platform.

    **Related capabilities:**
        * ``Launcher.Hulu``
        * ``Launcher.Hulu.Params`` – if launching with contentId

    **Parameters:**
        * contentId – Video id to open
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchAppStore** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    Launch the device's app store app, optionally deep-linked to a
    specific app's page.

    **Related capabilities:**
        * ``Launcher.AppStore``
        * ``Launcher.AppStore.Params``

    **Parameters:**
        * appId – (optional) ID of the application to show in the app store
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

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

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`PlayStateListener <and-playstatelistener>`> **subscribePlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)
    Subscribe for playback state changes

    **Parameters:**
        * listener – receives play state notifications

    **Returns:** ServiceSubscription<PlayStateListener>

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MediaInfoListener <and-mediainfolistener>`> **subscribeMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)

    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

void **displayImage** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, LaunchListener *listener*)

    Display an image on the device. Not all devices support all of the
    parameters -- supply as many as you have available.

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

    Play an audio or video file on the device. Not all devices support
    all of the parameters -- supply as many as you have available.

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

:doc:`VolumeControl <and-volumecontrol>` **getVolumeControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getVolumeControlCapabilityLevel** ()

void **volumeUp** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends the volume up command to the device.

    **Related capabilities:**
        * ``VolumeControl.UpDown``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **volumeDown** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends the volume down command to the device.

    **Related capabilities:**
        * ``VolumeControl.UpDown``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **setVolume** (float *volume*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Set the volume of the device.

    **Related capabilities:**
        * ``VolumeControl.Set``

    **Parameters:**
        * volume – Volume as a float between 0.0 and 1.0
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getVolume** (:doc:`VolumeListener <and-volumelistener>` *listener*)

    Get the current volume of the device.

    **Related capabilities:**
        * ``VolumeControl.Get``

    **Parameters:**
        * listener – (optional) VolumeListener with methods to be called on success or failure

void **setMute** (boolean *isMute*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Set the current volume.

    **Related capabilities:**
        * ``VolumeControl.Mute.Set``

    **Parameters:**
        * isMute
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getMute** (:doc:`MuteListener <and-mutelistener>` *listener*)

    Get the current mute state.

    **Related capabilities:**
        * ``VolumeControl.Mute.Get``

    **Parameters:**
        * listener – (optional) MuteListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`VolumeListener <and-volumelistener>`> **subscribeVolume** (:doc:`VolumeListener <and-volumelistener>` *listener*)

    Subscribe to the volume on the TV.

    **Related capabilities:**
        * ``VolumeControl.Subscribe``

    **Parameters:**
        * listener – (optional) VolumeListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MuteListener <and-mutelistener>`> **subscribeMute** (:doc:`MuteListener <and-mutelistener>` *listener*)

    Subscribe to the mute state on the TV.

    **Related capabilities:**
        * ``VolumeControl.Mute.Subscribe``

    **Parameters:**
        * listener – (optional) MuteListener with methods to be called on success or failure

:doc:`TVControl <and-tvcontrol>` **getTVControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getTVControlCapabilityLevel** ()

void **channelUp** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends a channel up command to the TV.

    **Related capabilities:**
        * ``TVControl.Channel.Up``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **channelDown** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends a channel down command to the TV.

    **Related capabilities:**
        * ``TVControl.Channel.Down``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **setChannel** (:doc:`ChannelInfo <and-channelinfo>` *channelNumber*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sets the current channel to the channel provided by the ChannelInfo
    object provided.


    **Related capabilities:**
        * ``TVControl.Channel.Set``

    **Parameters:**
        * channelNumber
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getCurrentChannel** (:doc:`ChannelListener <and-channellistener>` *listener*)

    Gets the current channel info from the TV.

    **Related capabilities:**
        * ``TVControl.Channel.Get``

    **Parameters:**
        * listener – (optional) ChannelListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ChannelListener <and-channellistener>`> **subscribeCurrentChannel** (:doc:`ChannelListener <and-channellistener>` *listener*)

    Subscribes to any changes in the current channel. Each time the
    channel is changed, the new channel's info will be provided to the
    success callback.

    **Related capabilities:**
        * ``TVControl.Channel.Subscribe``

    **Parameters:**
        * listener – (optional) ChannelListener with methods to be called on success or failure

void **getChannelList** (:doc:`ChannelListListener <and-channellistlistener>` *listener*)

    Get a list of available channels from the TV.

    **Related capabilities:**
        * ``TVControl.Channel.List``

    **Parameters:**
        * listener – (optional) ChannelListListener with methods to be called on success or failure

void **getProgramInfo** (:doc:`ProgramInfoListener <and-programinfolistener>` *listener*)

    Gets the current program info from the TV.

    **Related capabilities:**
        * ``TVControl.Program.Get``

    **Parameters:**
        * listener – (optional) ProgramInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ProgramInfoListener <and-programinfolistener>`> **subscribeProgramInfo** (:doc:`ProgramInfoListener <and-programinfolistener>` *listener*)

    Subscribes to any changes in the current program. Each time the
    channel is changed or a new program starts, the new program's info
    will be provided to the success callback.

    **Related capabilities:**
        * ``TVControl.Program.Subscribe``

    **Parameters:**
        * listener – (optional) ProgramInfoListener with methods to be called on success or failure

void **getProgramList** (:doc:`ProgramListListener <and-programlistlistener>` *listener*)

    Gets a list of all programs scheduled to play on the current channel.

    **Related capabilities:**
        * ``TVControl.Program.List``

    **Parameters:**
        * listener – (optional) ProgramListListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ProgramListListener <and-programlistlistener>`> **subscribeProgramList** (:doc:`ProgramListListener <and-programlistlistener>` *listener*)

    Subscribes to any changes in the current program. Each time the
    channel is changed or a new program starts, the new program's info
    will be provided to the success callback.

    **Related capabilities:**
        * ``TVControl.Program.List.Subscribe``

    **Parameters:**
        * listener – (optional) ProgramListListener with methods to be called on success or failure

void **get3DEnabled** (:doc:`State3DModeListener <and-state3dmodelistener>` *listener*)

    Gets the current 3D status of the TV.

    **Related capabilities:**
        * ``TVControl.3D.Get``

    **Parameters:**
        * listener – (optional) State3DModeListener with methods to be called on success or failure

void **set3DEnabled** (boolean *enabled*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sets the current 3D status of the TV.

    **Related capabilities:**
        * ``TVControl.3D.Set``

    **Parameters:**
        * enabled – Whether the TV's 3D mode should be on or off
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`State3DModeListener <and-state3dmodelistener>`> **subscribe3DEnabled** (:doc:`State3DModeListener <and-state3dmodelistener>` *listener*)

    Subscribes to changes in the TV's 3D status.

    **Related capabilities:**
        * ``TVControl.3D.Subscribe``

    **Parameters:**
        * listener – (optional) State3DModeListener with methods to be called on success or failure

:doc:`ToastControl <and-toastcontrol>` **getToastControl** ()

`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getToastControlCapabilityLevel** ()

void **showToast** (String *message*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Show a toast on the TV.

    **Parameters:**
        * message – Message to display
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForApp** (String *message*, :doc:`AppInfo <and-appinfo>` *appInfo*, JSONObject *params*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Show a toast on the TV and perform an action when the toast is clicked on the TV.

    **Related capabilities:**
        * ``ToastControl.Show.Clickable.App``
        * ``ToastControl.Show.Clickable.App.Params``

    **Parameters:**
        * message – Message to display
        * appInfo – AppInfo for app to launch on click of toast
        * params – Launch params for app
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForURL** (String *message*, String *url*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Show a toast on the TV and perform an action when the toast is
    clicked on the TV.

    **Related capabilities:**
        * ``ToastControl.Show.Clickable.URL``

    **Parameters:**
        * message – Message to display
        * url
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`ExternalInputControl <and-externalinputcontrol>` **getExternalInput** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getExternalInputControlPriorityLevel** ()

void **launchInputPicker** (:doc:`AppLaunchListener <and-applaunchlistener>` *listener*)

    Launches the visual input picker on the device. This may be helpful
    for situations where the device does not support directly
    listing/modifying the external inputs.

    **Related capabilities:**
        * ``ExternalInputControl.Picker.Launch``

    **Parameters:**
        * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **closeInputPicker** (:doc:`LaunchSession <and-launchsession>` *launchSessionm*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Closes the input picker on the device, if it is currently open.

    **Related capabilities:**
        * ``ExternalInputControl.Picker.Close``

    **Parameters:**
        * launchSessionm
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getExternalInputList** (:doc:`ExternalInputListListener <and-externalinputlistlistener>` *listener*)

    Get a list of input devices (HDMI, AV, etc) connected to the device

    **Related capabilities:**
        * ``ExternalInputControl.List``

    **Parameters:**
        * listener – (optional) ExternalInputListListener with methods to be called on success or failure

void **setExternalInput** (:doc:`ExternalInputInfo <and-externalinputinfo>` *input*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Switch to the specified external input

    **Related capabilities:**
        * ``ExternalInputControl.Set``

    **Parameters:**
        * input
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`MouseControl <and-mousecontrol>` **getMouseControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMouseControlCapabilityLevel** ()

void **connectMouse** ()

    Establish a connection with the DeviceService's mouse communication
    medium (WebSocket, HTTP, etc). While this step may not be necessary
    with certain platforms, it is suggested to call it anyways, for
    purposes of seamless normalization. Calling connect on a
    non-connectable protocol will just trigger the success callback
    immediately.

    **Related capabilities:**
        * ``MouseControl.Connect``

void **disconnectMouse** ()

    Disconnects from the mouse communication medium.

    **Related capabilities:**
        * ``MouseControl.Disconnect``

void **click** ()

    Perform a click action at the current mouse position.

    **Related capabilities:**
        * ``MouseControl.Click``

void **move** (double *dx*, double *dy*)

    Move the mouse by the given distance values.

    **Related capabilities:**
        * ``MouseControl.Move``

    **Parameters:**
        * dx – Distance to move the mouse on the x-axis relative to its current position
        * dy – Distance to move the mouse on the y-axis relative to its current position

void **scroll** (double *dx*, double *dy*)

    Scroll by the given distance values.

    **Related capabilities:**
        * ``MouseControl.Scroll``

    **Parameters:**
        * dx – Distance to scroll the mouse on the x-axis relative to its current position
        * dy – Distance to scroll the mouse on the y-axis relative to its current position

:doc:`TextInputControl <and-textinputcontrol>` **getTextInputControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getTextInputControlCapabilityLevel** ()

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`TextInputStatusListener <and-textinputstatuslistener>`> **subscribeTextInputStatus** (:doc:`TextInputStatusListener <and-textinputstatuslistener>` *listener*)

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

:doc:`PowerControl <and-powercontrol>` **getPowerControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPowerControlCapabilityLevel** ()

void **powerOff** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Sends a power off signal to the TV. A success message will,
    internally, trigger a disconnection with the device.

    **Related capabilities:**
        * ``PowerControl.Off``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **powerOn** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

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

:doc:`WebAppLauncher <and-webapplauncher>` **getWebAppLauncher** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getWebAppLauncherCapabilityLevel** ()

void **launchWebApp** (String *webAppId*, LaunchListener *listener*)

    Launch a web application on the TV.

    **Related capabilities:**
        * ``WebAppLauncher.Launch``
        * ``WebAppLauncher.Launch.Params`` – if launching with params

    **Parameters:**
        * webAppId – ID of web app assigned by platform vendor
        * listener – (optional) LaunchListener with methods to be called on success or failure

void **joinWebApp** (:doc:`LaunchSession <and-launchsession>` *webAppLaunchSession*, LaunchListener *listener*)

    Join an active web app without launching/relaunching. If the app is
    not running/joinable, the failure block will be called immediately.

    **Related capabilities:**
        * ``WebAppLauncher.Send``
        * ``WebAppLauncher.Receive``

    **Parameters:**
        * webAppLaunchSession – LaunchSession for the web app to be joined
        * listener – (optional) LaunchListener with methods to be called on success or failure

void **closeWebApp** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

   Closes a web app with the provided LaunchSession.

    **Related capabilities:**
        * ``WebAppLauncher.Close``

    **Parameters:**
        * launchSession – LaunchSession associated with the web app to be closed
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **pinWebApp** (String *webAppId*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **unPinWebApp** (String *webAppId*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **isWebAppPinned** (String *webAppId*, :doc:`WebAppPinStatusListener <and-webapppinstatuslistener>` *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) WebAppPinStatusListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`WebAppPinStatusListener <and-webapppinstatuslistener>`> **subscribeIsWebAppPinned** (String *webAppId*, :doc:`WebAppPinStatusListener <and-webapppinstatuslistener>` *listener*)

    **Parameters:**
        * webAppId
        * listener – (optional) WebAppPinStatusListener with methods to be called on success or failure

:doc:`PlaylistControl <and-playlistcontrol>` **getPlaylistControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPlaylistControlCapabilityLevel** ()

void **jumpToTrack** (long *index*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Jump the playlist to the designated track.

    Play a track specified by index in the playlist

    **Related capabilities:**
        * ``PlaylistControl.JumpToTrack``

    **Parameters:**
        * index – index in the playlist, it starts from zero like index of array
        * listener – optional response listener

void **setPlayMode** (:doc:`PlayMode <and-playmode>` *playMode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Set order of playing tracks

    **Parameters:**
        * playMode
        * listener – optional response listener

void **onLoseReachability** (DeviceServiceReachability *reachability*)

    **Parameters:**
        * reachability

void **unsubscribe** (URLServiceSubscription<?> *subscription*)

    **Parameters:**
        * subscription

void **sendCommand** (ServiceCommand<?> *command*)

    **Parameters:**
        * command
