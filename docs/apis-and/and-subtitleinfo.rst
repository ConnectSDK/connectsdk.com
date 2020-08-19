SubtitleInfo
============
``com.connectsdk.core.SubtitleInfo``

Normalized reference object for information about a subtitle track.
It's used in ``MediaInfo`` class. The only one required parameter is
``url``, others can be ``null``. This class is immutable and has a
builder for easy construction.

Different services support specific subtitle formats:

* ``DLNAService`` supports only SRT subtitles. Since there is no
  official specification for them, subtitles may not work on all
  DLNA-compatible devices

* ``NetcastTVService`` supports only SRT subtitles and has the same
  restrictions as ``DLNAService``

* ``CastService`` supports only WebVTT subtitles and it has
  additional requirements

  https://developers.google.com/cast/docs/android_sender#cors-requirements

* ``FireTVService`` supports only WebVTT subtitles

* ``WebOSTVService`` supports WebVTT subtitles. Server providing
  subtitles should support CORS headers, similarly to Cast service's
  requirements.

Inner Classes
-------------
- :doc:`Builder <and-subtitleinfo-builder>`

Methods
-------

String **getUrl** ()

String **getMimeType** ()

String **getLabel** ()

String **getLanguage** ()

boolean **equals** (Object *o*)
   **Parameters:**
   -  o

int **hashCode** ()
