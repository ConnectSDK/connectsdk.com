DIALService
===========
``com.connectsdk.service.DIALService``

*extends* :doc:`DeviceService <and-deviceservice>`

DIALService is a full implementation of the DIscover And Launch (DIAL)
protocol specification. DIALService is used to launch & close apps on
DIAL-enabled devices. It can also be used to probe for an app's
existence on a DIAL-enabled device. DIAL commands occur over HTTP.

See the `DIAL protocol
specification <http://www.dial-multiscreen.org/dial-protocol-specification>`__
for more information.

Properties
----------

final String ID = "DIAL"

Methods
-------

static void **registerApp** (String *appId*)
    Registers an app ID to be checked upon discovery of this device. If
    the app is found on the target device, the DIALService will gain the
    "Launcher." capability, where is the value of the appId parameter.

    This method must be called before starting DiscoveryManager for the
    first time.

    **Parameters:**

    -  appId - ID of the app to be checked for

static DiscoveryFilter **discoveryFilter** ()

**DIALService** (ServiceDescription *serviceDescription*, ServiceConfig *serviceConfig*)
    **Parameters:**

    -  serviceDescription
    -  serviceConfig

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPriorityLevel** (Class<?extends CapabilityMethods > *clazz*)
    **Parameters:**

    -  clazz

void **setServiceDescription** (ServiceDescription *serviceDescription*)
    **Parameters:**

    -  serviceDescription

:doc:`Launcher <and-launcher>` **getLauncher** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getLauncherCapabilityLevel** ()

