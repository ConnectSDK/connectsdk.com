Launcher
========

The Launcher capability protocol serves to define the methods required
for normalizing the launching of apps. It allows for in-built support
for certain common launch types (deep-linking to YouTube, Netflix, Hulu,
browser, etc) as well as by (platform-specific) app id.

Methods
-------

\- (id<:doc:`Launcher <ios-launcher>`>) **launcher**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **launcherPriority**

\- (void) **launchApp**:(NSString \*)\ *appId* **success**:(`AppLaunchSuccessBlock <#applaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch an application on the device.

   **Related capabilities:**

   -  ``Launcher.App``

   **Parameters:**

   -  appId – ID of the application

   -  **success**: success – Optional AppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **launchAppWithInfo**:(:doc:`AppInfo <ios-appInfo>` \*)\ *appInfo* **success**:(`AppLaunchSuccessBlock <#applaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch an application on the device.

   **Related capabilities:**

   -  ``Launcher.App``

   -  ``Launcher.App.Params`` – if launching with params

   **Parameters:**

   -  appInfo – AppInfo object for the application

   -  **success**: success – Optional AppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **launchAppWithInfo**:(:doc:`AppInfo <ios-appInfo>` \*)\ *appInfo* **params**:(NSDictionary \*)\ *params* **success**:(`AppLaunchSuccessBlock <#applaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch an application on the device.

   **Related capabilities:**

   -  ``Launcher.App``

   -  ``Launcher.App.Params`` – if launching with params

   **Parameters:**

   -  appInfo – AppInfo object for the application

   -  **params**: params

   -  **success**: success – Optional AppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **closeApp**:(:doc:`LaunchSession <ios-launchSession>` \*)\ *launchSession* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Close an application on the device.

   **Related capabilities:**

   -  ``Launcher.App.Close``

   **Parameters:**

   -  launchSession – LaunchSession of the target app

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getAppListWithSuccess**:(`AppListSuccessBlock <#applistsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Gets a list of all apps installed on the device.

   **Related capabilities:**

   -  ``Launcher.App.List``

   **Parameters:**

   -  success – Optional AppListSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getRunningAppWithSuccess**:(`AppInfoSuccessBlock <#appinfosuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Gets an AppInfo object for the current running app on the device.

   **Related capabilities:**

   -  ``Launcher.RunningApp``

   **Parameters:**

   -  success – Optional AppInfoSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (:doc:`ServiceSubscription <ios-servicesubscription>` \*) **subscribeRunningAppWithSuccess**:(`AppInfoSuccessBlock <#appinfosuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribes to changes of the current running app. Every time the
   running app changes, the success block will be called with an AppInfo
   object for the current running app.

   **Related capabilities:**

   -  ``Launcher.RunningApp.Subscribe``

   **Parameters:**

   -  success – Optional AppInfoSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getAppState**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *launchSession* **success**:(`AppStateSuccessBlock <#appstatesuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Gets the target app's running status and on-screen visibility.

   **Related capabilities:**

   -  ``Launcher.AppState``

   **Parameters:**

   -  launchSession – LaunchSession of the target app

   -  **success**: success – Optional AppStateSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (:doc:`ServiceSubscription <ios-servicesubscription>` \*) **subscribeAppState**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *launchSession* **success**:(`AppStateSuccessBlock <#appstatesuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribes to changes of the state of the target app. Every time the
   app's state changes, the success block will be called with info on
   the app's running status and on-screen visibility.

   **Related capabilities:**

   -  ``Launcher.AppState.Subscribe``

  **Parameters:**

   -  launchSession – LaunchSession of the target app

   -  **success**: success – Optional AppStateSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **launchAppStore**:(NSString \*)\ *appId* **success**:(`AppLaunchSuccessBlock <#applaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch the device's app store app, optionally deep-linked to a
   specific app's page.

   **Related capabilities:**

   -  ``Launcher.AppStore``
   -  ``Launcher.AppStore.Params``

   **Parameters:**

   -  appId – (optional) ID of the application to show in the app store

   -  **success**: success – Optional AppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **launchBrowser**:(NSURL \*)\ *target* **success**:(`AppLaunchSuccessBlock <#applaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch the web browser. Will launch deep-linked to provided URL, if
   supported on the target platform.

   **Related capabilities:**

   -  ``Launcher.Browser``

   -  ``Launcher.Browser.Params`` – if launching with url

   **Parameters:**

   -  target – URL to open

   -  **success**: success – Optional AppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **launchYouTube**:(NSString \*)\ *contentId* **success**:(`AppLaunchSuccessBlock <#applaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch YouTube app. Will launch deep-linked to provided contentId, if
   supported on the target platform.

   **Related capabilities:**

   -  ``Launcher.YouTube``

   -  ``Launcher.YouTube.Params`` – if launching with contentId

   **Parameters:**

   -  contentId – Video id to open

   -  **success**: success – Optional AppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **launchYouTube**:(NSString \*)\ *contentId* **startTime**:(float)\ *startTime* **success**:(`AppLaunchSuccessBlock <#applaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch YouTube app. Will launch deep-linked to provided contentId, if
   supported on the target platform.

   **Related capabilities:**

   -  ``Launcher.YouTube``

   -  ``Launcher.YouTube.Params`` – if launching with contentId

   **Parameters:**

   -  contentId – Video id to open

   -  **startTime**: startTime

   -  **success**: success – Optional AppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

Typedefs
--------

AppInfoSuccessBlock
~~~~~~~~~~~~~~~~~~~

void(^)(:doc:`AppInfo <ios-appinfo>` \*appInfo)

Success block that is called upon requesting info about the current
running app.

-  appInfo

   Object containing info about the running app

AppLaunchSuccessBlock
~~~~~~~~~~~~~~~~~~~~~

void(^)(:doc:`LaunchSession <ios-launchsession>` \*launchSession)

Success block that is called upon successfully launching an app.

AppListSuccessBlock
~~~~~~~~~~~~~~~~~~~

void(^)(NSArray \*appList)

Success block that is called upon successfully getting the app list.

-  appList

   Array containing an AppInfo object for each available app on the
   device

AppStateSuccessBlock
~~~~~~~~~~~~~~~~~~~~

void(^)(BOOL running, BOOL visible)

Success block that is called upon successfully getting an app's state.

-  running

   Whether the app is currently running

-  visible

   Whether the app is currently visible on the screen
