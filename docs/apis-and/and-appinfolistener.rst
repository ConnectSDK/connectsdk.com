AppInfoListener 
===============
``com.connectsdk.service.capability.Launcher.AppInfoListener``

*extends* :doc:`ResponseListener <and-responselistener>`

Success listener that is called upon requesting info about the current
running app.

Passes an AppInfo object containing info about the running app

Inherited Methods
-----------------

void **onSuccess** (T *object*)
    Returns the success of the call of type T.

    **Parameters:**

    -  object – Response object, can be any number of object types, depending on the protocol/capability/etc

void **onError** (:doc:`ServiceCommandError <and-servicecommanderror>` *error*)
    Method to return the error that was generated. Will pass an error
    object with a helpful status code and error message.

    **Parameters:**

    -  error – ServiceCommandError describing the error
