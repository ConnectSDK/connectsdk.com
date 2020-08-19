MediaInfo
=========

Normalized reference object for information about a media file to be
sent to a device through the MediaPlayer capability. "Media file", in
this context, refers to an audio or video resource.

Properties
----------

NSURL \* url
   URL source of the media file

NSString \* mimeType
   Mime-type of the media file

NSString \* title
   Title of the media file (optional)

NSString \* description
   Short description of the media file (optional)

NSTimeInterval duration
   Duration of the media file

NSArray \* images
   Collection of ImageInfo objects to send, as necessary, to the device
   when launching media through the MediaPlayer capability.

:doc:`SubtitleInfo <ios-subtitleinfo>` \* subtitleInfo
   Subtitle track for this media instance (optional).

Methods
-------

\- (instancetype) **initWithURL**:(NSURL \*)\ *url* **mimeType**:(NSString \*)\ *mimeType*
   Creates an instance of MediaInfo with given property values.

   **Parameters:**

   -  url – URL source of the media file

   -  **mimeType**: mimeType – Mime-type of the media file

\- (void) **addImage**:(:doc:`ImageInfo <ios-imageinfo>` \*)\ *image*
   Adds an ImageInfo object to the array of images.

   **Parameters:**

   -  image – ImageInfo object to be added

\- (void) **addImages**:(NSArray \*)\ *images*
   Adds an array of ImageInfo objects to the array of images.

   **Parameters:**

   -  images - Array of ImageInfo objects to be added
