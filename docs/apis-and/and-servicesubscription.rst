ServiceSubscription 
======================================================================
``com.connectsdk.service.command.ServiceSubscription``

Methods
-------

void **unsubscribe** ()

T **addListener** (T *listener*)

    **Parameters:**
        * listener – (optional) T with methods to be called on success or failure

void **removeListener** (T *listener*)

    **Parameters:**
        * listener – (optional) T with methods to be called on success or failure

List<T> **getListeners** ()
