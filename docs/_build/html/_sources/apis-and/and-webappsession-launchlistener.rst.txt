WebAppSession.LaunchListener
===========================================================================
``com.connectsdk.service.sessions.WebAppSession.LaunchListener``

*extends*\ :doc:`ResponseListener <and-responselistener>`

Success block that is called upon successfully launch of a web app.

Passes a WebAppSession Object containing important information about the
web app's session. This object is required to perform many functions
with the web app, including app-to-app communication, media playback,
closing, etc.

Inherited Methods
-----------------

void **onSuccess** (T *object*)
   
    Returns the success of the call of type T.

    **Parameters:**
        * object – Response object, can be any number of object types, depending on the protocol/capability/etc

void **onError** (:doc:`ServiceCommandError <and-servicecommanderror>` *error*)
   
    Method to return the error that was generated. Will pass an error
    object with a helpful status code and error message.

    **Parameters:**
        * error – ServiceCommandError describing the error
