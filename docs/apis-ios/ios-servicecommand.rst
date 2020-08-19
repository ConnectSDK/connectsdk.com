ServiceCommand
==============

Properties
----------

id<ServiceCommandDelegate> delegate

SuccessBlock callbackComplete

FailureBlock callbackError

NSString \* HTTPMethod

id payload

NSURL \* target

Methods
-------

\- (instancetype) **initWithDelegate**:(id<ServiceCommandDelegate>)\ *delegate* **target**:(NSURL \*)\ *url* **payload**:(id)\ *payload*
   **Parameters:**

   -  delegate
   -  **target**: url
   -  **payload**: payload

\- (void) **send**

\+ (instancetype) **commandWithDelegate**:(id<ServiceCommandDelegate>)\ *delegate* **target**:(NSURL \*)\ *url* **payload**:(id)\ *payload*
   **Parameters:**

   -  delegate
   -  **target**: url
   -  **payload**: payload
