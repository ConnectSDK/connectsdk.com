Beam Web Apps
=============

There are several platforms available which support the launching of web
apps. A web app is typically run on a temporary basis in a full-screen
browser instance.

Web App IDs
-----------

Both webOS and Chromecast platforms require a web app ID for API calls
to launch & communicate with web apps. This web app ID is translated it
into your web app's URL on web app launch.

For information on creating a web app ID for webOS, please visit the
`registration site`_.

To learn how to register for a Chromecast web app ID,
visit `Google's app ID registration site`_.

Launch web app with identifier
------------------------------

Connect SDK currently supports web app launching on webOS and Chromecast
devices, which both translate a web app identifier into your web app's
URL.

.. _registration site: http://lgsvl.com/connectSDK/index.php
.. _Google's app ID registration site: https://developers.google.com/cast/docs/registration

Communicating with web apps
---------------------------

Bi-directional communication with your web app is made extremely simple.
Data can be sent and received as strongly-typed data.  For example, as a
string or a keyed set of values (JSON object).

.. code-block:: java

   String webAppId = null;

   // This variable should be a class field
   // ConnectableDevice mDevice;

   if (mDevice.getServiceByName("webOS TV") != null)
       webAppId = "5G7328DE";
   else if (mDevice.getServiceByName("Chromecast") != null)
       webAppId = "3E5106AB";
   else if (mDevice.getServiceByName("AirPlay") != null)
       webAppId = "http://www.example.com/";

   if (webAppId == null)
       return;

   mDevice.getWebAppLauncher().launchWebApp(webAppId, new WebAppSession.LaunchListener() {

       @Override
       public void onError(ServiceCommandError error) {
           Log.d("App Tag", "Failed to open web app: " + error);
       }

       @Override
       public void onSuccess(WebAppSession object) {
           Log.d("App Tag", "Web app launch success");
       }
   });

.. code-block:: java

  String webAppId = "your_web_app";
  // These variables should be class fields
  // WebAppSession mWebAppSession;
  // WebAppSessionListener mWebAppSessionListener;
  // ConnectableDevice mDevice;

  mDevice.getWebAppLauncher().launchWebApp(webAppId, new WebAppSession.LaunchListener() {

      @Override
      public void onError(ServiceCommandError error) {
          Log.d("App Tag", "Failed to open web app: " + error);
      }

      @Override
      public void onSuccess(WebAppSession object) {
          Log.d("App Tag", "Web app launch success");

          mWebAppSession = object;
          mWebAppSession.setWebAppSessionListener(mWebAppSessionListener);

          mWebAppSession.connect(new ResponseListener() {

              @Override
              public void onError(ServiceCommandError error) {
                  Log.d("App Tag", "Failed to connect to web app: " + error);
              }

              @Override
              public void onSuccess(Object object) {
                  Log.d("App Tag", "Web app connect success");
              }
          });
      }
  });

After successfully establishing a connection, you can send messages
to your web app.

.. code-block:: java

   mWebAppSession.sendMessage("This is a test message", null);

You can also send an NSDictionary which will be received by the web app as
a JSON object.

.. code-block:: java

   JSONObject message = null;
   try {
       message = new JSONObject() {{
           put("someParameter", "someValue");
           put("anArray", new JSONArray() {{
               put("array value 1");
               put("array value 2");
               put("array value 3");
           }});
           put("anotherObject", new JSONObject() {{
               put("anotherParameter", "anotherValue");
           }});
       }};
   } catch (JSONException e) {
       e.printStackTrace();
   }

   mWebAppSession.sendMessage(message, null);

WebAppSessionDelegate allows you to receive messages from your web app.

Beam media to web app
---------------------

A common use case for web apps is the playback and control of media
files. Connect SDK provides capabilities for directly
playing/controlling media on a WebAppSession, provided that web app has
integrated the :doc:`Connect SDK JavaScript Bridge <../guide-web/index>`.

Rather than calling playMedia on your device's mediaPlayer,
webAppSession provides its own mediaPlayer. After media has been beamed
into the web app, the control is just like any other media session.

.. code-block:: java

   // These variable should be class fields
   // LaunchSession mLaunchSession;
   // MediaControl mMediaControl;
   // WebAppSession mWebAppSession;

   MediaPlayer.LaunchListener listener = new MediaPlayer.launchListener() {
       @Override
       public void onSuccess(MediaLaunchObject object) {
           // save these object references to control media playback
           mLaunchSession = object.launchSession;
           mMediaControl = object.mediaControl;

           // you will want to enable your media control UI elements here
       }

       @Override
       public void onError(ServiceCommandError error) {
           Log.d("App Tag", "Display photo failure: " + error);
       }
   };

   String mediaURL = "http://www.connectsdk.com/files/9613/9656/8539/test_image.jpg"; // credit: Blender Foundation/CC By 3.0
   String iconURL = "http://www.connectsdk.com/files/2013/9656/8845/test_image_icon.jpg"; // credit: sintel-durian.deviantart.com
   String title = "Sintel Character Design";
   String description = "Blender Open Movie Project";
   String mimeType = "image/jpeg";

   List imageList = Arrays.asList(new ImageInfo(iconURL));
   MediaInfo mediaInfo = new MediaInfo(mediaURL, mimeType, title, description, imageList);


   mWebAppSession.getMediaPlayer().displayImage(mediaInfo, listener);
