AppInfoListener com.connectsdk.service.capability.Launcher.AppInfoListener
==========================================================================

*extends*\ `ResponseListener </apis/1-6-0/android/ResponseListener>`__

Success listener that is called upon requesting info about the current
running app.

Passes an AppInfo object containing info about the running app

Inherited Methods
-----------------

void **onSuccess** (T *object*)
   Returns the success of the call of type T.

   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  object –

      Response object, can be any number of object types, depending on
      the protocol/capability/etc

void **onError** (`ServiceCommandError </apis/1-6-0/android/ServiceCommandError>`__ *error*)
   Method to return the error that was generated. Will pass an error
   object with a helpful status code and error message.

   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  error –

      ServiceCommandError describing the error