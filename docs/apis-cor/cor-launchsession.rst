LaunchSession
=============

A LaunchSession represents the result of an app launch. Its primary
purpose is to be able to close an app that was previously launched,
using the launchSession.close() method.

Methods
-------

launchSession.\ **close** ()
   Close the app/media associated with this launch session.

Mixin Methods - WrappedObject
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

launchSession.\ **acquire** ()
   Indicate that you would like to keep an active reference to this
   object. Wrapped objects that are not acquired may be freed after the
   success callback returns.

   **Returns:** object – reference to object

launchSession.\ **release** ()
   Release the reference to this object. After calling .release(), this
   object may no longer be used. You should always release objects when
   you no longer need them, to avoid memory leaks.
