ServiceCommandError
======================================================================
``com.connectsdk.service.command.ServiceCommandError``

This class implements base service error which is based on HTTP response
codes

Methods
-------

**ServiceCommandError** ()

**ServiceCommandError** (String *detailMessage*)

    **Parameters:**
        *  detailMessage

**ServiceCommandError** (int *code*, String *detailMessage*)

    **Parameters:**
        *  code
        *  detailMessage

**ServiceCommandError** (int *code*, String *desc*, Object *payload*)

    **Parameters:**
        *  code
        *  desc
        *  payload

int **getCode** ()

Object **getPayload** ()

static :doc:`ServiceCommandError <and-servicecommanderror>` **notSupported** ()

    Create an error which indicates that feature is not supported by a service

    **Returns:** NotSupportedServiceCommandError

static :doc:`ServiceCommandError <and-servicecommanderror>` **getError** (int *code*)

    Create an error from HTTP response code

    **Parameters:**
        *  code – HTTP response code

    **Returns:** ServiceCommandError
