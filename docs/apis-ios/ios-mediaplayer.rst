MediaPlayer
===========

The MediaPlayer capability protocol serves to define the methods
required for displaying media on the device.

Methods
-------

\- (id<`MediaPlayer </apis/1-6-0/ios/MediaPlayer>`__>) **mediaPlayer**

\- (`CapabilityPriorityLevel </apis/1-6-0/ios/CapabilityPriorityLevel>`__) **mediaPlayerPriority**

\- (void) **displayImageWithMediaInfo**:(`MediaInfo </apis/1-6-0/ios/MediaInfo>`__ \*)\ *mediaInfo* **success**:(`MediaPlayerSuccessBlock <#mediaplayersuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  mediaInfo

   -  **success**: success – Optional MediaPlayerSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **playMediaWithMediaInfo**:(`MediaInfo </apis/1-6-0/ios/MediaInfo>`__ \*)\ *mediaInfo* **shouldLoop**:(BOOL)\ *shouldLoop* **success**:(`MediaPlayerSuccessBlock <#mediaplayersuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  mediaInfo

   -  **shouldLoop**: shouldLoop

   -  **success**: success – Optional MediaPlayerSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **closeMedia**:(`LaunchSession </apis/1-6-0/ios/LaunchSession>`__ \*)\ *launchSession* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Close a running media session. Because media is handled differently
   on different platforms, it is required to keep track of LaunchSession
   and MediaControl objects to control that media session in the future.
   LaunchSession will be required to close the media and mediaControl
   will be required to control the media.

   **Related capabilities:**

   -  ``MediaPlayer.Close``

   **Parameters:**

   -  launchSession – LaunchSession object for use in closing media instance

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **displayImage**:(NSURL \*)\ *imageURL* **iconURL**:(NSURL \*)\ *iconURL* **title**:(NSString \*)\ *title* **description**:(NSString \*)\ *description* **mimeType**:(NSString \*)\ *mimeType* **success**:(`MediaPlayerDisplaySuccessBlock <#mediaplayerdisplaysuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Display an image on the device. Not all devices support all of the
   parameters -- supply as many as you have available.

   **Related capabilities:**

   -  ``MediaPlayer.Display.Image``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   **Parameters:**

   -  imageURL – URL of image to open

   -  **iconURL**: iconURL – URL of an icon to show next to the title

   -  **title**: title – Title text to display

   -  **description**: description – Description text to display

   -  **mimeType**: mimeType – MIME type of the image, for example "image/jpeg"

   -  **success**: success – Optional MediaPlayerDisplaySuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **displayImage**:(`MediaInfo </apis/1-6-0/ios/MediaInfo>`__ \*)\ *mediaInfo* **success**:(`MediaPlayerDisplaySuccessBlock <#mediaplayerdisplaysuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Display an image on the device. Not all devices support all of the
   parameters -- supply as many as you have available.

   **Related capabilities:**

   -  ``MediaPlayer.Display.Image``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   **Parameters:**

   -  mediaInfo – Object of MediaInfo class which includes all the information about
      an image to display.

   -  **success**: success – Optional MediaPlayerDisplaySuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **playMedia**:(NSURL \*)\ *mediaURL* **iconURL**:(NSURL \*)\ *iconURL* **title**:(NSString \*)\ *title* **description**:(NSString \*)\ *description* **mimeType**:(NSString \*)\ *mimeType* **shouldLoop**:(BOOL)\ *shouldLoop* **success**:(`MediaPlayerDisplaySuccessBlock <#mediaplayerdisplaysuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Play an audio or video file on the device. Not all devices support
   all of the parameters -- supply as many as you have available.

   **Related capabilities:**

   -  ``MediaPlayer.Play.Video``
   -  ``MediaPlayer.Play.Audio``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   **Parameters:**

   -  mediaURL – URL of media file to open

   -  **iconURL**: iconURL – URL of an icon to show next to the title

   -  **title**: title – Title text to display

   -  **description**: description – Description text to display

   -  **mimeType**: mimeType – MIME type of the video, for example "video/mpeg4", "audio/mp3", etc

   -  **shouldLoop**: shouldLoop – Whether to automatically loop playback

   -  **success**: success – Optional MediaPlayerDisplaySuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **playMedia**:(`MediaInfo </apis/1-6-0/ios/MediaInfo>`__ \*)\ *mediaInfo* **shouldLoop**:(BOOL)\ *shouldLoop* **success**:(`MediaPlayerDisplaySuccessBlock <#mediaplayerdisplaysuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Play an audio or video file on the device. Not all devices support
   all of the parameters -- supply as many as you have available.

   **Related capabilities:**

   -  ``MediaPlayer.Play.Video``
   -  ``MediaPlayer.Play.Audio``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   **Parameters:**

   -  mediaInfo – Object of MediaInfo class which includes all the information about an image to display.

   -  **shouldLoop**: shouldLoop – Whether to automatically loop playback

   -  **success**: success – Optional MediaPlayerDisplaySuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

Typedefs
--------

MediaPlayerDisplaySuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

void(^)(`LaunchSession </apis/1-6-0/ios/LaunchSession>`__
\*launchSession, id<`MediaControl </apis/1-6-0/ios/MediaControl>`__>
mediaControl)

Success block that is called upon successfully playing/displaying a
media file.

-  launchSession

   LaunchSession to allow closing this media player

-  mediaControl

   MediaControl object used to control playback

MediaPlayerSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~

void(^)(`MediaLaunchObject </apis/1-6-0/ios/MediaLaunchObject>`__
\*mediaLaunchObject)
