ProgramInfo
===========================================
``com.connectsdk.core.ProgramInfo``

Normalized reference object for information about a TVs program.

Methods
-------

String **getId** ()
     Gets the ID of the program on the first screen device. Format is different depending on the platform.

void **setId** (String *id*)
     Sets the ID of the program on the first screen device. Format is different depending on the platform.

     **Parameters:**

     * id

String **getName** ()
     Gets the user-friendly name of the program (ex. Sesame Street, Cosmos, Game of Thrones, etc).

void **setName** (String *name*)
     Sets the user-friendly name of the program (ex. Sesame Street, Cosmos, Game of Thrones, etc).

     **Parameters:**

     * name

:doc:`ChannelInfo <and-channelinfo>` **getChannelInfo** ()
     Gets the reference to the ChannelInfo object that this program is associated with

void **setChannelInfo** (:doc:`ChannelInfo <and-channelinfo>` *channelInfo*)
     Sets the reference to the ChannelInfo object that this program is associated with

     **Parameters:**

     * channelInfo

Object **getRawData** ()
     Gets the raw data from the first screen device about the program. In most cases, this is an NSDictionary.

void **setRawData** (Object *rawData*)
     Sets the raw data from the first screen device about the program. In most cases, this is an NSDictionary.

     **Parameters:**

     * rawData

boolean **equals** (Object *o*)
     Compares two ProgramInfo objects.

     **Parameters:**

     * o

     **Returns:** true if both ProgramInfo id & name values are equal
