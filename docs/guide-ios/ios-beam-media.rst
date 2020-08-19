Beam Media
==========

A common use case with Connect SDK is to beam a simple media file
(image, video, audio) to a TV. The following is a quick example of how
you can beam an image onto a TV. This example assumes that you have
discovered and connected to a device.

Beam an image file
------------------

.. code-block:: obj-c

   NSURL *mediaURL = [NSURL URLWithString:@"http://www.connectsdk.com/files/9613/9656/8539/test_image.jpg"]; // credit: Blender Foundation/CC By 3.0
   NSURL *iconURL = [NSURL URLWithString:@"http://www.connectsdk.com/files/2013/9656/8845/test_image_icon.jpg"]; // credit: sintel-durian.deviantart.com
   NSString *title = @"Sintel Character Design";
   NSString *description = @"Blender Open Movie Project";
   NSString *mimeType = @"image/jpeg";

   MediaInfo *mediaInfo = [[MediaInfo alloc] initWithURL:mediaURL mimeType:mimeType];
   mediaInfo.title = title;
   mediaInfo.description = description;
   ImageInfo *imageInfo = [[ImageInfo alloc] initWithURL:iconURL type:ImageTypeThumb];
   [mediaInfo addImage:imageInfo];

   __block MediaLaunchObject *launchObject;

   [self.device.mediaPlayer displayImageWithMediaInfo:mediaInfo
                                              success:
    ^(MediaLaunchObject *mediaLaunchObject) {
        NSLog(@"display photo success");

        // save the object reference to control media playback
        launchObject = mediaLaunchObject;

        // enable your media control UI elements here
    }
                                              failure:
    ^(NSError *error) {
        NSLog(@"display photo failure: %@", error.localizedDescription);
    }];

Beam an audio/video file
------------------------

.. code-block:: obj-c

   NSURL *mediaURL = [NSURL URLWithString:@"http://www.connectsdk.com/files/8913/9657/0225/test_video.mp4"]; // credit: Blender Foundation/CC By 3.0
   NSURL *iconURL = [NSURL URLWithString:@"http://www.connectsdk.com/files/7313/9657/0225/test_video_icon.jpg"]; // credit: sintel-durian.deviantart.com
   NSString *title = @"Sintel Trailer";
   NSString *description = @"Blender Open Movie Project";
   NSString *mimeType = @"video/mp4"; // audio/* for audio files

   MediaInfo *mediaInfo = [[MediaInfo alloc] initWithURL:mediaURL mimeType:mimeType];
   mediaInfo.title = title;
   mediaInfo.description = description;
   ImageInfo *imageInfo = [[ImageInfo alloc] initWithURL:iconURL type:ImageTypeThumb];
   [mediaInfo addImage:imageInfo];

   if ([self.device hasCapability:kMediaPlayerSubtitleWebVTT]) {
       NSURL *subtitlesURL = [NSURL URLWithString:@"http://ec2-54-201-108-205.us-west-2.compute.amazonaws.com/samples/media/sintel_en.vtt"];
       SubtitleInfo *subtitleInfo = [SubtitleInfo infoWithURL:subtitlesURL
                                                     andBlock:^(SubtitleInfoBuilder *builder) {
                                                         builder.mimeType = @"text/vtt";
                                                         builder.language = @"English";
                                                         builder.label = @"English Subtitles";
                                                     }];
       mediaInfo.subtitleInfo = subtitleInfo;
   }

   __block MediaLaunchObject *launchObject;

   [self.device.mediaPlayer playMediaWithMediaInfo:mediaInfo
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

Control media playback
----------------------

In the previous example, you will notice that the success block was
called with a mediaControl object. In order to control the media in the
current playback session, you will need to store a reference to this
mediaControl object and call control methods on that object.

.. code-block:: obj-c

   // pause media file
   [launchObject.mediaControl pauseWithSuccess:nil failure:nil];

   // play media file
   [launchObject.mediaControl playWithSuccess:nil failure:nil];

   // seek to 10 seconds
   [launchObject.mediaControl seek:10 success:nil failure:nil];

   // close media file
   [launchObject.session closeWithSuccess:nil failure:nil];
   // or
   [self.device.mediaPlayer closeMedia:launchObject.session success:nil failure:nil];

Beam a playlist
---------------

.. code-block:: obj-c

   NSURL *mediaURL = [NSURL URLWithString:@"your-playlist.m3u"];
   NSURL *iconURL = [NSURL URLWithString:@"http://www.connectsdk.com/files/2013/9656/8845/test_image_icon.jpg"]; // credit: sintel-durian.deviantart.com
   NSString *title = @"Playlist";
   NSString *description = @"Playlist description";
   NSString *mimeType = @"application/x-mpegurl";

   MediaInfo *mediaInfo = [[MediaInfo alloc] initWithURL:mediaURL mimeType:mimeType];
   mediaInfo.title = title;
   mediaInfo.description = description;
   ImageInfo *imageInfo = [[ImageInfo alloc] initWithURL:iconURL type:ImageTypeThumb];
   [mediaInfo addImage:imageInfo];

   __block MediaLaunchObject *launchObject;

   [self.device.mediaPlayer playMediaWithMediaInfo:mediaInfo
                                        shouldLoop:NO
                                           success:
    ^(MediaLaunchObject *mediaLaunchObject) {
        // save the object reference to control playlist and media playback
        launchObject = mediaLaunchObject;

        // enable your media control UI elements here
    }
                                           failure:
    ^(NSError *error) {
        NSLog(@"play playlist failure: %@", error.localizedDescription);
    }];

Control a playlist
------------------

.. code-block:: obj-c

   // play previous track
   [launchObject.playListControl playPreviousWithSuccess:nil failure:nil];
   // play next track
   [launchObject.playListControl playNextWithSuccess:nil failure:nil];
   // play a track specified by index (starts from zero)
   [launchObject.playListControl jumpToTrackWithIndex:0 success:nil failure:nil];

.. note::
   For beaming media to AirPlay devices, you must set the
   :doc:`AirPlayServiceMode <../apis-ios/ios-airplayservicemode>` to
   AirPlayServiceModeMedia. See the :doc:`API
   docs <../apis-ios/ios-airplayservice>` for more information.
