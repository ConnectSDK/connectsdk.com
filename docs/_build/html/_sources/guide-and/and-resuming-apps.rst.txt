Resuming Apps
=============

It may be necessary for your app to resume from a background or closed
state and re-establish connection with a previously connected device.
There are many ways in which Connect SDK provides information to allow
for this behavior.

ConnectableDevice ID
~~~~~~~~~~~~~~~~~~~~

Each ConnectableDevice has a unique ID assigned to it upon creation.
When that device is connected to, the device store saves information
about each of the device's services. The unique ID persists across app
launches by attributing service UUIDs to the unique device ID in the
device store.

LaunchSession
~~~~~~~~~~~~~

The ability to interact with an app requires some information to
persist, including a session ID. This session ID may be required to
close the app, as well as allow the app to accurately track certain
state information.

WebAppSession
~~~~~~~~~~~~~

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

.. code-block:: java

   ConnectableDevice device; // device you've connected to

   SharedPreferences preferences = context.getSharedPreferences("MyPreferences", Context.MODE_PRIVATE);
   SharedPreferences.Editor editor = preferences.edit();

   editor.putString("recentDeviceId", device.getId());
   editor.commit();

Reconnect to device
~~~~~~~~~~~~~~~~~~~

.. code-block:: java

  ConnectableDevice mDevice;
  String mRecentDeviceId;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);

      SharedPreferences preferences = context.getSharedPreferences("MyPreferences", Context.MODE_PRIVATE);
      mRecentDeviceId = preferences.getString("recentDeviceId");

      DiscoveryManager.getInstance().setCapabilityFilters(myCapabilityFilters);
      DiscoveryManager.getInstance().addListener(this);
      DiscoveryManager.getInstance().start();
  }

  @Override
  public void onDeviceAdded(DiscoveryManager manager, ConnectableDevice device) {
      if (mRecentDeviceId != null && mDevice == null) {
          if (device.getId().equalsIgnoreCase(mRecentDeviceId)) {
              mDevice = device;
              device.addListener(this);
              device.connect();
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

.. code-block:: java

  WebAppSession webAppSession; // retrieved from WebAppLauncher launch success block

  LaunchSession launchSession = webAppSession.launchSession;
  JSONObject launchSessionInfo = launchSession.toJSONObject();

  SharedPreferences preferences = context.getSharedPreferences("MyPreferences", Context.MODE_PRIVATE);
  SharedPreferences.Editor editor = preferences.edit();

  editor.putString("launchSession", launchSessionInfo.toString());
  editor.commit();

Re-create session after device is connected/ready
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

   ConnectableDevice device; // device that has been re-discovered & re-connected
   WebAppSession.LaunchListener joinWebAppListener;

   SharedPreferences preferences = context.getSharedPreferences("MyPreferences", Context.MODE_PRIVATE);

   String launchSessionData = preferences.getString("launchSession");
   JSONObject launchSessionInfo = null;

   try {
       launchSessionInfo = new JSONObject(launchSessionData);
   } catch (JSONException ex) {

   }

   if (launchSessionInfo != null) {
       LaunchSession launchSession = LaunchSession.launchSessionFromJSONObject(launchSessionInfo);

       device.getWebAppLauncher().joinWebApp(launchSession, joinWebAppListener);
   }

Low-effort re-connection option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you could re-join your web app with just the web app id.
This could have the side effect of generating new session information
for your user, which may not be desired.

.. code-block:: java

   device.getWebAppLauncher().joinWebApp("your web app id", joinWebAppListener);

.. seealso::

   * :doc:`Discover & Connect to Device <and-discover-connect>`
   * :doc:`Checking Capabilities <and-checking-capabilities>`
   * :doc:`Beam Web Apps <and-beam-web-apps>`
