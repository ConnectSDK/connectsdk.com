Launcher
===================================================
``com.connectsdk.service.capability.Launcher``

*extends CapabilityMethods*

The Launcher capability protocol serves to define the methods required
for normalizing the launching of apps. It allows for in-built support
for certain common launch types (deep-linking to YouTube, Netflix, Hulu,
browser, etc) as well as by (platform-specific) app id.

Properties
----------

final String Any = "Launcher.Any"

final String Application = "Launcher.App"

final String Application_Params = "Launcher.App.Params"

final String Application_Close = "Launcher.App.Close"

final String Application_List = "Launcher.App.List"

final String Browser = "Launcher.Browser"

final String Browser_Params = "Launcher.Browser.Params"

final String Hulu = "Launcher.Hulu"

final String Hulu_Params = "Launcher.Hulu.Params"

final String Netflix = "Launcher.Netflix"

final String Netflix_Params = "Launcher.Netflix.Params"

final String YouTube = "Launcher.YouTube"

final String YouTube_Params = "Launcher.YouTube.Params"

final String AppStore = "Launcher.AppStore"

final String AppStore_Params = "Launcher.AppStore.Params"

final String AppState = "Launcher.AppState"

final String AppState_Subscribe = "Launcher.AppState.Subscribe"

final String RunningApp = "Launcher.RunningApp"

final String RunningApp_Subscribe = "Launcher.RunningApp.Subscribe"

final String[] Capabilities = { Application, Application_Params, Application_Close, Application_List, Browser, Browser_Params, Hulu, Hulu_Params, Netflix, Netflix_Params, YouTube, YouTube_Params, AppStore, AppStore_Params, AppState, AppState_Subscribe, RunningApp, RunningApp_Subscribe }

Inner Classes
-------------

*  :doc:`AppInfoListener <and-appinfolistener>`
*  :doc:`AppLaunchListener <and-applaunchlistener>`
*  :doc:`AppListListener <and-applistlistener>`
*  :doc:`AppState <and-appstate>`
*  :doc:`AppStateListener <and-appstatelistener>`

Methods
-------

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

void **launchAppWithInfo** (:doc:`AppInfo <and-appinfo>` *appInfo*, Object *params*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
     Launch an application on the device.

     **Related capabilities:**

     * ``Launcher.App``
     * ``Launcher.App.Params`` – if launching with params

     **Parameters:**

     * appInfo – AppInfo object for the application
     * params
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
     app's state changes, the success block will be called with info on the app's running status and on-screen visibility.

     **Related capabilities:**

     * ``Launcher.AppState.Subscribe``

     **Parameters:**

     * launchSession - LaunchSession of the target app
     * listener – (optional) AppStateListener with methods to be called on success or failure

void **launchBrowser** (String *url*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
     Launch the web browser. Will launch deep-linked to provided URL, if supported on the target platform.

     **Related capabilities:**

     * ``Launcher.Browser``
     * ``Launcher.Browser.Params`` – if launching with url

     **Parameters:**

     * url
     * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchYouTube** (String *contentId*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
     Launch YouTube app. Will launch deep-linked to provided contentId, if supported on the target platform.

     **Related capabilities:**

     * ``Launcher.YouTube``
     *  ``Launcher.YouTube.Params`` – if launching with contentId

     **Parameters:**

     * contentId – Video id to open
     * listener – (optional) AppLaunchListener with methods to be called on success or failure

void **launchYouTube** (String *contentId*, float *startTime*, :doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
     Launch YouTube app. Will launch deep-linked to provided contentId, if supported on the target platform.

     **Related capabilities:**

     * ``Launcher.YouTube``
     * ``Launcher.YouTube.Params`` – if launching with contentId

     **Parameters:**

     * contentId – Video id to open
     * startTime
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
