ChannelInfo com.connectsdk.core.ChannelInfo
===========================================

Normalized reference object for information about a TVs channels. This
object is required to set the channel on a TV.

Methods
-------

**ChannelInfo** ()
   Default constructor method.

JSONObject **getRawData** ()
   Gets the raw data from the first screen device about the channel. In
   most cases, this is an NSDictionary.

void **setRawData** (JSONObject *rawData*)
   Sets the raw data from the first screen device about the channel. In
   most cases, this is an NSDictionary.

   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  rawData

String **getName** ()
   Gets the user-friendly name of the channel

void **setName** (String *channelName*)
   Sets the user-friendly name of the channel

   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  channelName

String **getId** ()
   Gets the TV's unique ID for the channel

void **setId** (String *channelId*)
   Sets the TV's unique ID for the channel

   .. rubric:: Parameters:
      :name: parameters-2
      :class: method-detail-label

   -  channelId

String **getNumber** ()
   Gets the TV channel's number (likely to be a combination of the major
   & minor numbers)

void **setNumber** (String *channelNumber*)
   Sets the TV channel's number (likely to be a combination of the major
   & minor numbers)

   .. rubric:: Parameters:
      :name: parameters-3
      :class: method-detail-label

   -  channelNumber

int **getMinorNumber** ()
   Gets the TV channel's minor number

void **setMinorNumber** (int *minorNumber*)
   Sets the TV channel's minor number

   .. rubric:: Parameters:
      :name: parameters-4
      :class: method-detail-label

   -  minorNumber

int **getMajorNumber** ()
   Gets the TV channel's major number

void **setMajorNumber** (int *majorNumber*)
   Sets the TV channel's major number

   .. rubric:: Parameters:
      :name: parameters-5
      :class: method-detail-label

   -  majorNumber

boolean **equals** (Object *o*)
   Compares two ChannelInfo objects.

   .. rubric:: Parameters:
      :name: parameters-6
      :class: method-detail-label

   -  o

   .. rubric:: Returns:
      :name: returns
      :class: method-detail-label

   YES if both ChannelInfo number & name values are equal

Inherited Methods
-----------------

JSONObject **toJSONObject** ()
