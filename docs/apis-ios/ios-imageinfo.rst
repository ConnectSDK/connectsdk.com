ImageInfo
=========

Normalized reference object for information about an image to be sent to a device through the MediaPlayer capability.

Properties
----------

NSURL \* url
   URL source of the image

`ImageType <#imagetype>`__ type
   Type of image (see ImageType enum)

NSInteger width
   Width of the image (optional)

NSInteger height
   Height of the image (optional)

Methods
-------

\- (instancetype) **initWithURL**:(NSURL \*)\ *url* **type**:(`ImageType <#imagetype>`__)\ *type*
   Creates an instance of ImageInfo with given property values.

   **Parameters:**

   * url – URL source of the image
   * **type**: type – Type of image (see ImageType enum)

Typedefs
--------

ImageType
~~~~~~~~~

NSUInteger
