Resuming Apps
=============

It may be necessary for your app to resume from a background or closed
state and re-establish connection with a previously connected device.
There are many ways in which Connect SDK provides information to allow
for this behavior.

ConnectableDevice ID
--------------------

Each ConnectableDevice has a unique ID assigned to it upon creation.
When that device is connected to, the device store saves information
about each of the device's services. The unique ID persists across app
launches by attributing service UUIDs to the unique device ID in the
device store.

LaunchSession
-------------

The ability to interact with an app requires some information to
persist, including a session ID. This session ID may be required to
close the app, as well as allow the app to accurately track certain
state information.

WebAppSession
-------------

The ability to communicate with a web app requires a LaunchSession
object and/or the web app id.

Resuming most recent connection
-------------------------------

In order to save & reconnect to a previously connected device, all you
need to keep track of is the device's ID. Assuming you are using the
ConnectableDeviceStore included with Connect SDK, previously connected
devices will persist the same ID between app launches.

When your app restarts, you should immediately start discovery and
listen for device found events from DiscoveryManager. In these events,
you can check each device's ID and call ``connect`` on the previously
connected device.

Important note about reconnecting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just because your device has been discovered on the network doesn't mean
that all of its services/capabilities are available. You will need to
set a CapabilityFilter on DiscoveryManager or manually check the
ConnectableDevice's capabilities before you call ``connect``.

Save device ID to disk
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: obj-c

   ConnectableDevice *device; // device you've connected to

   [[NSUserDefaults standardUserDefaults] setObject:device.id forKey:@"recentDeviceId"];

   // save right away before entering background
   [NSUserDefaults standardUserDefaults] synchronize];

Reconnect to device
~~~~~~~~~~~~~~~~~~~

.. code-block:: obj-c

   ConnectableDevice *mDevice;
   NSString *mRecentDeviceId;

   - (void) viewDidLoad {
       [super viewDidLoad];

       mRecentDeviceId = [[NSUserDefaults standardUserDefaults] objectForKey:@"recentDeviceId"];

       [[DiscoveryManager sharedManager] setCapabilityFilters:myCapabilityFilters];
       [[DiscoveryManager sharedManager] setDelegate:self];
       [[DiscoveryManager sharedManager] start];
   }

   - (void) discoveryManager:(DiscoveryManager *)manager didFindDevice:(ConnectableDevice *)device {
       if (mRecentDeviceId && !mDevice) {
           if ([device.id isEqualToString:mRecentDeviceId]) {
               mDevice = device;
               [device setDelegate:self];
               [device connect];
           }
       }
   }

Resuming a web app session
--------------------------

Resuming a web app session is as simple as saving the WebAppSession's
LaunchSession object before entering the background. It can even be
serialized into a JSON object for easy cross-platform storage.

Save session info to disk
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: obj-c

   WebAppSession *webAppSession; // retrieved from WebAppLauncher launch success block

   LaunchSession *launchSession = webAppSession.launchSession;
   NSDictionary *launchSessionInfo = [launchSession toJSONObject];

   [[NSUserDefaults standardUserDefaults] setObject:launchSessionInfo forKey:@"launchSession"];

   // save right away before entering background
   [NSUserDefaults standardUserDefaults] synchronize];

Re-create session after device is connected/ready
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: obj-c

   ConnectableDevice *device; // device that has been re-discovered & re-connected

   NSDictionary *launchSessionInfo = (NSDictionary *) [[NSUserDefaults standardUserDefaults] objectForKey:@"launchSession"];
   LaunchSession *launchSession = [LaunchSession launchSessionFromJSONObject:launchSessionInfo];

   [device.webAppLauncher joinWebApp:launchSession
                             success:^(WebAppSession *webAppSession) { }
                             failure:^(NSError *) { } ];

Low-effort re-connection option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you could re-join your web app with just the web app id.
This could have the side effect of generating new session information
for your user, which may not be desired.

.. code-block:: obj-c

   [device.webAppLauncher joinWebAppWithId:@"your web app id"
                                   success:^(WebAppSession *webAppSession) { }
                                   failure:^(NSError *) { } ];

.. seealso::

   * :doc:`Discover & Connect to Device <ios-discover-connect>`
   * :doc:`Checking Capabilities <ios-checking-capabilities>`
   * :doc:`Beam Web Apps <ios-beam-web-apps>`
