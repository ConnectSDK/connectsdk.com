AppInfo com.connectsdk.core.AppInfo
===================================

Normalized reference object for information about a DeviceService's app.
This object will, in most cases, be used to launch apps.

In some cases, all that is needed to launch an app is the app id.

Methods
-------

**AppInfo** ()
   Default constructor method.

**AppInfo** (String *id*)
   Default constructor method.

   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  id –

      App id to launch

String **getId** ()
   Gets the ID of the app on the first screen device. Format is
   different depending on the platform. (ex. youtube.leanback.v4,
   0000001134, netflix, etc).

void **setId** (String *id*)
   Sets the ID of the app on the first screen device. Format is
   different depending on the platform. (ex. youtube.leanback.v4,
   0000001134, netflix, etc).

   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  id

String **getName** ()
   Gets the user-friendly name of the app (ex. YouTube, Browser,
   Netflix, etc).

void **setName** (String *name*)
   Sets the user-friendly name of the app (ex. YouTube, Browser,
   Netflix, etc).

   .. rubric:: Parameters:
      :name: parameters-2
      :class: method-detail-label

   -  name

JSONObject **getRawData** ()
   Gets the raw data from the first screen device about the app.

void **setRawData** (JSONObject *data*)
   Sets the raw data from the first screen device about the app.

   .. rubric:: Parameters:
      :name: parameters-3
      :class: method-detail-label

   -  data

boolean **equals** (Object *o*)
   Compares two AppInfo objects.

   .. rubric:: Parameters:
      :name: parameters-4
      :class: method-detail-label

   -  o –

      Other AppInfo object to compare.

   .. rubric:: Returns:
      :name: returns
      :class: method-detail-label

   true if both AppInfo id values are equal

Inherited Methods
-----------------

JSONObject **toJSONObject** ()
