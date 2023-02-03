MediaPlayer
===========

The MediaPlayer capability protocol serves to define the methods
required for displaying media on the device.

Methods
-------

mediaPlayer.\ **displayImage** (*url*, *mimeType*, [*options*])
   Display an image on the device. Not all devices support all of the
   parameters -- supply as many as you have available.

   On success, the success event/callback will be fired with the
   arguments (launchSession, mediaControl)

   -  launchSession: LaunchSession
   -  mediaControl: MediaControl

   **Related capabilities:**

   -  ``MediaPlayer.Display.Image``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   **Parameters:**

   -  url (string)

   -  mimeType (string) – MIME type of the image, for example "image/jpeg"

   -  options (object) [optional] – All properties are optional:

      -  title (string): Title text to display
      -  description (string): Description text to display
      -  iconUrl (string): URL of icon to show next to the title

   **Returns:** :doc:`Command <cor-command>`

mediaPlayer.\ **playMedia** (*url*, *mimeType*, [*options*])
   Play an audio or video file on the device. Not all devices support
   all of the parameters -- supply as many as you have available.

   On success, the success event/callback will be fired with the
   arguments (launchSession, mediaControl)

   -  launchSession: LaunchSession
   -  mediaControl: MediaControl

   **Related capabilities:**

   -  ``MediaPlayer.Play.Video``
   -  ``MediaPlayer.Play.Audio``
   -  ``MediaPlayer.MediaData.Title``
   -  ``MediaPlayer.MediaData.Description``
   -  ``MediaPlayer.MediaData.Thumbnail``
   -  ``MediaPlayer.MediaData.MimeType``

   **Parameters:**

   -  url (string)

   -  mimeType (string) – MIME type of the video, for example "video/mpeg4", "audio/mp3",
      etc

   -  options (object) [optional] – All properties are optional:

      -  title (string): Title text to display
      -  description (string): Description paragraph to display
      -  iconUrl (string): URL of icon to show next to the title
      -  shouldLoop (boolean): Whether to automatically loop playback
      -  subtitles {object} subtitle track with options (properties are
         optional unless specified otherwise):

         -  url (string) [required]: must be a valid URL
         -  mimeType (string)
         -  language (string)
         -  label (string)

   **Returns:** :doc:`Command <cor-command>`
