ChannelInfo
===========

Normalized reference object for information about a TVs channels. This
object is required to set the channel on a TV.

Properties
----------

NSString \* id
   TV's unique ID for the channel

NSString \* name
   User-friendly name of the channel

NSString \* number
   TV channel's number (likely to be a combination of the major & minor
   numbers)

int majorNumber
   TV channel's major number

int minorNumber
   TV channel's minor number

id rawData
   Raw data from the first screen device about the channel. In most
   cases, this is an NSDictionary.

Methods
-------

\- (BOOL) **isEqual**:(:doc:`ChannelInfo <ios-channelinfo>` \*)\ *channelInfo*
   Compares two ChannelInfo objects.

   **Parameters:**

   * channelInfo – ChannelInfo object to compare.

   **Returns:** YES if both ChannelInfo number & name values are equal
