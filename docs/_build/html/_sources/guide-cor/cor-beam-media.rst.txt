Beam Media
==========

A common use case with Connect SDK will be to beam a simple media file
(image, video, audio) to a TV. The following is a quick example of how
you can beam an image onto a TV. This example is assuming that you have
discovered & connected to a device.

Beam an image file
------------------

.. code-block:: javascript

   var url = "http://www.connectsdk.com/files/9613/9656/8539/test_image.jpg";
   var iconUrl = "http://www.connectsdk.com/files/9613/9656/8539/test_image.jpg";
   var mimeType = "image/jpeg";

   device.getMediaPlayer().displayImage(url, mimeType, {
       title: "Sintel Character Design",
       description: "Blender Open Movie Project",
   }).success(function (launchSession, mediaControl) {
       console.log("Image launch successful");
   }).error(function (err) {
       console.log("error: " + err.message);
   });

Beam an audio/video file
------------------------

.. code-block:: javascript

   var myMediaControl;

   var url = "http://www.connectsdk.com/files/8913/9657/0225/test_video.mp4";
   var iconUrl = "http://www.connectsdk.com/files/7313/9657/0225/test_video_icon.jpg";
   var mimeType = "video/mp4";

   device.getMediaPlayer().displayImage(url, mimeType, {
       title: "Sintel Trailer",
       description: "Blender Open Movie Project",
   }).success(function (launchSession, mediaControl) {
       console.log("Video launch successful");

       // save a reference to the MediaControl object (if supported)
       myMediaControl = mediaControl && mediaControl.acquire();
   }).error(function (err) {
       console.log("error: " + err.message);
   });

Control media playback
----------------------

In the previous example, you will notice that the success block was
called with a mediaControl object. In order to control the media in the
current playback session, you will need to store a reference to this
mediaControl object and call control methods on that object.

.. code-block:: javascript

   // Pause media
   myMediaControl.pause()

   // Play media
   myMediaControl.play();

   // Seek to 10 seconds
   myMediaControl.seek(10);

   // Close media player
   myLaunchSession.close();

Beam media to web app
---------------------

A common use case for web apps is the playback and control of media
files. Connect SDK provides capabilities for directly
playing/controlling media on a WebAppSession, provided that web app has
integrated the :doc:`Connect SDK JavaScript Bridge <../guide-web/index>`.

Rather than calling playMedia on your device's mediaPlayer,
webAppSession provides its own mediaPlayer. After media has been beamed
into the web app, the control is just like any other media session.

.. code-block:: javascript

  myWebAppSession.getMediaPlayer().playMedia(url, mimeType, options).success(function (launchSession, mediaControl) {
      myLaunchSession = launchSession.acquire();
      myMediaControl = mediaControl && mediaControl.acquire();
  }).error(function (err) {
      console.log("play video failure: " + err.message);
  });

Beam a playlist
---------------

.. code-block:: javascript

  var url = "your-playlist.m3u";
  var mimeType = "application/x-mpegurl";
  var options = { title: "Playlist", description: "Playlist Description" };

  myWebAppSession.getMediaPlayer().playMedia(url, mimeType, options)
  .success(function (launchSession, mediaControl, playlistControl) {
      myLaunchSession = launchSession.acquire();
      myMediaControl = mediaControl && mediaControl.acquire();
      myPlaylistControl = playlistControl && playlistControl.acquire();
  }).error(function (err) {
      console.log("play video failure: " + err.message);
  });

Control a playlist
------------------

.. code-block:: javascript

  // play previous track
  myPlaylistControl.previous();
  // play next track
  myPlaylistControl.next();
  // play a track specified by index (index starts from zero)
  myPlaylistControl.jumpToTrack(0);
