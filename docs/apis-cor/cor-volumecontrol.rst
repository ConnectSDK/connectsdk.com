VolumeControl
=============

The VolumeControl capability protocol serves to define the methods
required for normalizing common volume specific commands (volume
up/down, mute, etc).

Methods
-------

volumeControl.\ **getVolume** ()
   Get the current volume of the device.

   On success, the success event/callback will be fired with the
   arguments (volume)

   -  volume: number

   **Related capabilities:**

   -  ``VolumeControl.Get``

   **Returns:** :doc:`Command <cor-command>`

volumeControl.\ **setVolume** (*volume*)
   Set the volume of the device.

   **Related capabilities:**

   -  ``VolumeControl.Set``

   **Parameters:**

   -  volume (float) – Volume as a float between 0.0 and 1.0

   **Returns:** :doc:`Command <cor-command>`

volumeControl.\ **volumeUp** ()
   Sends the volume up command to the device.

   **Related capabilities:**

   -  ``VolumeControl.UpDown``

   **Returns:** :doc:`Command <cor-command>`

volumeControl.\ **volumeDown** ()
   Sends the volume down command to the device.

   **Related capabilities:**

   -  ``VolumeControl.UpDown``

   **Returns:** :doc:`Command <cor-command>`

volumeControl.\ **getMute** ()
   Get the current mute state.

   On success, the success event/callback will be fired with the
   arguments (mute)

   -  mute: boolean

   **Related capabilities:**

   -  ``VolumeControl.Mute.Get``

   **Returns:** :doc:`Command <cor-command>`

volumeControl.\ **setMute** (*mute*)
   Set the current volume.

   **Related capabilities:**

   -  ``VolumeControl.Mute.Set``

   **Parameters:**

   -  mute (boolean)

   **Returns:** :doc:`Command <cor-command>`

volumeControl.\ **subscribeMute** ()
   Subscribe to the mute state on the TV.

   On success, the success event/callback will be fired with the
   arguments (mute)

   -  mute: boolean

   **Related capabilities:**

   -  ``VolumeControl.Mute.Subscribe``

   **Returns:** :doc:`Subscription <cor-subscription>`

volumeControl.\ **subscribeVolume** ()
   Subscribe to the volume on the TV.

   On success, the success event/callback will be fired with the
   arguments (volume)

   -  volume: number

   **Related capabilities:**

   -  ``VolumeControl.Subscribe``

   **Returns:** :doc:`Subscription <cor-subscription>`
