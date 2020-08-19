SubtitleInfo
============

Represents a subtitle track used for media playing.

The URL is required, so the ``-init`` method will throw an exception.
Please use the parameterized initializers.

This class is immutable.

Different services support specific subtitles formats:

-  DLNA service supports ``SRT`` format only. Since there is no official
   specification for them, subtitles may not work on all DLNA-compatible
   devices.

-  Netcast service supports ``SRT`` format only, through DLNA.

-  Google Cast service supports ``WebVTT`` format only and has
   additional requirements:
   https://developers.google.com/cast/docs/ios_sender#cors-requirements

-  FireTV service supports ``WebVTT`` format only. Subtitles on Fire TV
   are hidden by default and should be displayed manually by the user.

-  WebOS service supports ``WebVTT`` format only. Server providing
   subtitles should support CORS headers, similarly to Cast service's
   requirements.

Properties
----------

NSURL \* url
   The subtitle track's URL.

NSString \* mimeType
   The subtitle's mimeType.

NSString \* language
   The subtitle's source language. The contents depend on the target
   device.

NSString \* label
   A custom label that may be displayed by a device's media player.

Methods
-------

\+ (instancetype) **infoWithURL**:(NSURL \*)\ *url*
   Creates a new instance with the given ``url``.

   **Parameters:**

   -  url

\+ (instancetype) **infoWithURL**:(NSURL \*)\ *url* **andBlock**:(void(^)(:doc:`SubtitleInfoBuilder <ios-subtitleinfobuilder>` \*builder))\ *block*
   Creates a new instance with the given ``url`` and properties set in
   the ``builder`` object.

   **Parameters:**

   -  url
   -  **andBlock**: block
