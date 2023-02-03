ChannelListener
===============
``com.connectsdk.service.capability.TVControl.ChannelListener``

*extends* :doc:`ResponseListener <and-responselistener>`

Success block that is called upon successfully getting the current
channel's information.

Passes a ChannelInfo object containing information about the current
channel

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
