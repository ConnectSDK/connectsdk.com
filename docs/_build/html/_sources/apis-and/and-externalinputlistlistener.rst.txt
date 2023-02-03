ExternalInputListListener
=========================
``com.connectsdk.service.capability.ExternalInputControl.ExternalInputListListener``

*extends* :doc:`ResponseListener <and-responselistener>`

Success block that is called upon successfully getting the external
input list.

Passes a list containing an ExternalInputInfo object for each available
external input on the device

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
