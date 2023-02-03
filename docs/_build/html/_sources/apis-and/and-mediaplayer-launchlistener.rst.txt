MediaPlayer.LaunchListener
===========================================================================
``com.connectsdk.service.capability.MediaPlayer.LaunchListener``

*extends* :doc:`ResponseListener <and-responselistener>`

Success block that is called upon successfully playing/displaying a media file.

Passes a MediaLaunchObject which contains the objects for controlling media playback.

Inherited Methods
-----------------

void **onSuccess** (T *object*)
     Returns the success of the call of type T.

     **Parameters:**
     
     * object – Response object, can be any number of object types, depending on the protocol/capability/etc

void **onError** (:doc:`ServiceCommandError <and-servicecommanderror>` *error*)
     Method to return the error that was generated. Will pass an error object with a helpful status code and error message.

     **Parameters:**

     * error – ServiceCommandError describing the error
