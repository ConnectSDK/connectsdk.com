Beam Web Apps
=============

There are several platforms available that support the launching of web
apps. A web app is typically run on a temporary basis in a full-screen
browser instance.

Web App IDs
-----------

Both webOS and Chromecast require a web app ID for API calls to launch
and communicate with web apps. This web app ID is translated into your
web app's URL on web app launch.

For information on creating a web app ID for webOS, please visit the `LG
registration site <http://lgsvl.com/connectSDK/index.php>`__.

To learn how to register for a Chromecast web app ID, visit `Google's
app ID registration
site <https://developers.google.com/cast/docs/registration>`__.

Launch web app with identifier
------------------------------

Connect SDK currently supports web app launching on webOS, Chromecast,
and Apple TV devices. Both webOS and Chromecast will translate a web app
identifier into your web app's URL.

.. code-block:: obj-c

   NSString *webAppId;

   if ([_device serviceWithName:@"webOS TV"])
       webAppId = @"5G7328DE";
   else if ([_device serviceWithName:@"Chromecast"])
       webAppId = @"3E5106AB";
   else if ([_device serviceWithName:@"AirPlay"])
       webAppId = @"http://www.example.com/";

   if (!webAppId)
       return;

   [_device.webAppLauncher launchWebApp:webAppId success:^(WebAppSession *webAppSession) {
       NSLog(@"web app launch success");
   } failure:^(NSError *error) {
       NSLog(@"web app launch error: %@", error.localizedDescription);
   }];

Communicate with web app
------------------------

Bi-directional communication with your web app is made extremely simple.
Data can be sent and received strongly-typed as a string or a keyed set
of values (JSON object).

.. code-block:: obj-c

   WebAppSession *_webAppSession;

   [_device.webAppLauncher launchWebApp:webAppId success:^(WebAppSession *webAppSession) {
       NSLog(@"web app launch success");

       _webAppSession = webAppSession;
       _webAppSession.delegate = self;

       [_webAppSession connectWithSuccess:^(id responseObject) {
           NSLog(@"web app connect success");
       } failure:^(NSError *error) {
           NSLog(@"web app connect error: %@", error.localizedDescription);
       }];
   } failure:^(NSError *error) {
       NSLog(@"web app launch error: %@", error.localizedDescription);
   }];

After successfully establishing a connection, you can send messages to
your web app.

.. code-block:: obj-c

   [_webAppSession sendText:@"This is a test message" success:nil failure:nil];

You can also send an NSDictionary which will be received by the web app
as a JSON object.

.. code-block:: obj-c

   NSDictionary *message = @{
       @"someParameter" : @"someValue",
       @"anArray": @[
           @"array value 1",
           @"array value 2",
           @"array value 3"
       ],
       @"anotherObject" : @{
           @"anotherParameter" : @"anotherValue"
       }
   };

   [_webAppSession sendJSON:message success:nil failure:nil];

WebAppSessionDelegate allows you to receive messages from your web app.

.. code-block:: obj-c

  <code>::

   - (void) webAppSession:(WebAppSession *)webAppSession didReceiveMessage:(id)message {
       // message may be either an NSString or an NSDictionary, depending on what was sent from the web app
       NSLog(@"Received message from web app %@", message);
   }

Beam media to web app
---------------------

A common use case for web apps is the playback and control of media
files. Connect SDK provides capabilities for directly
playing/controlling media on a WebAppSession, provided that web app has
integrated the :doc:`Connect SDK JavaScript
Bridge <../guide-web/index>`.

Rather than calling playMedia on your device's mediaPlayer,
webAppSession provides its own mediaPlayer. After media has been beamed
into the web app, the control is just like any other media session.

.. code-block:: obj-c

   MediaInfo *mediaInfo = [[MediaInfo alloc] initWithURL:mediaURL mimeType:mimeType];
   mediaInfo.title = title;
   mediaInfo.description = description;
   ImageInfo *imageInfo = [[ImageInfo alloc] initWithURL:iconURL type:ImageTypeThumb];
   [mediaInfo addImage:imageInfo];

   [webAppSession.mediaPlayer playMediaWithMediaInfo:mediaInfo
                                          shouldLoop:NO
                                             success:
    ^(MediaLaunchObject *mediaLaunchObject) {
        NSLog(@"play video success");

        // save the object reference to control media playback
        launchObject = mediaLaunchObject;

        // enable your media control UI elements here
    }
                                             failure:
    ^(NSError *error) {
        NSLog(@"play video failure: %@", error.localizedDescription);
    }];

.. note::
   For beaming media to AirPlay devices, you must set the
   :doc:`AirPlayServiceMode <../apis-ios/ios-airplayservicemode>` to
   AirPlayServiceModeMedia. See the :doc:`API
   docs <../apis-ios/ios-airplayservice>` for more information.
