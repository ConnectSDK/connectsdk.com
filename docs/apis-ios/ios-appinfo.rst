AppInfo
=======

Normalized reference object for information about a DeviceService's app.
This object will, in most cases, be used to launch apps.

In some cases, all that is needed to launch an app is the app id. For
these cases, a static constructor method has been provided.

Properties
----------

NSString \* id
   ID of the app on the first screen device. Format is different
   depending on the platform. (ex. youtube.leanback.v4, 0000001134,
   netflix, etc).

NSString \* name
   User-friendly name of the app (ex. YouTube, Browser, Netflix, etc).

id rawData
   Raw data from the first screen device about the app. In most cases,
   this is an NSDictionary.

Methods
-------

\- (BOOL) **isEqual**:(:doc:`AppInfo <ios-appinfo>` \*)\ *appInfo*
   Compares two AppInfo objects.

   **Parameters:**

   -  appInfo – AppInfo object to compare.

   **Returns:** YES if both AppInfo id values are equal

\+ (:doc:`AppInfo <ios-appinfo>` \*) **appInfoForId**:(NSString \*)\ *appId*
   Static constructor method.

   **Parameters:**

   -  appId – ID of the app on the first screen device
