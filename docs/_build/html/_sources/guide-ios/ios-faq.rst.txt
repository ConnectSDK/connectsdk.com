FAQ
===

When do I start the DiscoveryManager?
-------------------------------------

We recommend starting the DiscoveryManager when the app is started so
that devices can be discovered and ready for use by the time the UI is
loaded.

If you need to start the discovery later or only during a specific
activity within your app you should be aware that it can take a few
seconds for devices to be discovered.

How do I reconnect to a device on resume?
-----------------------------------------

When your app goes into the background you can hold onto a
ConnectableDevice object. When your app resumes you have the reference
to the ConnectableDevice and you can listen for the Device ready
function. Once the device is ready you can call connect and begin using
it again.

How do I re-connect to a Web App when app resumes?
--------------------------------------------------

When a WebApp is launched on a TV you get a reference to that WebApp's
WebAppSession object. When your phone's application goes into the
background you can hold onto that WebAppSession object for the next time
your application is in the foreground. Once your app is in the
foreground again and you get a ConnectableDevice object.

.. code-block:: obj-c

   connectableDeviceReady:

Then once the method is called you can use the stored WebAppSession
object to continue to send commands to the running app.

How do I get the number of devices discovered?
----------------------------------------------

When you start an app you should always assume that there are 0 devices
discovered. Using the DiscoveryManagerDelegate you will be notified
whenever a new device is discovered and an existing device has been
lost.

.. code-block:: obj-c

   discoveryManager:didFindDevice:
   discoveryManager:didLoseDevice:

When either of these methods are called you can reference the
compatibleDevices property of the sharedManager to get a complete list
of devices that match your filters.

When there are no compatible devices your UI should reflect this by
hiding the beam icon.

How do create an ADHoc list of devices?
---------------------------------------

When you specify your device filters you may have devices that don't
support every feature. If you are searching for all devices that can
either display an image or play a YouTube video then you want to show a
list of all the devices that can show an image.

To do this you will need to check that each device in the
compatibleDevices array has the capabilities that you are looking for.

.. code-block:: obj-c

   - (NSArray *) getImageDevices
   {
       NSMutableArray *imageDevices = [NSMutableArray new];

       for (ConnectableDevice *device in [DiscoveryManager sharedManager].compatibleDevices)
       {
           if ([device hasCapability:kMediaPlayerDisplayImage])
               [imageDevices addObject:device];
       }

       return imageDevices;
   }

How do I show an image or video from my device?
-----------------------------------------------

All videos that are sent with the Connect SDK are links to external web
content and your device is no different. You can setup a quick HTTP
server and pass the url of your phone with Connect SDK. The media player
will reach to your HTTP server and stream your content right from there.

There are some pre-made libraries that already do the heavy lifting for
you.

Checkout:
`CocoaHTTPServer <https://github.com/robbiehanson/CocoaHTTPServer>`__
