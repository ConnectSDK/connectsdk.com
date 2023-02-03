Launcher
========

The Launcher capability protocol serves to define the methods required
for normalizing the launching of apps. It allows for in-built support
for certain common launch types (deep-linking to YouTube, Netflix, Hulu,
browser, etc) as well as by (platform-specific) app id.

Methods
-------

launcher.\ **launchApp** (*appId*)
   Launch an application on the device.

   On success, the success event/callback will be fired with the
   arguments (launchSession)

   -  launchSession: LaunchSession

   **Related capabilities:**

   -  ``Launcher.App``

   **Parameters:**

   -  appId (string) – ID of the application

   **Returns:** :doc:`Command <cor-command>`

launcher.\ **closeApp** (*appId*)
   Close an application on the device.

   **Related capabilities:**

   -  ``Launcher.App.Close``

   **Parameters:**

   -  appId (string)

   **Returns:** :doc:`Command <cor-command>`

launcher.\ **launchAppStore** (*appId*)
   Launch the device's app store app, optionally deep-linked to a
   specific app's page.

   On success, the success event/callback will be fired with the
   arguments (launchSession)

   -  launchSession: LaunchSession

   **Related capabilities:**

   -  ``Launcher.AppStore``
   -  ``Launcher.AppStore.Params``

   **Parameters:**

   -  appId (string) – (optional) ID of the application to show in the app store

   **Returns:** :doc:`Command <cor-command>`

launcher.\ **launchBrowser** (*url*)
   Launch the web browser. Will launch deep-linked to provided URL, if
   supported on the target platform.

   On success, the success event/callback will be fired with the
   arguments (launchSession)

   -  launchSession: LaunchSession

   **Related capabilities:**

   -  ``Launcher.Browser``

   -  ``Launcher.Browser.Params`` – if launching with url

   **Parameters:**

   -  url (string)

   **Returns:** :doc:`Command <cor-command>`

launcher.\ **launchHulu** (*contentId*)
   Launch Hulu app. Will launch deep-linked to provided contentId, if
   supported on the target platform.

   On success, the success event/callback will be fired with the
   arguments (launchSession)

   -  launchSession: LaunchSession

   **Related capabilities:**

   -  ``Launcher.Hulu``

   -  ``Launcher.Hulu.Params`` – if launching with contentId

   **Parameters:**

   -  contentId (string) – Video id to open

   **Returns:** :doc:`Command <cor-command>`

launcher.\ **launchNetflix** (*contentId*)
   Launch Netflix app. Will launch deep-linked to provided contentId, if
   supported on the target platform.

   On success, the success event/callback will be fired with the
   arguments (launchSession)

   -  launchSession: LaunchSession

   **Related capabilities:**

   -  ``Launcher.Netflix``

   -  ``Launcher.Netflix.Params`` – if launching with contentId

   **Parameters:**

   -  contentId (string) – Video id to open

   **Returns:** :doc:`Command <cor-command>`

launcher.\ **launchYouTube** (*contentId*)
   Launch YouTube app. Will launch deep-linked to provided contentId, if
   supported on the target platform.

   On success, the success event/callback will be fired with the
   arguments (launchSession)

   -  launchSession: LaunchSession

   **Related capabilities:**

   -  ``Launcher.YouTube``

   -  ``Launcher.YouTube.Params`` – if launching with contentId

   **Parameters:**

   -  contentId (string) – Video id to open

   **Returns:** :doc:`Command <cor-command>`

launcher.\ **getAppList** ()
   Gets a list of all apps installed on the device.

   On success, the success event/callback will be fired with the
   arguments (appList)

   -  appList: AppInfo[] – Each AppInfo object contains:

      -  id (string): platform-specific appId
      -  name (string): human-readable name of app

   **Related capabilities:**

   -  ``Launcher.App.List``

   **Returns:** :doc:`Command <cor-command>`
