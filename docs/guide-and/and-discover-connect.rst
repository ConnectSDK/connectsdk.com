Discover & Connect to Device
============================

Initial setup
-------------

Your view controller should implement delegate/listener methods for
Connect SDK's DevicePicker and ConnectableDevice classes. These methods
will give you the ability to respond to device selection, ready,
disconnect, and error states.

.. code-block:: java

   public class MainActivity extends Activity implements ConnectableDeviceListener {
   }

It is helpful to retain local references to both the DiscoveryManager
and the ConnectableDevice objects. In most use cases, these two classes
will serve to provide most of the functionality required.

As soon as your app loads, you should instantiate the DiscoveryManager
singleton and start discovery. As different devices can take a wide
range of time to be discovered, it is recommended that discovery start
as soon as possible after app launch.

.. code-block:: java

   private DiscoveryManager mDiscoveryManager;
   private ConnectableDevice mDevice;

This can be initialized in the the Application class or in your
Activity. You should always use getApplicationContext() since the
DiscoveryManager will likely hold onto this object longer than the life
of a single Activity.

.. code-block:: java

   @Override
   public void onCreate(Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);

       DiscoveryManager.init(getApplicationContext());

       // This step could even happen in your app's delegate
       mDiscoveryManager = DiscoveryManager.getInstance();
       mDiscoveryManager.start();
   }

Discovery & device selection
----------------------------

In many cases, your user will want to select one device from a list of
many. You should present the DevicePicker to the user to receive their
selection. The DevicePicker includes a dynamic listing of all devices
that have been discovered on the network.

.. code-block:: java

   private void showImage() {
       DevicePicker devicePicker = new DevicePicker(this);
       AlertDialog dialog = devicePicker.getPickerDialog("Show Image", selectDevice);
       dialog.show();
   }

Once the user has selected a device, you should immediately register for
events from that device and then call the connect method.

.. code-block:: java

   AdapterView.OnItemClickListener selectDevice = new AdapterView.OnItemClickListener() {
       @Override
       public void onItemClick(AdapterView<?> adapter, View parent, int position, long id) {
           mDevice = (ConnectableDevice) adapter.getItemAtPosition(position);
           mDevice.addListener(deviceListener);
           mDevice.connect();
       }
   }

Capability Filtering
~~~~~~~~~~~~~~~~~~~~

If your app is making use of certain device capabilities (media
playback/controls, web app launching, etc), it is strongly recommended
that you create filters with this information for DiscoveryManager.

Devices that are discovered & shown in the picker will be guaranteed to
have the set of capabilities that you have provided. This will prevent
your users from selecting a device that has not yet acquired all of its
protocols.

.. code-block:: java

  CapabilityFilter videoFilter = new CapabilityFilter(
          MediaPlayer.Display_Video,
          MediaControl.Any,
          VolumeControl.Volume_Up_Down
  );

  CapabilityFilter imageCapabilities = new CapabilityFilter(
          MediaPlayer.Display_Image
  );

  DiscoveryManager.getInstance().setCapabilityFilters(videoFilter, imageCapabilities);

Check out the article on :doc:`capabilities <and-checking-capabilities>` for more depth on this topic.
