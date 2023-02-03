AppInfo
=======
``com.connectsdk.core.AppInfo``

Normalized reference object for information about a DeviceService's app.
This object will, in most cases, be used to launch apps.

In some cases, all that is needed to launch an app is the app id.

Methods
-------

**AppInfo** ()
    Default constructor method.

**AppInfo** (String *id*)
    Default constructor method.

    **Parameters:**

    -  id – App id to launch

String **getId** ()
    Gets the ID of the app on the first screen device. Format is
    different depending on the platform. (ex. youtube.leanback.v4,
    0000001134, netflix, etc).

void **setId** (String *id*)
    Sets the ID of the app on the first screen device. Format is
    different depending on the platform. (ex. youtube.leanback.v4,
    0000001134, netflix, etc).

    **Parameters:**

    -  id

String **getName** ()
    Gets the user-friendly name of the app (ex. YouTube, Browser,
    Netflix, etc).

void **setName** (String *name*)
    Sets the user-friendly name of the app (ex. YouTube, Browser,
    Netflix, etc).

    **Parameters:**

    -  name

JSONObject **getRawData** ()
    Gets the raw data from the first screen device about the app.

void **setRawData** (JSONObject *data*)
    Sets the raw data from the first screen device about the app.

    **Parameters:**

    -  data

boolean **equals** (Object *o*)
    Compares two AppInfo objects.

    **Parameters:**

    -  o – Other AppInfo object to compare.

    **Returns:** true if both AppInfo id values are equal

Inherited Methods
-----------------

JSONObject **toJSONObject** ()
