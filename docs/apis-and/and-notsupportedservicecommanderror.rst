NotSupportedServiceCommandError
==============================================================================================
``com.connectsdk.service.command.NotSupportedServiceCommandError``

*extends* :doc:`ServiceCommandError <and-servicecommanderror>`

This class defines an Error which is thrown if feature is not supported by a service implementation

Inherited Methods
-----------------

**ServiceCommandError** ()


int **getCode** ()


Object **getPayload** ()


static :doc:`ServiceCommandError <and-servicecommanderror>` **notSupported** ()
     Create an error which indicates that feature is not supported by a service

     **Returns:** NotSupportedServiceCommandError

static :doc:`ServiceCommandError <and-servicecommanderror>` **getError** (int *code*)
     Create an error from HTTP response code

     **Parameters:**

     * code – HTTP response code

     **Returns:** ServiceCommandError
