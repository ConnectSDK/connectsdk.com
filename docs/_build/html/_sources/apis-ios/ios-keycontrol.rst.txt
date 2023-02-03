KeyControl
==========

The KeyControl capability serves to define the methods required for
normalizing common key commands (up, down, left right, ok, back, home,
key code).

Methods
-------

\- (id<:doc:`KeyControl <ios-keycontrol>`>) **keyControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **keyControlPriority**

\- (void) **upWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends the up button key code to the TV.

   **Related capabilities:**

   * ``KeyControl.Up``

   **Parameters:**
      :name: parameters
      :class: method-detail-label

   * success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **downWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends the down button key code to the TV.

   **Related capabilities:**

   * ``KeyControl.Down``

   **Parameters:**

   * success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **leftWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends the left button key code to the TV.

   **Related capabilities:**

   * ``KeyControl.Left``

   **Parameters:**

   * success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **rightWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends the right button key code to the TV.

   **Related capabilities:**

   * ``KeyControl.Right``

   **Parameters:**

   * success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **okWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends the OK button key code to the TV.

   **Related capabilities:**

   * ``KeyControl.OK``

   **Parameters:**

   * success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **backWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends the back button key code to the TV.

   **Related capabilities:**

   * ``KeyControl.Back``

   **Parameters:**

   * success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **homeWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends the home button key code to the TV.

   **Related capabilities:**

   * ``KeyControl.Home``

   **Parameters:**

   * success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **sendKeyCode**:(NSUInteger)\ *keyCode* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends a key code value to the TV.

   **Related capabilities:**

   * ``KeyControl.Send.KeyCode``

   **Parameters:**

   * keyCode

   * **success**: success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure
