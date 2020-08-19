ResponseListener 
=============================================================================
``com.connectsdk.service.capability.listeners.ResponseListener``

*extends* :doc:`ErrorListener <and-errorlistener>`

Generic asynchronous operation response success handler block. If there
is any response data to be processed, it will be provided via the
responseObject parameter.

* responseObject
    Contains the output data as a generic object reference. This value 
    may be any of a number of types as defined by T in subclasses of
    ResponseListener. It is also possible that responseObject will be nil
    for operations that don't require data to be returned (move mouse, send key code, etc).

Methods
-------

void **onSuccess** (T *object*)

    Returns the success of the call of type T.

    **Parameters:**
        * object – Response object, can be any number of object types, depending on the protocol/capability/etc

Inherited Methods
-----------------

void **onError** (:doc:`ServiceCommandError <and-servicecommanderror>` *error*)

    Method to return the error that was generated. Will pass an error
    object with a helpful status code and error message.

    **Parameters:**
        * error – ServiceCommandError describing the error
