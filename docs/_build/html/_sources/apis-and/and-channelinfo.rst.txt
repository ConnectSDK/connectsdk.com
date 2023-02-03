ChannelInfo 
===========
``com.connectsdk.core.ChannelInfo``

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

    **Parameters:**

    -  rawData

String **getName** ()
    Gets the user-friendly name of the channel

void **setName** (String *channelName*)
    Sets the user-friendly name of the channel

    **Parameters:**

    -  channelName

String **getId** ()
    Gets the TV's unique ID for the channel

void **setId** (String *channelId*)
    Sets the TV's unique ID for the channel

    **Parameters:**

    -  channelId

String **getNumber** ()
    Gets the TV channel's number (likely to be a combination of the major
    & minor numbers)

void **setNumber** (String *channelNumber*)
    Sets the TV channel's number (likely to be a combination of the major
    & minor numbers)

    **Parameters:**

    -  channelNumber

int **getMinorNumber** ()
    Gets the TV channel's minor number

void **setMinorNumber** (int *minorNumber*)
    Sets the TV channel's minor number

    **Parameters:**

    -  minorNumber

int **getMajorNumber** ()
    Gets the TV channel's major number

void **setMajorNumber** (int *majorNumber*)
    Sets the TV channel's major number

    **Parameters:**

    -  majorNumber

boolean **equals** (Object *o*)
    Compares two ChannelInfo objects.

    **Parameters:**

    -  o

    **Returns:** YES if both ChannelInfo number & name values are equal

Inherited Methods
-----------------

JSONObject **toJSONObject** ()
