PowerControl
============

The PowerControl capability protocol serves to define the methods
required for normalizing power off functionality.

Methods
-------

powerControl.\ **powerOff** ()
   Sends a power off signal to the TV. A success message will,
   internally, trigger a disconnection with the device.

   **Related capabilities:**

   -  ``PowerControl.Off``

   **Returns:** :doc:`Command <cor-command>`
