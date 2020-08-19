MediaPlayer
=========================================================
``com.connectsdk.service.capability.MediaPlayer``

*extends CapabilityMethods*

The MediaPlayer capability protocol serves to define the methods
required for displaying media on the device.

Properties
----------

final String Any = "MediaPlayer.Any"

final String Display_Video = "MediaPlayer.Play.Video"
   This capability is deprecated. Use ``MediaPlayer.Play_Video`` instead.

final String Display_Audio = "MediaPlayer.Play.Audio"
   This capability is deprecated. Use ``MediaPlayer.Play_Audio`` instead.

final String Display_Image = "MediaPlayer.Display.Image"

final String Play_Video = "MediaPlayer.Play.Video"

final String Play_Audio = "MediaPlayer.Play.Audio"

final String Play_Playlist = "MediaPlayer.Play.Playlist"

final String Close = "MediaPlayer.Close"

final String Loop = "MediaPlayer.Loop"

final String Subtitle_SRT = "MediaPlayer.Subtitle.SRT"

final String Subtitle_WebVTT = "MediaPlayer.Subtitle.WebVTT"

final String MetaData_Title = "MediaPlayer.MetaData.Title"

final String MetaData_Description = "MediaPlayer.MetaData.Description"

final String MetaData_Thumbnail = "MediaPlayer.MetaData.Thumbnail"

final String MetaData_MimeType = "MediaPlayer.MetaData.MimeType"

final String MediaInfo_Get = "MediaPlayer.MediaInfo.Get"

final String MediaInfo_Subscribe = "MediaPlayer.MediaInfo.Subscribe"

final String[] Capabilities = { Display_Image, Play_Video, Play_Audio, Close, MetaData_Title, MetaData_Description, MetaData_Thumbnail, MetaData_MimeType, MediaInfo_Get, MediaInfo_Subscribe }

Inner Classes
-------------

* :doc:`LaunchListener <and-mediaplayer-launchlistener>`
* :doc:`MediaInfoListener <and-mediainfolistener>`
* :doc:`MediaLaunchObject <and-medialaunchobject>`

Methods
-------

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()


:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaPlayerCapabilityLevel** ()


void **getMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
     **Parameters:**

     * listener – (optional) MediaInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MediaInfoListener <and-mediainfolistener>`> **subscribeMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
     **Parameters:**

     * listener – (optional) MediaInfoListener with methods to be called on success or failure

void **displayImage** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, LaunchListener *listener*)
     Display an image on the device. Not all devices support all of the parameters -- supply as many as you have available.

     **Related capabilities:**

     * ``MediaPlayer.Display.Image``
     * ``MediaPlayer.MediaData.Title``
     * ``MediaPlayer.MediaData.Description``
     * ``MediaPlayer.MediaData.Thumbnail``
     * ``MediaPlayer.MediaData.MimeType``

     **Parameters:**

     * mediaInfo – Object of MediaInfo class which includes all the information about an image to display.
     * listener – (optional) LaunchListener with methods to be called on success or failure

void **playMedia** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, boolean *shouldLoop*, LaunchListener *listener*)
     Play an audio or video file on the device. Not all devices support all of the parameters -- supply as many as you have available.

     **Related capabilities:**

     * ``MediaPlayer.Play.Video``
     * ``MediaPlayer.Play.Audio``
     * ``MediaPlayer.MediaData.Title``
     * ``MediaPlayer.MediaData.Description``
     * ``MediaPlayer.MediaData.Thumbnail``
     * ``MediaPlayer.MediaData.MimeType``

     **Parameters:**

     * mediaInfo – Object of MediaInfo class which includes all the information about an image to display.
     * shouldLoop – Whether to automatically loop playback
     * listener – (optional) LaunchListener with methods to be called on success or failure

void **closeMedia** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Close a running media session. Because media is handled differently
     on different platforms, it is required to keep track of LaunchSession
     and MediaControl objects to control that media session in the future.
     LaunchSession will be required to close the media and mediaControl
     will be required to control the media.

     **Related capabilities:**
     
     * ``MediaPlayer.Close``

     **Parameters:**

     * launchSession – LaunchSession object for use in closing media instance
     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **displayImage** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, LaunchListener *listener*)
     Display an image on the device. Not all devices support all of the parameters -- supply as many as you have available.

     This method is deprecated. Use ``MediaPlayer::displayImage(MediaInfo mediaInfo, LaunchListener listener)`` instead.

     **Related capabilities:**

     * ``MediaPlayer.Display.Image``
     * ``MediaPlayer.MediaData.Title``
     * ``MediaPlayer.MediaData.Description``
     * ``MediaPlayer.MediaData.Thumbnail``
     * ``MediaPlayer.MediaData.MimeType``

     **Parameters:**

     * url
     * mimeType – MIME type of the image, for example "image/jpeg"
     * title – Title text to display
     * description – Description text to display
     * iconSrc
     * listener – (optional) LaunchListener with methods to be called on success or failure

void **playMedia** (String *url*, String *mimeType*, String *title*, String *description*, String *iconSrc*, boolean *shouldLoop*, LaunchListener *listener*)
     Play an audio or video file on the device. Not all devices support all of the parameters -- supply as many as you have available.

     This method is deprecated. Use ``MediaPlayer::playMedia(MediaInfo mediaInfo, boolean shouldLoop, LaunchListener listener)`` instead.

     **Related capabilities:**

     * ``MediaPlayer.Play.Video``
     * ``MediaPlayer.Play.Audio``
     * ``MediaPlayer.MediaData.Title``
     * ``MediaPlayer.MediaData.Description``
     * ``MediaPlayer.MediaData.Thumbnail``
     * ``MediaPlayer.MediaData.MimeType``

     **Parameters:**

     * url
     * mimeType – MIME type of the video, for example "video/mpeg4", "audio/mp3", etc
     * title – Title text to display
     * description – Description text to display
     * iconSrc
     * shouldLoop – Whether to automatically loop playback
     * listener – (optional) LaunchListener with methods to be called on success or failure
