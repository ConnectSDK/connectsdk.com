ProgramInfo
===========

Normalized reference object for information about a TVs program.

Properties
----------

NSString \* id
   ID of the program on the first screen device. Format is different
   depending on the platform.

NSString \* name
   User-friendly name of the program (ex. Sesame Street, Cosmos, Game of
   Thrones, etc).

:doc:`ChannelInfo <ios-channelinfo>` \* channelInfo
   Reference to the ChannelInfo object that this program is associated
   with

id rawData
   Raw data from the first screen device about the program. In most
   cases, this is an NSDictionary.

Methods
-------

\- (BOOL) **isEqual**:(:doc:`ProgramInfo <ios-programinfo>` \*)\ *programInfo*
   Compares two ProgramInfo objects.

   **Parameters:**

   -  programInfo – ProgramInfo object to compare.

   **Returns:** YES if both ProgramInfo id & name values are equal
