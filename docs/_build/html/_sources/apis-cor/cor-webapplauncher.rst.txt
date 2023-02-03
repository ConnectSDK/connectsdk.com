WebAppLauncher
==============

The WebAppLauncher capability protocol provides capabilities for
launching web apps and establishing two-way communication.

Methods
-------

webAppLauncher.\ **launchWebApp** (*webAppId*, *params*)
   Launch a web application on the TV.

   See WebAppSession for a detailed example.

   On success, the success event/callback will be fired with the
   arguments (webAppSession)

   -  webAppSession: WebAppSession

   **Related capabilities:**

   -  ``WebAppLauncher.Launch``

   -  ``WebAppLauncher.Launch.Params`` – if launching with params

   **Parameters:**

   -  webAppId (string) – ID of web app assigned by platform vendor

   -  params (object) – Dictionary of key/value strings. Not available on all target
      platforms

   **Returns:** :doc:`Command <cor-command>`

webAppLauncher.\ **joinWebApp** (*webAppId*, *params*)
   Join an active web app without launching/relaunching. If the app is
   not running/joinable, the failure block will be called immediately.

   On success, the success event/callback will be fired with the
   arguments (webAppSession)

   -  webAppSession: WebAppSession

   **Related capabilities:**

   -  ``WebAppLauncher.Send``
   -  ``WebAppLauncher.Receive``

   **Parameters:**

   -  webAppId (string) – Unique identifier for the web app to be joined

   -  params (object)

   **Returns:** :doc:`Command <cor-command>`

webAppLauncher.\ **closeWebApp** (*webAppId*)
   Closes a web app with the provided LaunchSession.

   **Related capabilities:**

   -  ``WebAppLauncher.Close``

   **Parameters:**

   -  webAppId (string)

   **Returns:** :doc:`Command <cor-command>`

webAppLauncher.\ **pinWebApp** (*webAppId*)
   **Parameters:**

   -  webAppId (string)

   **Returns:** :doc:`Command <cor-command>`

webAppLauncher.\ **unPinWebApp** (*webAppId*)
   **Parameters:**

   -  webAppId (string)

   **Returns:** :doc:`Command <cor-command>`

webAppLauncher.\ **isWebAppPinned** (*webAppId*)
   **Parameters:**

   -  webAppId (string)

   **Returns:** :doc:`Command <cor-command>`

webAppLauncher.\ **subscribeIsWebAppPinned** (*webAppId*)
   **Parameters:**

   -  webAppId (string)

   **Returns:** :doc:`Command <cor-command>`
