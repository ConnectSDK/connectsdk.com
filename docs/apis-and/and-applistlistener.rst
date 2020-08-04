AppListListener com.connectsdk.service.capability.Launcher.AppListListener
==========================================================================

*extends*\ `ResponseListener </apis/1-6-0/android/ResponseListener>`__

Success block that is called upon successfully getting the app list.

Passes a List containing an AppInfo for each available app on the device

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
