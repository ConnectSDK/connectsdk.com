AirPlayServiceHTTPKeepAlive
===========================

The class is responsible for maintaining an AirPlay connection alive by
sending periodic requests.

Properties
----------

CGFloat interval
   The interval between keep-alive requests, in seconds. 50 by default.

id<ServiceCommandDelegate> commandDelegate
   An object that sends AirPlay commands.

NSURL \* commandURL
   The base URL for commands.

Methods
-------

\- (instancetype) **initWithInterval**:(CGFloat)\ *interval* **andCommandDelegate**:(id<ServiceCommandDelegate>)\ *commandDelegate*
   Designated initializer, setting the interval and command delegate.

   **Parameters:**

   -  interval
   -  **andCommandDelegate**: commandDelegate

\- (instancetype) **initWithCommandDelegate**:(id<ServiceCommandDelegate>)\ *commandDelegate*
   Initializer that sets the command delegate.

   **Parameters:**

   -  commandDelegate

\- (void) **startTimer**
   Schedules sending keep-alive requests. The first one will be sent
   after the specified ``interval``.

\- (void) **stopTimer**
   Stops sending keep-alive requests.
