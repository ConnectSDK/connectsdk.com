VolumeListener 
=============================================================================
``com.connectsdk.service.capability.VolumeControl.VolumeListener``

*extends* :doc:`ResponseListener <and-responselistener>`

Success block that is called upon successfully getting the device's
system volume.

Passes the current system volume, value is a float between 0.0 and 1.0

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
