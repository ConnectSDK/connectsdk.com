KeyControl
==========

The KeyControl capability serves to define the methods required for
normalizing common key commands (up, down, left right, ok, back, home,
key code).

Methods
-------

keyControl.\ **up** ()
   Sends the up button key code to the TV.

   **Related capabilities:**

   -  ``KeyControl.Up``

   **Returns:** :doc:`Command <cor-command>`

keyControl.\ **down** ()
   Sends the down button key code to the TV.

   **Related capabilities:**

   -  ``KeyControl.Down``

   **Returns:** :doc:`Command <cor-command>`

keyControl.\ **left** ()
   Sends the left button key code to the TV.

   **Related capabilities:**

   -  ``KeyControl.Left``

   **Returns:** :doc:`Command <cor-command>`

keyControl.\ **right** ()
   Sends the right button key code to the TV.

   **Related capabilities:**

   -  ``KeyControl.Right``

   **Returns:** :doc:`Command <cor-command>`

keyControl.\ **ok** ()
   Sends the OK button key code to the TV.

   **Related capabilities:**

   -  ``KeyControl.OK``

   **Returns:** :doc:`Command <cor-command>`

keyControl.\ **back** ()
   Sends the back button key code to the TV.

   **Related capabilities:**

   -  ``KeyControl.Back``

   **Returns:** :doc:`Command <cor-command>`

keyControl.\ **home** ()
   Sends the home button key code to the TV.

   **Related capabilities:**

   -  ``KeyControl.Home``

   **Returns:** :doc:`Command <cor-command>`

keyControl.\ **sendKeyCode** (*keyCode*)
   Sends a key code value to the TV.

   **Related capabilities:**

   -  ``KeyControl.Send.KeyCode``

   **Parameters:**

   -  keyCode (number) – Refer to the native Connect SDK device services for a list of
      keycodes

   **Returns:** :doc:`Command <cor-command>`
