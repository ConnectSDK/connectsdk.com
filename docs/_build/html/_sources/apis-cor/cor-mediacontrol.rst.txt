MediaControl
============

The MediaControl capability protocol serves to define the methods
required for normalizing the control of media playback (play, pause,
fast forward, etc) as well as obtaining media information (playhead
position, duration, etc).

Methods
-------

mediaControl.\ **play** ()
   Send play command.

   **Related capabilities:**

   -  ``MediaControl.Play``

   **Returns:** :doc:`Command <cor-command>`

mediaControl.\ **pause** ()
   Send pause command.

   **Related capabilities:**

   -  ``MediaControl.Pause``

   **Returns:** :doc:`Command <cor-command>`

mediaControl.\ **stop** ()
   Send play command.

   **Related capabilities:**

   -  ``MediaControl.Stop``

   **Returns:** :doc:`Command <cor-command>`

mediaControl.\ **rewind** ()
   Send rewind command.

   **Related capabilities:**

   -  ``MediaControl.Rewind``

   **Returns:** :doc:`Command <cor-command>`

mediaControl.\ **fastForward** ()
   Send play command.

   **Related capabilities:**

   -  ``MediaControl.FastForward``

   **Returns:** :doc:`Command <cor-command>`

mediaControl.\ **seek** (*position*)
   Seeks to a new position within the current media item

   **Related capabilities:**

   -  ``MediaControl.Seek``

   **Parameters:**

   -  position (number) – Media seek position in seconds

   **Returns:** :doc:`Command <cor-command>`

mediaControl.\ **getDuration** ()
   On success, the success event/callback will be fired with the
   arguments (duration)

   -  duration: number – duration in seconds

   **Returns:** :doc:`Command <cor-command>`

mediaControl.\ **getPosition** ()
   On success, the success event/callback will be fired with the
   arguments (position)

   -  position: number – position in seconds

   **Returns:** :doc:`Command <cor-command>`

mediaControl.\ **subscribePlayState** ()
   On success, the success event/callback will be fired with the
   arguments (playState)

   -  playState: string – One of:

      -  "unknown"
      -  "idle"
      -  "playing"
      -  "paused"
      -  "buffering"
      -  "finished"

   **Returns:** :doc:`Command <cor-command>`
