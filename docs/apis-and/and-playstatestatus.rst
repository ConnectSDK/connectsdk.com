PlayStateStatus
==============================================================================
``com.connectsdk.service.capability.MediaControl.PlayStateStatus``

Enumerates possible playback status

Properties
----------

Unknown
   Unknown state

Idle
   Media source is not set.

Playing
   Media is playing.

Paused
   Media is paused.

Buffering
   Media is buffering on the first screen device (e.g. on the TV)

Methods
-------

static :doc:`PlayStateStatus <and-playstatestatus>` **convertPlayerStateToPlayStateStatus** (int *playerState*)
     Converts int value into PlayStateStatus

     **Parameters:**

     * playerState – int value

     **Returns:** PlayStateStatus

static :doc:`PlayStateStatus <and-playstatestatus>` **convertTransportStateToPlayStateStatus** (String *transportState*)
     Converts String value into PlayStateStatus

     **Parameters:**

     * transportState – String value

     **Returns:** PlayStateStatus
