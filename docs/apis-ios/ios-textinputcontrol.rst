TextInputControl
================

The TextInputControl capability serves to define the methods required
for normalizing common text input commands (send text, enter, delete,
keyboard status).

Methods
-------

\- (id<:doc:`TextInputControl <ios-textinputcontrol>`>) **textInputControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **textInputControlPriority**

\- (:doc:`ServiceSubscription <ios-servicesubscription>` \*) **subscribeTextInputStatusWithSuccess**:(`TextInputStatusInfoSuccessBlock <#textinputstatusinfosuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribe to information about the current text field.

   **Related capabilities:**

   -  ``TextInputControl.Subscribe``

   **Parameters:**

   -  success – Optional TextInputStatusInfoSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **sendText**:(NSString \*)\ *input* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Send text to the current text field.

   **Related capabilities:**

   -  ``TextInputControl.Send.Text``

   **Parameters:**

   -  input

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **sendEnterWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Send enter key to the current text field.

   **Related capabilities:**

   -  ``TextInputControl.Send.Enter``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **sendDeleteWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Send delete event to the current text field.

   **Related capabilities:**

   -  ``TextInputControl.Send.Delete``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

Typedefs
--------

TextInputStatusInfoSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

void(^)(:doc:`TextInputStatusInfo <ios-textinputstatusinfo>`
\*textInputStatusInfo)

Response block that is fired on any change of keyboard visibility.

-  textInputStatusInfo

   provides keyboard type & visibility information
