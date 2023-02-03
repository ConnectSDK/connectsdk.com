Launch App on TV
================

Many TVs and streaming players include support for launching installed
apps. The following is a simplified example of how to launch YouTube on
a device.

Launch an app
-------------

.. code-block:: javascript

   device.getLauncher().launchApp("YouTube").success(function (launchSesssion) {
       console.log("app launch success");
   }).error(function (err) {
       console.log("app launch error: " + err.message);
   });

Device-specific app identifiers
-------------------------------

On each device (webOS TV, Roku, etc) apps are identified by different
values. Here is an example of the different identifiers in use for the
YouTube app.

*  webOS: youtube.leanback.v4 (value may change with future updates)
*  Netcast: 0000000000017498 (value may be different on each TV)
*  DIAL: YouTube (listed in `DIAL registry`_)
*  Roku: 837 (Roku-specific channel number)

.. _DIAL registry: http://www.dial-multiscreen.org/dial-registry/namespace-database

Launching an app with device-specific identifiers
-------------------------------------------------

The following snippet shows how to detect the platform of your device
and launch with the appropriate app identifier.

.. code-block:: javascript

   var appId;

   if (device.hasService(ConnectSDK.Services.WebOSTV)) {
       appId = "youtube.leanback.v4";
   } else if (device.hasService(ConnectSDK.Services.NetcastTV)) {
       appId = "0000000000017498";
   } else if (device.hasService(ConnectSDK.Services.Roku)) {
       appId = "837";
   } else if (device.hasService(ConnectSDK.Services.DIAL)) {
       appId = "YouTube";
   }

   if (!appId) {
       return;
   }

   device.getLauncher().launchApp(appId).success(function (launchSesssion) {
       console.log("app launch success");
   }).error(function (err) {
       console.log("app launch error: " + err.message);
   });

Launching an app with parameters
--------------------------------

In most cases, a device's launcher object will allow you to pass launch
parameters to your app. Connect SDK has normalized the parameter input
type to a keyed set of values. These values are then parsed into the
appropriate format for the protocol (XML, JSON, URL params, etc).

.. code-block:: javascript

   var params = {
       "someKey": "someValue"
   }

   device.getLauncher().launchApp(appId, params).success(function (launchSesssion) {
       console.log("app launch success");
   }).error(function (err) {
       console.log("app launch error: " + err.message);
   });

.. important::
   Due to the variety of protocols in use, it is strongly recommended that
   you only use strings for the keys AND values of your parameters.