void **launchApp** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    **Parameters:**

    -  appId
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchAppWithInfo** (:doc:`AppInfo <and-appinfo>` *appInfo*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    **Parameters:**

    -  appInfo
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchAppWithInfo** (final :doc:`AppInfo <and-appinfo>` *appInfo*, Object *params*, final :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    **Parameters:**

    -  appInfo
    -  params
    -  listener – (optional) final AppLaunchListener with methods to be called on success or failure

void **launchBrowser** (String *url*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    **Parameters:**

    -  url
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **closeApp** (final :doc:`LaunchSession <and-launchsession>` *launchSession*, final :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  launchSession
    -  listener – (optional) final ResponseListener< Object > with methods to be called on success or failure

void **launchYouTube** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    **Parameters:**

    -  contentId
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchYouTube** (String *contentId*, float *startTime*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    **Parameters:**

    -  contentId
    -  startTime
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchHulu** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    **Parameters:**

    -  contentId
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchNetflix** (final String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    **Parameters:**
    -  contentId
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchAppStore** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    **Parameters:**

    -  appId
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **getAppList** (:doc:`AppListListener <and-applistlistener>` *listener*)
    **Parameters:**

    -  listener – (optional) AppListListener with methods to be called on success or failure

void **getRunningApp** (:doc:`AppInfoListener <and-appinfolistener>` *listener*)
    **Parameters:**

    -  listener – (optional) AppInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppInfoListener <and-appinfolistener>`> **subscribeRunningApp** (:doc:`AppInfoListener <and-appinfolistener>` *listener*)
    **Parameters:**

    -  listener – (optional) AppInfoListener with methods to be called on success or failure

void **getAppState** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`AppStateListener <and-appstatelistener>` *listener*)
    **Parameters:**

    -  launchSession
    -  listener – (optional) AppStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppStateListener <and-appstatelistener>`> **subscribeAppState** (:doc:`LaunchSession <and-launchsession>` *launchSession*, com.connectsdk.service.capability.\ :doc:`Launcher <and-launcher>`.\ :doc:`AppStateListener <and-appstatelistener>` *listener*)
    **Parameters:**

    -  launchSession
    -  listener – (optional) com.connectsdk.service.capability.Launcher.AppStateListener with methods to be called on success or failure

void **closeLaunchSession** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    **Parameters:**

    -  launchSession
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

boolean **isConnectable** ()

boolean **isConnected** ()

void **connect** ()

void **disconnect** ()

void **onLoseReachability** (DeviceServiceReachability *reachability*)
    **Parameters:**

    -  reachability

void **sendCommand** (final ServiceCommand<?> *mCommand*)
    **Parameters:**

    -  mCommand

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

:doc:`Launcher <and-launcher>` **getLauncher** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getLauncherCapabilityLevel** ()

void **launchAppWithInfo** (:doc:`AppInfo <and-appinfo>` *appInfo*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    Launch an application on the device.

    **Related capabilities:**

    -  ``Launcher.App``
    -  ``Launcher.App.Params`` – if launching with params

    **Parameters:**

    -  appInfo – AppInfo object for the application
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchApp** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    Launch an application on the device.

    **Related capabilities:**

    -  ``Launcher.App``

    **Parameters:**

    -  appId – ID of the application
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **closeApp** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Close an application on the device.

    **Related capabilities:**

    -  ``Launcher.App.Close``

    **Parameters:**

    -  launchSession – LaunchSession of the target app
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getAppList** (:doc:`AppListListener <and-applistlistener>` *listener*)
    Gets a list of all apps installed on the device.

    **Related capabilities:**

    -  ``Launcher.App.List``

    **Parameters:**

    -  listener – (optional) AppListListener with methods to be called on success or failure

void **getRunningApp** (:doc:`AppInfoListener <and-appinfolistener>` *listener*)
    Gets an AppInfo object for the current running app on the device.

    **Related capabilities:**

    -  ``Launcher.RunningApp``

    **Parameters:**

    -  listener – (optional) AppInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppInfoListener <and-appinfolistener>`> **subscribeRunningApp** (:doc:`AppInfoListener <and-appinfolistener>` *listener*)
    Subscribes to changes of the current running app. Every time the
    running app changes, the success block will be called with an AppInfo
    object for the current running app.

    **Related capabilities:**

    -  ``Launcher.RunningApp.Subscribe``

    **Parameters:**

    -  listener – (optional) AppInfoListener with methods to be called on success or failure

void **getAppState** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`AppStateListener <and-appstatelistener>` *listener*)
    Gets the target app's running status and on-screen visibility.

    **Related capabilities:**

    -  ``Launcher.AppState``

    **Parameters:**

    -  launchSession – LaunchSession of the target app
    -  listener – (optional) AppStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`AppStateListener <and-appstatelistener>`> **subscribeAppState** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`AppStateListener <and-appstatelistener>` *listener*)
    Subscribes to changes of the state of the target app. Every time the
    app's state changes, the success block will be called with info on
    the app's running status and on-screen visibility.

    **Related capabilities:**

    -  ``Launcher.AppState.Subscribe``

    **Parameters:**

    -  launchSession – LaunchSession of the target app
    -  listener – (optional) AppStateListener with methods to be called on success or failure

void **launchBrowser** (String *url*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    Launch the web browser. Will launch deep-linked to provided URL, if
    supported on the target platform.

    **Related capabilities:**

    -  ``Launcher.Browser``
    -  ``Launcher.Browser.Params`` – if launching with url

    **Parameters:**

    -  url
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchYouTube** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    Launch YouTube app. Will launch deep-linked to provided contentId, if
    supported on the target platform.

    **Related capabilities:**

    -  ``Launcher.YouTube``
    -  ``Launcher.YouTube.Params`` – if launching with contentId

    **Parameters:**

    -  contentId – Video id to open
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchNetflix** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    Launch Netflix app. Will launch deep-linked to provided contentId, if
    supported on the target platform.

    **Related capabilities:**

    -  ``Launcher.Netflix``
    -  ``Launcher.Netflix.Params`` – if launching with contentId

    **Parameters:**

    -  contentId – Video id to open
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchHulu** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    Launch Hulu app. Will launch deep-linked to provided contentId, if
    supported on the target platform.

    **Related capabilities:**

    -  ``Launcher.Hulu``
    -  ``Launcher.Hulu.Params`` – if launching with contentId

    **Parameters:**

    -  contentId – Video id to open
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchAppStore** (String *appId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    Launch the device's app store app, optionally deep-linked to a
    specific app's page.

    **Related capabilities:**

    -  ``Launcher.AppStore``
    -  ``Launcher.AppStore.Params``

    **Parameters:**

    -  appId – (optional) ID of the application to show in the app store
    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **onLoseReachability** (DeviceServiceReachability *reachability*)
    **Parameters:**

    -  reachability

void **unsubscribe** (URLServiceSubscription<?> *subscription*)
    **Parameters:**

    -  subscription

void **sendCommand** (ServiceCommand<?> *command*)
    **Parameters:**

    -  command
