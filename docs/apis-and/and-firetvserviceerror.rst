FireTVServiceError
====================================================================
``com.connectsdk.service.command.FireTVServiceError``

*extends* :doc:`ServiceCommandError <and-servicecommanderror>`

This class implements an exception for FireTVService

Methods
-------

**FireTVServiceError** (String *message*)
     **Parameters:**

     * message

**FireTVServiceError** (String *message*, Throwable *e*)
     **Parameters:**

     * message
     * e

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
