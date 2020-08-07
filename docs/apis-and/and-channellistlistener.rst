ChannelListListener
===================
``com.connectsdk.service.capability.TVControl.ChannelListListener``

*extends* :doc:`ResponseListener <and-responselistener>`

Success block that is called upon successfully getting the channel list.

Passes a List of ChannelList objects for each available channel on the
TV

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
