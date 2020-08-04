DIALService com.connectsdk.service.DIALService
==============================================

*extends*\ `DeviceService </apis/1-6-0/android/DeviceService>`__

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

   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  appId –

      ID of the app to be checked for

static DiscoveryFilter **discoveryFilter** ()

**DIALService** (ServiceDescription *serviceDescription*, ServiceConfig *serviceConfig*)
   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  serviceDescription
   -  serviceConfig

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

`Launcher </apis/1-6-0/android/Launcher>`__ **getLauncher** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getLauncherCapabilityLevel** ()

void **launchApp** (String *appId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-4
      :class: method-detail-label

   -  appId

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchAppWithInfo** (`AppInfo </apis/1-6-0/android/AppInfo>`__ *appInfo*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-5
      :class: method-detail-label

   -  appInfo

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchAppWithInfo** (final `AppInfo </apis/1-6-0/android/AppInfo>`__ *appInfo*, Object *params*, final `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-6
      :class: method-detail-label

   -  appInfo

   -  params

   -  listener –

      (optional) final AppLaunchListener with methods to be called on
      success or failure

void **launchBrowser** (String *url*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-7
      :class: method-detail-label

   -  url

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **closeApp** (final `LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, final `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-8
      :class: method-detail-label

   -  launchSession

   -  listener –

      (optional) final ResponseListener< Object > with methods to be
      called on success or failure

void **launchYouTube** (String *contentId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-9
      :class: method-detail-label

   -  contentId

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchYouTube** (String *contentId*, float *startTime*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-10
      :class: method-detail-label

   -  contentId

   -  startTime

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchHulu** (String *contentId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-11
      :class: method-detail-label

   -  contentId

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchNetflix** (final String *contentId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-12
      :class: method-detail-label

   -  contentId

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchAppStore** (String *appId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-13
      :class: method-detail-label

   -  appId

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **getAppList** (`AppListListener </apis/1-6-0/android/AppListListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-14
      :class: method-detail-label

   -  listener –

      (optional) AppListListener with methods to be called on success or
      failure

void **getRunningApp** (`AppInfoListener </apis/1-6-0/android/AppInfoListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-15
      :class: method-detail-label

   -  listener –

      (optional) AppInfoListener with methods to be called on success or
      failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`AppInfoListener </apis/1-6-0/android/AppInfoListener>`__> **subscribeRunningApp** (`AppInfoListener </apis/1-6-0/android/AppInfoListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-16
      :class: method-detail-label

   -  listener –

      (optional) AppInfoListener with methods to be called on success or
      failure

void **getAppState** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, `AppStateListener </apis/1-6-0/android/AppStateListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-17
      :class: method-detail-label

   -  launchSession

   -  listener –

      (optional) AppStateListener with methods to be called on success
      or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`AppStateListener </apis/1-6-0/android/AppStateListener>`__> **subscribeAppState** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, com.connectsdk.service.capability.\ `Launcher </apis/1-6-0/android/Launcher>`__.\ `AppStateListener </apis/1-6-0/android/AppStateListener>`__ *listener*)
   .. rubric:: Parameters:
      :name: parameters-18
      :class: method-detail-label

   -  launchSession

   -  listener –

      (optional)
      com.connectsdk.service.capability.Launcher.AppStateListener with
      methods to be called on success or failure

void **closeLaunchSession** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   .. rubric:: Parameters:
      :name: parameters-19
      :class: method-detail-label

   -  launchSession

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

boolean **isConnectable** ()

boolean **isConnected** ()

void **connect** ()

void **disconnect** ()

void **onLoseReachability** (DeviceServiceReachability *reachability*)
   .. rubric:: Parameters:
      :name: parameters-20
      :class: method-detail-label

   -  reachability

void **sendCommand** (final ServiceCommand<?> *mCommand*)
   .. rubric:: Parameters:
      :name: parameters-21
      :class: method-detail-label

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

   .. rubric:: Parameters:
      :name: parameters-22
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
      :name: parameters-23
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
      :name: parameters-24
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
      :name: parameters-25
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
      :name: parameters-26
      :class: method-detail-label

   -  launchSession –

      LaunchSession to close

   -  listener –

      (optional) listener to be called on success/failure

`Launcher </apis/1-6-0/android/Launcher>`__ **getLauncher** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getLauncherCapabilityLevel** ()

void **launchAppWithInfo** (`AppInfo </apis/1-6-0/android/AppInfo>`__ *appInfo*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   Launch an application on the device.

   .. rubric:: Related capabilities:
      :name: related-capabilities
      :class: method-detail-label

   -  ``Launcher.App``

   -  ``Launcher.App.Params`` –

      if launching with params

   .. rubric:: Parameters:
      :name: parameters-27
      :class: method-detail-label

   -  appInfo –

      AppInfo object for the application

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchApp** (String *appId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   Launch an application on the device.

   .. rubric:: Related capabilities:
      :name: related-capabilities-1
      :class: method-detail-label

   -  ``Launcher.App``

   .. rubric:: Parameters:
      :name: parameters-28
      :class: method-detail-label

   -  appId –

      ID of the application

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **closeApp** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Close an application on the device.

   .. rubric:: Related capabilities:
      :name: related-capabilities-2
      :class: method-detail-label

   -  ``Launcher.App.Close``

   .. rubric:: Parameters:
      :name: parameters-29
      :class: method-detail-label

   -  launchSession –

      LaunchSession of the target app

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getAppList** (`AppListListener </apis/1-6-0/android/AppListListener>`__ *listener*)
   Gets a list of all apps installed on the device.

   .. rubric:: Related capabilities:
      :name: related-capabilities-3
      :class: method-detail-label

   -  ``Launcher.App.List``

   .. rubric:: Parameters:
      :name: parameters-30
      :class: method-detail-label

   -  listener –

      (optional) AppListListener with methods to be called on success or
      failure

void **getRunningApp** (`AppInfoListener </apis/1-6-0/android/AppInfoListener>`__ *listener*)
   Gets an AppInfo object for the current running app on the device.

   .. rubric:: Related capabilities:
      :name: related-capabilities-4
      :class: method-detail-label

   -  ``Launcher.RunningApp``

   .. rubric:: Parameters:
      :name: parameters-31
      :class: method-detail-label

   -  listener –

      (optional) AppInfoListener with methods to be called on success or
      failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`AppInfoListener </apis/1-6-0/android/AppInfoListener>`__> **subscribeRunningApp** (`AppInfoListener </apis/1-6-0/android/AppInfoListener>`__ *listener*)
   Subscribes to changes of the current running app. Every time the
   running app changes, the success block will be called with an AppInfo
   object for the current running app.

   .. rubric:: Related capabilities:
      :name: related-capabilities-5
      :class: method-detail-label

   -  ``Launcher.RunningApp.Subscribe``

   .. rubric:: Parameters:
      :name: parameters-32
      :class: method-detail-label

   -  listener –

      (optional) AppInfoListener with methods to be called on success or
      failure

void **getAppState** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, `AppStateListener </apis/1-6-0/android/AppStateListener>`__ *listener*)
   Gets the target app's running status and on-screen visibility.

   .. rubric:: Related capabilities:
      :name: related-capabilities-6
      :class: method-detail-label

   -  ``Launcher.AppState``

   .. rubric:: Parameters:
      :name: parameters-33
      :class: method-detail-label

   -  launchSession –

      LaunchSession of the target app

   -  listener –

      (optional) AppStateListener with methods to be called on success
      or failure

`ServiceSubscription </apis/1-6-0/android/ServiceSubscription>`__\ <`AppStateListener </apis/1-6-0/android/AppStateListener>`__> **subscribeAppState** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSession*, `AppStateListener </apis/1-6-0/android/AppStateListener>`__ *listener*)
   Subscribes to changes of the state of the target app. Every time the
   app's state changes, the success block will be called with info on
   the app's running status and on-screen visibility.

   .. rubric:: Related capabilities:
      :name: related-capabilities-7
      :class: method-detail-label

   -  ``Launcher.AppState.Subscribe``

   .. rubric:: Parameters:
      :name: parameters-34
      :class: method-detail-label

   -  launchSession –

      LaunchSession of the target app

   -  listener –

      (optional) AppStateListener with methods to be called on success
      or failure

void **launchBrowser** (String *url*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   Launch the web browser. Will launch deep-linked to provided URL, if
   supported on the target platform.

   .. rubric:: Related capabilities:
      :name: related-capabilities-8
      :class: method-detail-label

   -  ``Launcher.Browser``

   -  ``Launcher.Browser.Params`` –

      if launching with url

   .. rubric:: Parameters:
      :name: parameters-35
      :class: method-detail-label

   -  url

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchYouTube** (String *contentId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   Launch YouTube app. Will launch deep-linked to provided contentId, if
   supported on the target platform.

   .. rubric:: Related capabilities:
      :name: related-capabilities-9
      :class: method-detail-label

   -  ``Launcher.YouTube``

   -  ``Launcher.YouTube.Params`` –

      if launching with contentId

   .. rubric:: Parameters:
      :name: parameters-36
      :class: method-detail-label

   -  contentId –

      Video id to open

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchNetflix** (String *contentId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   Launch Netflix app. Will launch deep-linked to provided contentId, if
   supported on the target platform.

   .. rubric:: Related capabilities:
      :name: related-capabilities-10
      :class: method-detail-label

   -  ``Launcher.Netflix``

   -  ``Launcher.Netflix.Params`` –

      if launching with contentId

   .. rubric:: Parameters:
      :name: parameters-37
      :class: method-detail-label

   -  contentId –

      Video id to open

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchHulu** (String *contentId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   Launch Hulu app. Will launch deep-linked to provided contentId, if
   supported on the target platform.

   .. rubric:: Related capabilities:
      :name: related-capabilities-11
      :class: method-detail-label

   -  ``Launcher.Hulu``

   -  ``Launcher.Hulu.Params`` –

      if launching with contentId

   .. rubric:: Parameters:
      :name: parameters-38
      :class: method-detail-label

   -  contentId –

      Video id to open

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **launchAppStore** (String *appId*, `AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   Launch the device's app store app, optionally deep-linked to a
   specific app's page.

   .. rubric:: Related capabilities:
      :name: related-capabilities-12
      :class: method-detail-label

   -  ``Launcher.AppStore``
   -  ``Launcher.AppStore.Params``

   .. rubric:: Parameters:
      :name: parameters-39
      :class: method-detail-label

   -  appId –

      (optional) ID of the application to show in the app store

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **onLoseReachability** (DeviceServiceReachability *reachability*)
   .. rubric:: Parameters:
      :name: parameters-40
      :class: method-detail-label

   -  reachability

void **unsubscribe** (URLServiceSubscription<?> *subscription*)
   .. rubric:: Parameters:
      :name: parameters-41
      :class: method-detail-label

   -  subscription

void **sendCommand** (ServiceCommand<?> *command*)
   .. rubric:: Parameters:
      :name: parameters-42
      :class: method-detail-label

   -  command
