WebAppLauncher 
===============================================================
``com.connectsdk.service.capability.WebAppLauncher``

*extends CapabilityMethods*

The WebAppLauncher capability protocol provides capabilities for
launching web apps and establishing two-way communication.

Properties
----------

**final String Any = "WebAppLauncher.Any"**

**final String Launch = "WebAppLauncher.Launch"**

**final String Launch_Params = "WebAppLauncher.Launch.Params"**

**final String Message_Send = "WebAppLauncher.Message.Send"**

**final String Message_Receive = "WebAppLauncher.Message.Receive"**

**final String Message_Send_JSON = "WebAppLauncher.Message.Send.JSON"**

**final String Message_Receive_JSON = "WebAppLauncher.Message.Receive.JSON"**

**final String Connect = "WebAppLauncher.Connect"**

**final String Disconnect = "WebAppLauncher.Disconnect"**

**final String Join = "WebAppLauncher.Join"**

**final String Close = "WebAppLauncher.Close"**

**final String Pin = "WebAppLauncher.Pin"**

**final String[] Capabilities = { Launch, Launch_Params, Message_Send, Message_Receive, Message_Send_JSON, Message_Receive_JSON, Connect, Disconnect, Join, Close, Pin }**

Methods
-------

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

void **launchWebApp** (String *webAppId*, boolean *relaunchIfRunning*, LaunchListener *listener*)
   
    Launch a web application on the TV.

    **Related capabilities:**
        * ``WebAppLauncher.Launch``
        * ``WebAppLauncher.Launch.Params`` – if launching with params

    **Parameters:**
        * webAppId – ID of web app assigned by platform vendor
        * relaunchIfRunning – If supported on target platform, web app will force relaunch if value true
        * listener – (optional) LaunchListener with methods to be called on success or failure

void **launchWebApp** (String *webAppId*, JSONObject *params*, LaunchListener *listener*)
   
    Launch a web application on the TV.

    **Related capabilities:**
        * ``WebAppLauncher.Launch``
        * ``WebAppLauncher.Launch.Params`` – if launching with params

    **Parameters:**
        * webAppId – ID of web app assigned by platform vendor
        * params – Dictionary of key/value strings. Not available on all target platforms
        * listener – (optional) LaunchListener with methods to be called on success or failure

void **launchWebApp** (String *webAppId*, JSONObject *params*, boolean *relaunchIfRunning*, LaunchListener *listener*)
    
    Launch a web application on the TV.

    **Related capabilities:**
        * ``WebAppLauncher.Launch``
        * ``WebAppLauncher.Launch.Params`` – if launching with params

    **Parameters:**
        * webAppId – ID of web app assigned by platform vendor
        * params – Dictionary of key/value strings. Not available on all target platforms
        * relaunchIfRunning – If supported on target platform, web app will force relaunch if value true
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

void **joinWebApp** (String *webAppId*, LaunchListener *listener*)
    
    Join an active web app without launching/relaunching. If the app is
    not running/joinable, the failure block will be called immediately.

    **Related capabilities:**
        * ``WebAppLauncher.Send``
        * ``WebAppLauncher.Receive``

    **Parameters:**
        * webAppId – Unique identifier for the web app to be joined
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
