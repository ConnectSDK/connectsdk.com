PowerControl
============

The PowerControl capability protocol serves to define the methods
required for normalizing power off functionality.

Methods
-------

\- (id<:doc:`PowerControl <ios-powercontrol>`>) **powerControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **powerControlPriority**

\- (void) **powerOffWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends a power off signal to the TV. A success message will,
   internally, trigger a disconnection with the device.

   **Related capabilities:**

   -  ``PowerControl.Off``

  **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **powerOnWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure
