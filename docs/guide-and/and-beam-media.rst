Beam Media
==========

A common use case with Connect SDK will be to beam a simple media file
(image, video, audio) to a TV. The following is a quick example of how
you can beam an image onto a TV. This example is assuming that you have
discovered & connected to a device.

Beam an image file
------------------

.. code-block:: java

   String mediaURL = "http://www.connectsdk.com/files/9613/9656/8539/test_image.jpg"; // credit: Blender Foundation/CC By 3.0
   String iconURL = "http://www.connectsdk.com/files/2013/9656/8845/test_image_icon.jpg"; // credit: sintel-durian.deviantart.com
   String title = "Sintel Character Design";
   String description = "Blender Open Movie Project";
   String mimeType = "image/jpeg";

   MediaInfo mediaInfo = new MediaInfo.Builder(mediaURL, mimeType)
         .setTitle(title)
         .setDescription(description)
         .setIcon(iconURL)
         .build();

   // These variable should be class fields
   // LaunchSession mLaunchSession;
   // MediaControl mMediaControl;
   // ConnectableDevice mDevice;

   MediaPlayer.LaunchListener listener = new MediaPlayer.LaunchListener() {
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

   mDevice.getMediaPlayer().displayImage(mediaInfo, listener);

Beam an audio/video file
------------------------

.. code-block:: java

   String mediaURL = "http://www.connectsdk.com/files/8913/9657/0225/test_video.mp4"; // credit: Blender Foundation/CC By 3.0
   String iconURL = "http://www.connectsdk.com/files/2013/9656/8845/test_image_icon.jpg"; // credit: sintel-durian.deviantart.com
   String title = "Sintel Trailer";
   String description = "Blender Open Movie Project";
   String mimeType = "video/mp4"; // audio/* for audio files

   SubtitleInfo subtitles = null;
   if (getTv().hasCapability(MediaPlayer.Subtitle_WebVTT)) {
         subtitles = new SubtitleInfo.Builder("http://ec2-54-201-108-205.us-west-2.compute.amazonaws.com/samples/media/sintel_en.vtt")
               .setMimeType("text/vtt")
               .setLanguage("en")
               .setLabel("English subtitles")
               .build();
   }
   MediaInfo mediaInfo = new MediaInfo.Builder(mediaURL, mimeType)
         .setTitle(title)
         .setDescription(description)
         .setIcon(iconURL)
         .setSubtitleInfo(subtitles)
         .build();

   // These variables should be class fields
   // LaunchSession mLaunchSession;
   // MediaControl mMediaControl;
   // ConnectableDevice mDevice;

   MediaPlayer.LaunchListener listener = new MediaPlayer.LaunchListener() {
       @Override
       public void onSuccess(MediaLaunchObject object) {
           // save these object references to control media playback
           mLaunchSession = object.launchSession;
           mMediaControl = object.mediaControl;

           // you will want to enable your media control UI elements here
       }

       @Override
       public void onError(ServiceCommandError error) {
           Log.d("App Tag", "Play media failure: " + error);
       }
   };

   mDevice.getMediaPlayer().playMedia(mediaInfo, false, listener);

Control media playback
----------------------

In the previous example, you will notice that the success block was
called with a mediaControl object. In order to control the media in the
current playback session, you will need to store a reference to this
mediaControl object and call control methods on that object.

.. code-block:: java

   // pause media file
   mMediaControl.pause(null);

   // play media file
   mMediaControl.play(null);

   // seek to 10 seconds
   mMediaControl.seek(10000L, null);

   // close media file
   mMediaControl.close(null);
   // or
   mDevice.getMediaPlayer().closeMedia(mLaunchSession, null);

Beam a playlist
---------------

.. code-block:: java

   // These variables should be class fields
   // LaunchSession mLaunchSession;
   // MediaControl mMediaControl;
   // PlaylistControl mPlaylistControl;
   // ConnectableDevice mDevice;

   MediaInfo mediaInfo = new MediaInfo.Builder("your-playlist.m3u", "application/x-mpegurl")
           .setTitle("Playlist")
           .setDescription("Playlist description")
           .build();

   mDevice.getMediaPlayer().playMedia(mediaInfo, false, new MediaPlayer.LaunchListener() {
       @Override
       public void onSuccess(MediaLaunchObject object) {
           // save these object references to control media playback
           mLaunchSession = object.launchSession;
           mMediaControl = object.mediaControl;
           // playlistControl can be null if it's not supported by a service
           mPlaylistControl = object.playlistControl;
           // you will want to enable your media control UI elements here
       }

       @Override
       public void onError(ServiceCommandError error) {
           Log.d("App Tag", "Play playlist failure: " + error);
       }
   });

Control a playlist
------------------

.. code-block:: java

   // play previous track
   mPlaylistControl.previous(null);
   // play next track
   mPlaylistControl.next(null);
   // play a track specified by index (index starts from zero)
   mPlaylistControl.jumpToTrack(0, null);
