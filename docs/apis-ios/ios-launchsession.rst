LaunchSession
=============

Any time anything is launched onto a first screen device, there will be important session information that needs to be tracked. 
LaunchSession will track this data, and must be retained to perform certain actions within the session.

Properties
----------

NSString \* appId
   System-specific, unique ID of the app (ex. youtube.leanback.v4,
   0000134, hulu)

NSString \* name
   User-friendly name of the app (ex. YouTube, Browser, Hulu)

NSString \* sessionId
   Unique ID for the session (only provided by certain protocols)

id rawData
   Raw data from the first screen device about the session. In most
   cases, this is an NSDictionary.

:doc:`LaunchSessionType <ios-launchsessiontype>` sessionType
   When closing a LaunchSession, the DeviceService relies on the
   sessionType to determine the method of closing the session.

:doc:`DeviceService <ios-deviceservice>` \* service
   DeviceService responsible for launching the session.

Methods
-------

\- (BOOL) **isEqual**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *launchSession*
   Compares two LaunchSession objects.

   **Parameters:**

   * launchSession – LaunchSession object to compare.

   **Returns:** YES if both LaunchSession id and sessionId values are equal

\- (void) **closeWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Closes the session on the first screen device. Depending on the
   sessionType, the associated service will have different ways of
   handling the close functionality.

   **Parameters:**

   * success – (optional) SuccessBlock to be called on success
   * **failure**: failure – (optional) FailureBlock to be called on failure

\+ (:doc:`LaunchSession <ios-launchsession>` \*) **launchSessionForAppId**:(NSString \*)\ *appId*
   Instantiates a LaunchSession object for a given app ID.

   **Parameters:**

   * appId – System-specific, unique ID of the app

\+ (:doc:`LaunchSession <ios-launchsession>` \*) **launchSessionFromJSONObject**:(NSDictionary \*)\ *json*
   Deserializes a ``LaunchSession`` object from json object.

   **Parameters:**

   * json – Serialized ``LaunchSession`` object by ``-[LaunchSession toJSONObject]``.
