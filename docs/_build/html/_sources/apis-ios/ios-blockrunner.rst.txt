BlockRunner
===========

Abstracts and encapsulates asynchrony, that is how and where blocks are
run. Using this protocol, you can easily change which dispatch queue or
``NSOperationQueue`` delegate blocks are run on, instead of hard-coding
``dispatch_async(dispatch_get_main_queue(), ^{ });``. For example:

.. code-block:: objc

   dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_BACKGROUND, 0);
   AppStateChangeNotifier *notifier = [AppStateChangeNotifier new];
   notifier.blockRunner = [[DispatchQueueBlockRunner alloc] initWithDispatchQueue:queue];

Another great use case is turning asynchronous tests into synchronous,
making them faster and easier:

.. code-block:: objc

   - (void)testStartListeningShouldSubscribeToDidBackgroundEvent {
       AppStateChangeNotifier *notifier = [AppStateChangeNotifier new];
       notifier.blockRunner = [SynchronousBlockRunner new];
       [notifier startListening];

       __block BOOL verified = NO;
       notifier.didBackgroundBlock = ^{
           verified = YES;
       };
       [self postNotificationName:UIApplicationDidEnterBackgroundNotification];

       XCTAssertTrue(verified, @"didBackgroundBlock should be called");
   }

Here we use the synchronous block runner (instead of the default
asynchronous, main queue one) to avoid writing asynchronous tests with
``XCTestExpectation``.

Methods
-------

\- (void) **runBlock**:(nonnull `VoidBlock <#VoidBlock>`__)\ *block*
   Runs the given ``block`` somewhere, depending on the concrete
   implementation.

   **Parameters:**

   * block – block to run; must not be ``nil``.

\- (void) **runBlock**:(nonnull `VoidBlock <#VoidBlock>`__)\ *block*
   Runs the given ``block`` somewhere, depending on the concrete
   implementation.

   **Parameters:**

   * block – block to run; must not be ``nil``.

Typedefs
--------

VoidBlock
~~~~~~~~~

void(^)(void)

A type for blocks without arguments and no return value.
