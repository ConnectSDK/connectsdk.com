SubtitleInfoBuilder
===================

Used to initialize a ``SubtitleInfo`` object in a convenient way. The
properties are writable at this point, and then become readonly in a
final object.

You should not create this object manually. It is passed as a parameter
to ``+[SubtitleInfo infoWithURL:andBlock:]`` method.

http://www.annema.me/the-builder-pattern-in-objective-c

Properties
----------

NSString \* mimeType
   The subtitle's mimeType.

NSString \* language
   The subtitle's source language. The contents depend on the target
   device.

NSString \* label
   A custom label that may be displayed by a device's media player.
