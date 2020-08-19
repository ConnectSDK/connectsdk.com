MouseControl
============

The MouseControl capability serves to define the methods required for
normalizing a mouse/trackpad (move/scroll with relative coordinates and
click).

Methods
-------

\- (id<:doc:`MouseControl <ios-mousecontrol>`>) **mouseControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **mouseControlPriority**

\- (void) **connectMouseWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Establish a connection with the DeviceService's mouse communication
   medium (WebSocket, HTTP, etc). While this step may not be necessary
   with certain platforms, it is suggested to call it anyways, for
   purposes of seamless normalization. Calling connect on a
   non-connectable protocol will just trigger the success callback
   immediately.

   **Related capabilities:**

   -  ``MouseControl.Connect``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **disconnectMouse**
   Disconnects from the mouse communication medium.

   **Related capabilities:**

   -  ``MouseControl.Disconnect``

\- (void) **clickWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Perform a click action at the current mouse position.

   **Related capabilities:**

   -  ``MouseControl.Click``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **move**:(CGVector)\ *distance* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Move the mouse by the given distance values.

   **Related capabilities:**

   -  ``MouseControl.Move``

   **Parameters:**

   -  distance – Distance to move the mouse relative to its current position

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **scroll**:(CGVector)\ *distance* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Scroll by the given distance values.

   **Related capabilities:**

   -  ``MouseControl.Scroll``

   **Parameters:**

   -  distance – Distance to scroll relative to current position

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure
