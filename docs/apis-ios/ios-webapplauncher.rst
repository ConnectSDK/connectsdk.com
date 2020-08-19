WebAppLauncher
==============

The WebAppLauncher capability protocol provides capabilities for
launching web apps and establishing two-way communication.

Methods
-------

\- (id<:doc:`WebAppLauncher <ios-webapplauncher>`>) **webAppLauncher**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **webAppLauncherPriority**

\- (void) **launchWebApp**:(NSString \*)\ *webAppId* **success**:(`WebAppLaunchSuccessBlock <#webapplaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch a web application on the TV.

   **Related capabilities:**

   -  ``WebAppLauncher.Launch``

   -  ``WebAppLauncher.Launch.Params`` – if launching with params

   **Parameters:**

   -  webAppId – ID of web app assigned by platform vendor

   -  **success**: success – Optional WebAppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **launchWebApp**:(NSString \*)\ *webAppId* **params**:(NSDictionary \*)\ *params* **success**:(`WebAppLaunchSuccessBlock <#webapplaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch a web application on the TV.

   **Related capabilities:**

   -  ``WebAppLauncher.Launch``

   -  ``WebAppLauncher.Launch.Params`` – if launching with params

   **Parameters:**

   -  webAppId – ID of web app assigned by platform vendor

   -  **params**: params – Dictionary of key/value strings. Not available on all target
      platforms

   -  **success**: success – Optional WebAppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **launchWebApp**:(NSString \*)\ *webAppId* **relaunchIfRunning**:(BOOL)\ *relaunchIfRunning* **success**:(`WebAppLaunchSuccessBlock <#webapplaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch a web application on the TV.

   This method requires pairing on webOS

   **Related capabilities:**

   -  ``WebAppLauncher.Launch``

   -  ``WebAppLauncher.Launch.Params`` – if launching with params

   **Parameters:**

   -  webAppId – ID of web app assigned by platform vendor

   -  **relaunchIfRunning**: relaunchIfRunning – If supported on target platform, web app will force relaunch if
      value true

   -  **success**: success – Optional WebAppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **launchWebApp**:(NSString \*)\ *webAppId* **params**:(NSDictionary \*)\ *params* **relaunchIfRunning**:(BOOL)\ *relaunchIfRunning* **success**:(`WebAppLaunchSuccessBlock <#webapplaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Launch a web application on the TV.

   This method requires pairing on webOS

   **Related capabilities:**

   -  ``WebAppLauncher.Launch``

   -  ``WebAppLauncher.Launch.Params`` – if launching with params

   **Parameters:**

   -  webAppId – ID of web app assigned by platform vendor

   -  **params**: params – Dictionary of key/value strings. Not available on all target
      platforms

   -  **relaunchIfRunning**: relaunchIfRunning – If supported on target platform, web app will force relaunch if
      value true

   -  **success**: success – Optional WebAppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **joinWebApp**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *webAppLaunchSession* **success**:(`WebAppLaunchSuccessBlock <#webapplaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Join an active web app without launching/relaunching. If the app is
   not running/joinable, the failure block will be called immediately.

   **Related capabilities:**

   -  ``WebAppLauncher.Send``
   -  ``WebAppLauncher.Receive``

   **Parameters:**

   -  webAppLaunchSession – LaunchSession for the web app to be joined

   -  **success**: success – Optional WebAppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **joinWebAppWithId**:(NSString \*)\ *webAppId* **success**:(`WebAppLaunchSuccessBlock <#webapplaunchsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Join an active web app without launching/relaunching. If the app is
   not running/joinable, the failure block will be called immediately.

   **Related capabilities:**

   -  ``WebAppLauncher.Send``
   -  ``WebAppLauncher.Receive``

   **Parameters:**

   -  webAppId – Unique identifier for the web app to be joined

   -  **success**: success – Optional WebAppLaunchSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **closeWebApp**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *launchSession* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Closes a web app with the provided LaunchSession.

   **Related capabilities:**

   -  ``WebAppLauncher.Close``

   **Parameters:**

   -  launchSession – LaunchSession associated with the web app to be closed

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **pinWebApp**:(NSString \*)\ *webAppId* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  webAppId

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **unPinWebApp**:(NSString \*)\ *webAppId* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  webAppId

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **isWebAppPinned**:(NSString \*)\ *webAppId* **success**:(WebAppPinStatusBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  webAppId

   -  **success**: success – Optional WebAppPinStatusBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (:doc:`ServiceSubscription <ios-servicesubscription>` \*) **subscribeIsWebAppPinned**:(NSString \*)\ *webAppId* **success**:(WebAppPinStatusBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  webAppId

   -  **success**: success – Optional WebAppPinStatusBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

Typedefs
--------

WebAppLaunchSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~~

void(^)(:doc:`WebAppSession <ios-webappsession>`
\*webAppSession)

Success block that is called upon successfully launch of a web app.

-  webAppSession

   Object containing important information about the web app's session.
   This object is required to perform many functions with the web app,
   including app-to-app communication, media playback, closing, etc.
