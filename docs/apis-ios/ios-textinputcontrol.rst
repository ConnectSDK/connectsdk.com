TextInputControl
================

The TextInputControl capability serves to define the methods required
for normalizing common text input commands (send text, enter, delete,
keyboard status).

Methods
-------

\- (id<`TextInputControl </apis/1-6-0/ios/TextInputControl>`__>) **textInputControl**

\- (`CapabilityPriorityLevel </apis/1-6-0/ios/CapabilityPriorityLevel>`__) **textInputControlPriority**

\- (`ServiceSubscription </apis/1-6-0/ios/ServiceSubscription>`__ \*) **subscribeTextInputStatusWithSuccess**:(`TextInputStatusInfoSuccessBlock <#textinputstatusinfosuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
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

void(^)(`TextInputStatusInfo </apis/1-6-0/ios/TextInputStatusInfo>`__
\*textInputStatusInfo)

Response block that is fired on any change of keyboard visibility.

-  textInputStatusInfo

   provides keyboard type & visibility information
