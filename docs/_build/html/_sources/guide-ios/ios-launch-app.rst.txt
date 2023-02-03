Launch App on TV
================

Many TVs and streaming players include support for launching installed
apps. The following is a simplified example of how to launch YouTube on
a device.

Launch an app
-------------

.. code-block:: obj-c

   [_device.launcher launchApp:@"YouTube" success:^(LaunchSession *launchSession) {
       NSLog(@"app launch success");
   } failure:^(NSError *error) {
       NSLog(@"app launch error: %@", error.localizedDescription);
   }];

Device-specific app identifiers
-------------------------------

On each device (webOS TV, Roku, etc) apps are identified by different
values. Here is an example of the different identifiers in use for the
YouTube app.

-  webOS: youtube.leanback.v4 (value may change with future updates)
-  Netcast: 0000000000017498 (value may be different on each TV)
-  DIAL: YouTube (listed in `DIAL
   registry <http://www.dial-multiscreen.org/dial-registry/namespace-database>`__)
-  Roku: 837 (Roku-specific channel number)

Launching an app with device-specific identifiers
-------------------------------------------------

The following snippet shows how to detect the platform of your device
and launch with the appropriate app identifier.

.. code-block:: obj-c

   NSString *appId;

   if ([_device serviceWithName:@"webOS TV"])
       appId = @"youtube.leanback.v4";
   else if ([_device serviceWithName:@"Netcast TV"])
       appId = @"0000000000017498";
   else if ([_device serviceWithName:@"Roku"])
       appId = @"837";
   else if ([_device serviceWithName:@"DIAL"])
       appId = @"YouTube";

   if (!appId)
       return;

   AppInfo *appInfo = [AppInfo appInfoForId:appId];
   appInfo.name = @"YouTube";

   [_device.launcher launchAppWithInfo:appInfo success:^(LaunchSession *launchSession) {
       NSLog(@"app launch success");
   } failure:^(NSError *error) {
       NSLog(@"app launch error: $@", error.localizedDescription);
   }];

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

.. code-block:: obj-c

   NSDictionary *params = @{
       @"someProperty" : @"someValue"
   };

   [_device.launcher launchAppWithInfo:appInfo params:params success:^(LaunchSession *launchSession) {
       NSLog(@"app launch success");
   } failure:^(NSError *error) {
       NSLog(@"app launch error: $@", error.localizedDescription);
   }];

.. note::

   Due to the variety of protocols in use, it is strongly recommended that
   you only use strings for the keys AND values of your parameters.
