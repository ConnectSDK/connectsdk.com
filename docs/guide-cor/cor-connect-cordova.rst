Discover & Connect to Device
============================

This guide assumes you're working with a brand new Cordova app as
described in the :doc:`Setup Instructions <cor-setup-instructions>`. It will show you how to add a
button that selects a supported smart TV on your local WiFi network and
displays a video.

Adding a device picker button
-----------------------------

Open hello_connect/www/index.html in your preferred editor. Let's add a
new button:

.. code-block:: html

   <div class="app">
     <h1>Apache Cordova</h1>
     <button onclick="app.showDevicePicker()">Select a TV</button>

Open hello_connect/www/js/index.js in your preferred text editor. Find
the "onDeviceReady" method, which is called when Cordova is finished
initializing. At the end, add the following line:

.. code-block:: javascript

   app.setupDiscovery();

Next, add a new method to the app object called setupDiscovery:

.. code-block:: javascript

   setupDiscovery: function () {
       ConnectSDK.discoveryManager.startDiscovery();
   }

Now let's add a handler for the button:

.. code-block:: javascript

   showDevicePicker: function () {
       ConnectSDK.discoveryManager.pickDevice();
   }

Let's build and run the modified example. If you are building through
Xcode/Android Studio you will need to run the following command to
update the projects.

::

   cordova prepare

Otherwise, you can simply build with the Cordova tools</>

::

   cordova build

Connecting to a device
----------------------

If the app launch went well, you should be able to click on the "Select
a TV" button to bring up a picker.

Next, we should allow the user to actually do something with the TV.

Open hello_connect/www/js/index.js again. We'll modify showDevicePicker
to talk to the TV by chaining a *success* callback that will be called
when a device is selected. This function will be called with a device
object as the first argument, which we can use to send a video URL to
the TV.

.. code-block:: javascript

   showDevicePicker: function () {
       ConnectSDK.discoveryManager.pickDevice().success(function (device) {
           function sendVideo () {
               device.getMediaPlayer().playMedia("http://media.w3.org/2010/05/sintel/trailer.mp4", "video/mp4");
           }

           if (device.isReady()) { // already connected
               sendVideo();
           } else {
               device.on("ready", sendVideo);
               device.connect();
           }
       })
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

.. code-block:: javascript

  var videoFilter = new ConnectSDK.CapabilityFilter([
     ConnectSDK.Capabilities.MediaPlayer.Play.Video,
     ConnectSDK.Capabilities.MediaControl.Any,
     ConnectSDK.Capabilities.VolumeControl.UpDown
  ]);

  var imageFilter = new ConnectSDK.CapabilityFilter([
      ConnectSDK.Capabilities.MediaPlayer.Display.Image
  ]);

  ConnectSDK.discoveryManager.setCapabilityFilters([videoFilter, imageFilter]);

  app.setupDiscovery();
