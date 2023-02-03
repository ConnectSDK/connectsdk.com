AppStateChangeNotifier
======================

Listens to app state change events (didEnterBackground and
didBecomeActive, in particular) and allows other components be notified
about them using a simpler API.

Properties
----------

`AppStateChangeBlock <#appstatechangeblock>`__ didBackgroundBlock
   The block is called when the app has entered background.

`AppStateChangeBlock <#appstatechangeblock>`__ didForegroundBlock
   The block is called when the app has entered foreground.

id<:doc:`BlockRunner <ios-blockrunner>`> blockRunner
   The ``BlockRunner`` instance specifying where to run the blocks. The
   default value is the main dispatch queue runner. Cannot be ``nil``,
   as it will reset to the default value.

Methods
-------

\- (void) **startListening**
   Starts listening for app state change events. This method is
   idempotent.

   You **MUST** call ``-stopListening`` for this object to be removed.

\- (void) **stopListening**
   Stops listening for app state change events. This method is
   idempotent.

   This method **MUST** be called to ``dealloc`` this object if you
   called ``-startListening`` before.

Typedefs
--------

AppStateChangeBlock
~~~~~~~~~~~~~~~~~~~

void(^)()

Type of a block that is called on an app state change event.
