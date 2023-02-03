ExternalInputInfo
=================
``com.connectsdk.core.ExternalInputInfo``

Normalized reference object for information about a DeviceService's
external inputs. This object is required to set a DeviceService's
external input.

Methods
-------

**ExternalInputInfo** ()
    Default constructor method.

String **getId** ()
    Gets the ID of the external input on the first screen device.

void **setId** (String *inputId*)
    Sets the ID of the external input on the first screen device.

    **Parameters:**

    -  inputId

String **getName** ()
    Gets the user-friendly name of the external input (ex. AV, HDMI1,
    etc).

void **setName** (String *inputName*)
    Sets the user-friendly name of the external input (ex. AV, HDMI1,
    etc).

    **Parameters:**

    -  inputName

void **setRawData** (JSONObject *rawData*)
    Sets the raw data from the first screen device about the external
    input.

    **Parameters:**

    -  rawData

JSONObject **getRawData** ()
    Gets the raw data from the first screen device about the external
    input.

boolean **isConnected** ()
    Whether the DeviceService is currently connected to this external
    input.

void **setConnected** (boolean *connected*)
    Sets whether the DeviceService is currently connected to this
    external input.

    **Parameters:**

    -  connected

String **getIconURL** ()
    Gets the URL to an icon representing this external input.

void **setIconURL** (String *iconURL*)
    Sets the URL to an icon representing this external input.

    **Parameters:**

    -  iconURL

boolean **equals** (Object *o*)
    Compares two ExternalInputInfo objects.

    **Parameters:**

    -  o

    **Returns:** YES if both ExternalInputInfo id & name values are equal

Inherited Methods
-----------------

JSONObject **toJSONObject** ()