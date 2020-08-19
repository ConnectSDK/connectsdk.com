ImageInfo
=======================================
``com.connectsdk.core.ImageInfo``

Normalized reference object for information about an image file. This
object can be used to represent a media file (ex. icon, poster)

Inner Classes
-------------

* ImageType

Methods
-------

**ImageInfo** (String *url*)
     Default constructor method.

     **Parameters:**
   
     * url

**ImageInfo** (String *url*, ImageType *type*, int *width*, int *height*)
   Default constructor method.

   **Parameters:**

   * url – add type of file, width and height of image.
   * type
   * width
   * height

String **getUrl** ()
   Gets URL address of an image file.

void **setUrl** (String *url*)
   Sets URL address of an image file.

   **Parameters:**

   * url

ImageType **getType** ()
   Gets a type of an image file.

void **setType** (ImageType *type*)
   Sets a type of an image file.

   **Parameters:**

   * type

int **getWidth** ()
   Gets a width of an image.

void **setWidth** (int *width*)
   Sets a width of an image.

   **Parameters:**

   * width

int **getHeight** ()
   Gets a height of an image.

void **setHeight** (int *height*)
   Sets a height of an image.

   **Parameters:**

   * height

boolean **equals** (Object *o*)
   **Parameters:**

   * o

int **hashCode** ()
