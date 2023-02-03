MediaInfo
=======================================
``com.connectsdk.core.MediaInfo``

Normalized reference object for information about a media to display.
This object can be used to pass as a parameter to displayImage or playMedia.

Inner Classes
-------------

* :doc:`Builder <and-mediainfo-builder>`

Methods
-------

**MediaInfo** (String *url*, String *mimeType*, String *title*, String *description*)
     This constructor is deprecated. Use ``MediaInfo.Builder`` instead.

     **Parameters:**

     * url – media file
     * mimeType – media mime type
     * title – optional metadata
     * description – optional metadata

**MediaInfo** (String *url*, String *mimeType*, String *title*, String *description*, List<`ImageInfo </apis/1-6-0/android/ImageInfo>`__> *allImages*)
     This constructor is deprecated. Use ``MediaInfo.Builder`` instead.

     **Parameters:**

     * url – media file
     * mimeType – media mime type
     * title – optional metadata
     * description – optional metadata
     * allImages – list of imageInfo objects where [0] is icon, [1] is poster

String **getMimeType** ()
     Gets type of a media file.

void **setMimeType** (String *mimeType*)
     Sets type of a media file.

     This method is deprecated.

     **Parameters:**

     * mimeType

String **getTitle** ()
     Gets title for a media file.

void **setTitle** (String *title*)
     Sets title of a media file.

     This method is deprecated

     **Parameters:**

     * title

String **getDescription** ()
     Gets description for a media.

void **setDescription** (String *description*)
     Sets description for a media. This method is deprecated

     **Parameters:**

     * description

List<:doc:`ImageInfo <and-imageinfo>`> **getImages** ()
     Gets list of ImageInfo objects for images representing a media (ex. icon, poster).
     Where first ([0]) is icon image, and second ([1]) is poster image.

void **setImages** (List<:doc:`ImageInfo <and-imageinfo>`> *images*)
     Sets list of ImageInfo objects for images representing a media (ex. icon, poster).
     Where first ([0]) is icon image, and second ([1]) is poster image.

     This method is deprecated

     **Parameters:**

     * images

long **getDuration** ()
     Gets duration of a media file.

void **setDuration** (long *duration*)
     Sets duration of a media file. This method is deprecated

     **Parameters:**

     * duration

String **getUrl** ()
     Gets URL address of a media file.

void **setUrl** (String *url*)
     Sets URL address of a media file. This method is deprecated

     **Parameters:**

     * url

:doc:`SubtitleInfo <and-subtitleinfo>` **getSubtitleInfo** ()


void **addImages** (:doc:`ImageInfo <and-imageinfo>`... *images*)
     Stores ImageInfo objects.

     This method is deprecated

     **Parameters:**

     * images
