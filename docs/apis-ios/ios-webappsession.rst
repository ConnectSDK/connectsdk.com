WebAppSession
=============

Overview
--------

When a web app is launched on a first screen device, there are certain
tasks that can be performed with that web app. WebAppSession serves as a
second screen reference of the web app that was launched. It behaves
similarly to LaunchSession, but is not nearly as static.

In Depth
--------

On top of maintaining session information (contained in the
launchSession property), WebAppSession provides access to a number of
capabilities.

-  MediaPlayer

-  MediaControl

-  Bi-directional communication with web app

MediaPlayer and MediaControl are provided to allow for the most common
first screen use cases a media player (audio, video, & images).

The Connect SDK JavaScript Bridge has been produced to provide
normalized support for these capabilities across protocols (Chromecast,
webOS, etc).

Properties
----------

:doc:`LaunchSession <ios-launchsession>` \* launchSession
   LaunchSession object containing key session information. Much of this
   information is required for web app messaging & closing the web app.

:doc:`DeviceService <ios-deviceservice>` \* service
   DeviceService that was responsible for launching this web app.

id<:doc:`WebAppSessionDelegate <ios-webappsessiondelegate>`> delegate
   When messages are received from a web app, they are parsed into the
   appropriate object type (string vs JSON/NSDictionary) and routed to
   the WebAppSessionDelegate.

Methods
-------

\- (instancetype) **initWithLaunchSession**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *launchSession* **service**:(:doc:`DeviceService <ios-deviceservice>` \*)\ *service*
   Instantiates a WebAppSession object with all the information
   necessary to interact with a web app.

   **Parameters:**

   -  launchSession – LaunchSession containing info about the web app session

   -  **service**: service – DeviceService that was responsible for launching this web app

\- (:doc:`ServiceSubscription <ios-servicesubscription>` \*) **subscribeWebAppStatus**:(`WebAppStatusBlock <#webappstatusblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribes to changes in the web app's status.

   **Parameters:**

   -  success – (optional) WebAppStatusBlock to be called on app status change

   -  **failure**: failure – (optional) FailureBlock to be called on failure

\- (void) **joinWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Join an active web app without launching/relaunching. If the app is
   not running/joinable, the failure block will be called immediately.

   **Parameters:**

   -  success – (optional) SuccessBlock to be called on join success

   -  **failure**: failure – (optional) FailureBlock to be called on failure

\- (void) **closeWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Closes the web app on the first screen device.

   **Parameters:**

   -  success – (optional) SuccessBlock to be called on success

   -  **failure**: failure – (optional) FailureBlock to be called on failure

\- (void) **connectWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Establishes a communication channel with the web app.

   **Parameters:**

   -  success – (optional) SuccessBlock to be called on success

   -  **failure**: failure – (optional) FailureBlock to be called on failure

\- (void) **disconnectFromWebApp**
   Closes any open communication channel with the web app.

\- (void) **pinWebApp**:(NSString \*)\ *webAppId* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Pin the web app on the launcher.

   **Parameters:**

   -  webAppId – NSString webAppId to be pinned.

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **unPinWebApp**:(NSString \*)\ *webAppId* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   UnPin the web app on the launcher.

   **Parameters:**

   -  webAppId – NSString webAppId to be unpinned.

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **isWebAppPinned**:(NSString \*)\ *webAppId* **success**:(`WebAppPinStatusBlock <#webapppinstatusblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   To check if the web app is pinned or not

   **Parameters:**

   -  webAppId

   -  **success**: success – Optional WebAppPinStatusBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **sendText**:(NSString \*)\ *message* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends a simple string to the web app. The Connect SDK JavaScript
   Bridge will receive this message and hand it off as a string object.

   **Parameters:**

   -  message

   -  **success**: success – (optional) SuccessBlock to be called on success

   -  **failure**: failure – (optional) FailureBlock to be called on failure

\- (void) **sendJSON**:(NSDictionary \*)\ *message* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends a JSON object to the web app. The Connect SDK JavaScript Bridge
   will receive this message and hand it off as a JavaScript object.

   **Parameters:**

   -  message

   -  **success**: success – (optional) SuccessBlock to be called on success

   -  **failure**: failure – (optional) FailureBlock to be called on failure

Typedefs
--------

WebAppStatusBlock
~~~~~~~~~~~~~~~~~

void(^)(:doc:`WebAppStatus <ios-webappstatus>` status)

Success block that is called upon successfully getting a web app's
status.

-  status

   The current running & foreground status of the web app

WebAppPinStatusBlock
~~~~~~~~~~~~~~~~~~~~

void(^)(BOOL status)

Success block that is called upon successfully getting a web app's
status.

-  status

   The current running & foreground status of the web app
