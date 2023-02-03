TextInputControl
================

The TextInputControl capability serves to define the methods required
for normalizing common text input commands (send text, enter, delete,
keyboard status).

Methods
-------

textInputControl.\ **sendText** (*input*)
   Send text to the current text field.

   **Related capabilities:**

   -  ``TextInputControl.Send.Text``

   **Parameters:**

   -  input (string)

   **Returns:** :doc:`Command <cor-command>`

textInputControl.\ **sendEnter** ()
   Send enter key to the current text field.

   **Related capabilities:**

   -  ``TextInputControl.Send.Enter``

   **Returns:** :doc:`Command <cor-command>`

textInputControl.\ **sendDelete** ()
   Send delete event to the current text field.

   **Related capabilities:**

   -  ``TextInputControl.Send.Delete``

   **Returns:** :doc:`Command <cor-command>`

textInputControl.\ **subscribeTextInputStatus** ()
   Subscribe to information about the current text field.

   On success, the success event/callback will be fired with the
   arguments (textInputStatus)

   -  textInputStatus: TextInputStatus

   **Related capabilities:**

   -  ``TextInputControl.Subscribe``

   **Returns:** :doc:`Subscription <cor-subscription>`
