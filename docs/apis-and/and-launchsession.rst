LaunchSession 
===========================================================
``com.connectsdk.service.sessions.LaunchSession``

Any time anything is launched onto a first screen device, there will be
important session information that needs to be tracked. LaunchSession
will track this data, and must be retained to perform certain actions
within the session.

Inner Classes
-------------

* :doc:`LaunchSessionType <and-launchsessiontype>`

Methods
-------

**LaunchSession** ()


String **getAppId** ()
     System-specific, unique ID of the app (ex. youtube.leanback.v4, 0000134, hulu)

void **setAppId** (String *appId*)
     Sets the system-specific, unique ID of the app (ex. youtube.leanback.v4, 0000134, hulu)

     **Parameters:**

     * appId – Id of the app

String **getAppName** ()
     User-friendly name of the app (ex. YouTube, Browser, Hulu)

void **setAppName** (String *appName*)
     Sets the user-friendly name of the app (ex. YouTube, Browser, Hulu)

     **Parameters:**

     * appName – Name of the app

String **getSessionId** ()
     Unique ID for the session (only provided by certain protocols)

void **setSessionId** (String *sessionId*)
     Sets the session id (only provided by certain protocols)

     **Parameters:**

     * sessionId – Id of the current session

:doc:`DeviceService <and-deviceservice>` **getService** ()
     DeviceService responsible for launching the session.

void **setService** (:doc:`DeviceService <and-deviceservice>` *service*)
     DeviceService responsible for launching the session.

     **Parameters:**

     * service – Sets the DeviceService

Object **getRawData** ()
     Raw data from the first screen device about the session. In most cases, this is a JSONObject.

void **setRawData** (Object *rawData*)
     Sets the raw data from the first screen device about the session. In most cases, this is a JSONObject.

     **Parameters:**

     * rawData – Sets the raw data

:doc:`LaunchSessionType <and-launchsessiontype>` **getSessionType** ()
     When closing a LaunchSession, the DeviceService relies on the sessionType to determine the method of closing the session.

void **setSessionType** (:doc:`LaunchSessionType <and-launchsessiontype>` *sessionType*)
     Sets the LaunchSessionType of this LaunchSession.

     **Parameters:**
   
     * sessionType – The type of LaunchSession

void **close** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Close the app/media associated with the session.

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

boolean **equals** (Object *launchSession*)
     Compares two LaunchSession objects.

     **Parameters:**

     * launchSession – LaunchSession object to compare.

     **Returns:** true if both LaunchSession id and sessionId values are equal

static :doc:`LaunchSession <and-launchsession>` **launchSessionForAppId** (String *appId*)
     Instantiates a LaunchSession object for a given app ID.

     **Parameters:**
     
     * appId – System-specific, unique ID of the app

Inherited Methods
-----------------

JSONObject **toJSONObject** ()


void **fromJSONObject** (JSONObject *obj*)
     **Parameters:**

     * obj
