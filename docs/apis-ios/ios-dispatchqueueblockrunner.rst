DispatchQueueBlockRunner
========================

Dispatches a ``block`` asynchronously on the given ``dispatch_queue_t`` queue.

Please use the ``-initWithDispatchQueue``: initializer, because you must specify the ``queue``.

Methods
-------

\- (instancetype) **initWithDispatchQueue**:(dispatch_queue_t)\ *queue*
   Designated initializer. Initializes the object with the given
   ``dispatch queue`` which will run the blocks. The ``queue`` must not
   be ``nil``.

   **Parameters:**

   * queue

\+ (instancetype) **mainQueueRunner**
   Convenience method that returns a block runner with the main dispatch queue.