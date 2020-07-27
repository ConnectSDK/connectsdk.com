Launch App on TV
================

Many TVs and streaming players include support for launching installed
apps. The following is a simplified example of how to launch YouTube on
a device.

Launch an app
-------------

.. code-block:: java

   // This variable should be a class field
   // ConnectableDevice mDevice;
   mDevice.getLauncher().launchApp("YouTube", new Launcher.AppLaunchListener() {

       @Override
       public void onError(ServiceCommandError error) {
           Log.d("App Tag", "App Launch error: " + error);
       }

       @Override
       public void onSuccess(LaunchSession object) {
           Log.d("App Tag", "App Launch success.");
       }
   });

Device-specific app identifiers
-------------------------------

On each device (webOS TV, Roku, etc) apps are identified by different
values. Here is an example of the different identifiers in use for the
YouTube app.

-  webOS: youtube.leanback.v4 (value may change with future updates)
-  Netcast: 0000000000017498 (value may be different on each TV)
-  DIAL: YouTube (listed in `DIAL registry`_)
-  Roku: 837 (Roku-specific channel number)

.. _DIAL registry: http://www.dial-multiscreen.org/dial-registry/namespace-database

Launching an app with device-specific identifiers
-------------------------------------------------

The following snippet shows how to detect the platform of your device
and launch with the appropriate app identifier.

.. code-block:: java

   String appId = null;
   // This should be a class field
   // ConnectableDevice mDevice;

   if (mDevice.getServiceByName(WebOSTVService.ID) != null)
       appId = "youtube.leanback.v4";
   else if (mDevice.getServiceByName(NetcastTVService.ID) != null)
       appId = "0000000000017498";
   else if (mDevice.getServiceByName(RokuService.ID) != null)
       appId = "837";
   else if (mDevice.getServiceByName(DIALService.ID) != null)
       appId = "YouTube";

   if (appId == null)
       return;

   mDevice.getLauncher().launchApp(appId, new Launcher.AppLaunchListener() {

       @Override
       public void onError(ServiceCommandError error) {
           Log.d("App Tag", "App Launch error: " + error);
       }

       @Override
       public void onSuccess(LaunchSession object) {
           Log.d("App Tag", "App Launch success.");
       }
   });

AppInfo helper object
~~~~~~~~~~~~~~~~~~~~~

You will notice that the previous example refers to an AppInfo object.
This object is used internally by Connect SDK to manage an app's
protocol-specific properties. If a device supports app list, the app
list will return a set of AppInfo objects for each app installed on the
TV.

Launching an app with parameters
--------------------------------

In most cases, a device's launcher object will allow you to pass launch
parameters to your app. Connect SDK has normalized the parameter input
type to a keyed set of values. These values are then parsed into the
appropriate format for the protocol (XML, JSON, URL params, etc).

.. code-block:: java

   // This should be a class field
   // ConnectableDevice mDevice;

   JSONObject params = null;
   try {
       params = new JSONObject() {{
           put("someProperty", "someValue");
       }};
   } catch (JSONException e) {
       e.printStackTrace();
   }

   AppInfo appInfo = new AppInfo("your_app_id");
   mDevice.getLauncher().launchAppWithInfo(appInfo, params, new Launcher.AppLaunchListener() {

       @Override
       public void onError(ServiceCommandError error) {
           Log.d("App Tag", "App Launch error: " + error);
       }

       @Override
       public void onSuccess(LaunchSession object) {
           Log.d("App Tag", "App Launch success.");
       }
   });

.. note::

   Due to the variety of protocols in use, it is strongly recommended that you
   only use strings for the keys AND values of your parameters.
