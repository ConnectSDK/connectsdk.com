MouseControl
============

The MouseControl capability serves to define the methods required for
normalizing a mouse/trackpad (move/scroll with relative coordinates and
click).

Methods
-------

mouseControl.\ **connectMouse** ()
   Establish a connection with the DeviceService's mouse communication
   medium (WebSocket, HTTP, etc). While this step may not be necessary
   with certain platforms, it is suggested to call it anyways, for
   purposes of seamless normalization. Calling connect on a
   non-connectable protocol will just trigger the success callback
   immediately.

   **Related capabilities:**

   -  ``MouseControl.Connect``

   **Returns:** :doc:`Command <cor-command>`

mouseControl.\ **disconnectMouse** ()
   Disconnects from the mouse communication medium.

   **Related capabilities:**

   -  ``MouseControl.Disconnect``

   **Returns:** :doc:`Command <cor-command>`

mouseControl.\ **move** (*dx*, *dy*)
   Move the mouse by the given distance values.

   **Related capabilities:**

   -  ``MouseControl.Move``

   **Parameters:**

   -  dx (number) – Distance to move the mouse on the x-axis relative to its current
      position

   -  dy (number) – Distance to move the mouse on the y-axis relative to its current
      position

   **Returns:** :doc:`Command <cor-command>`

mouseControl.\ **scroll** (*dx*, *dy*)
   Scroll by the given distance values.

   **Related capabilities:**

   -  ``MouseControl.Scroll``

   **Parameters:**

   -  dx (number) – Distance to scroll the mouse on the x-axis relative to its current
      position

   -  dy (number) – Distance to scroll the mouse on the y-axis relative to its current
      position

   **Returns:** :doc:`Command <cor-command>`

mouseControl.\ **click** ()
   Perform a click action at the current mouse position.

   **Related capabilities:**

   -  ``MouseControl.Click``

   **Returns:** :doc:`Command <cor-command>`
