ExternalInputControl
====================

The ExternalInputControl capability serves to define the methods
required for normalizing all functions regarding external input
switching and general info.

ExternalInputInfo objects are plain JavaScript objects with the
following properties:

-  id (string): A platform-specific id representing an input device
-  name (string): A human-readable name for the input device

Methods
-------

externalInputControl.\ **getExternalInputList** ()
   Get a list of input devices (HDMI, AV, etc) connected to the device

   On success, the success event/callback will be fired with the
   arguments (externalInputList)

   -  externalInputList: ExternalInputInfo[]

   **Related capabilities:**

   -  ``ExternalInputControl.List``

   **Returns:** :doc:`Command <cor-command>`

externalInputControl.\ **setExternalInput** (*externalInputInfo*)
   Switch to the specified external input

   **Related capabilities:**

   -  ``ExternalInputControl.Set``

   **Parameters:**

   -  externalInputInfo (object) – Object containing the proper info to set current input. For best
      cross-platform support, it is suggested to get ExternalInputInfo
      references from getExternalInputList, if possible.

   **Returns:** :doc:`Command <cor-command>`

externalInputControl.\ **showExternalInputPicker** ()
   **Returns:** :doc:`Command <cor-command>`
