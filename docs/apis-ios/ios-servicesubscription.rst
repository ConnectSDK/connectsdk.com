ServiceSubscription
===================

*extends*\ :doc:`ServiceCommand <ios-servicecommand>`

Properties
----------

int callId

NSMutableArray \* successCalls

NSMutableArray \* failureCalls

BOOL isSubscribed

Methods
-------

\- (instancetype) **initWithDelegate**:(id<ServiceCommandDelegate>)\ *delegate* **target**:(NSURL \*)\ *target* **payload**:(id)\ *payload* **callId**:(int)\ *callId*
   **Parameters:**

   -  delegate
   -  **target**: target
   -  **payload**: payload
   -  **callId**: callId

\- (void) **addSuccess**:(id)\ *success*
   **Parameters:**

   -  success – Optional id to be called on success

\- (void) **addFailure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  failure – Optional FailureBlock to be called on failure

\- (void) **subscribe**

\- (void) **unsubscribe**

+\ (instancetype) **subscriptionWithDelegate**:(id<ServiceCommandDelegate>)\ *delegate* **target**:(NSURL \*)\ *url* **payload**:(id)\ *payload* **callId**:(int)\ *callId*
   **Parameters:**

   -  delegate
   -  **target**: url
   -  **payload**: payload
   -  **callId**: callId

Inherited Methods
-----------------

\- (instancetype) **initWithDelegate**:(id<ServiceCommandDelegate>)\ *delegate* **target**:(NSURL \*)\ *url* **payload**:(id)\ *payload*
   **Parameters:**

   -  delegate
   -  **target**: url
   -  **payload**: payload

\- (void) **send**

+ (instancetype) **commandWithDelegate**:(id<ServiceCommandDelegate>)\ *delegate* **target**:(NSURL \*)\ *url* **payload**:(id)\ *payload*
   **Parameters:**

   -  delegate
   -  **target**: url
   -  **payload**: payload
