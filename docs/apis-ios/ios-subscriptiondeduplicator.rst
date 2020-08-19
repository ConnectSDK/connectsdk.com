SubscriptionDeduplicator
========================

Deduplicates subscription notifications with the same state. The state
can be of any class, allowing ``NSNumber``-wrapped values.

It's an immutable class.

Methods
-------

\- (instancetype) **runBlock**:(dispatch_block_t)\ *block* **ifStateDidChangeTo**:(id)\ *newState*
   If the new ``state`` is different from the previous one, runs the
   ``block`` synchronously.

   **Parameters:**

   -  block
   -  **ifStateDidChangeTo**: newState

   **Returns:** a new instance that you should save to track the new state.
