MediaControl
===========================================================
``com.connectsdk.service.capability.MediaControl``

*extends CapabilityMethods*

The MediaControl capability protocol serves to define the methods
required for normalizing the control of media playback (play, pause,
fast forward, etc) as well as obtaining media information (playhead
position, duration, etc).

Properties
----------

final String Any = "MediaControl.Any"

final String Play = "MediaControl.Play"

final String Pause = "MediaControl.Pause"

final String Stop = "MediaControl.Stop"

final String Rewind = "MediaControl.Rewind"

final String FastForward = "MediaControl.FastForward"

final String Seek = "MediaControl.Seek"

final String Duration = "MediaControl.Duration"

final String PlayState = "MediaControl.PlayState"

final String PlayState_Subscribe = "MediaControl.PlayState.Subscribe"

final String Position = "MediaControl.Position"

final String Previous = "MediaControl.Previous"
     This capability is deprecated. Use ``PlaylistControl.Previous`` instead.

final String Next = "MediaControl.Next"
     This capability is deprecated. Use ``PlaylistControl.Next`` instead.

final int PLAYER_STATE_UNKNOWN = 0

final int PLAYER_STATE_IDLE = 1

final int PLAYER_STATE_PLAYING = 2

final int PLAYER_STATE_PAUSED = 3

final int PLAYER_STATE_BUFFERING = 4

final String[] Capabilities = { Play, Pause, Stop, Rewind, FastForward, Seek,

Inner Classes
-------------

* :doc:`DurationListener <and-durationlistener>`
* :doc:`PlayStateListener <and-playstatelistener>`
* :doc:`PlayStateStatus <and-playstatestatus>`
* :doc:`PositionListener <and-positionlistener>`

Methods
-------

:doc:`MediaControl <and-mediacontrol>` **getMediaControl** ()
     Get MediaControl implementation

     **Returns:** MediaControl

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaControlCapabilityLevel** ()
     Get a capability priority for current implementation

     **Returns:** CapabilityPriorityLevel

void **play** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Send play command.

     **Related capabilities:**

     * ``MediaControl.Play``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **pause** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Send pause command.

     **Related capabilities:**

     * ``MediaControl.Pause``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **stop** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Send play command.

     **Related capabilities:**

     * ``MediaControl.Stop``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **rewind** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Send rewind command.

     **Related capabilities:**

     * ``MediaControl.Rewind``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **fastForward** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Send play command.

     **Related capabilities:**

     * ``MediaControl.FastForward``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **previous** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     This method is deprecated. Use ``PlaylistControl::previous(ResponseListener<Object> listener)`` instead.

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **next** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     This method is deprecated. Use ``PlaylistControl::next(ResponseListener<Object> listener)`` instead.

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **seek** (long *position*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Seeks to a new position within the current media item

     **Related capabilities:**

     * ``MediaControl.Seek``

     **Parameters:**

     * position – The new position, in milliseconds from the beginning of the stream
     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getDuration** (:doc:`DurationListener <and-durationlistener>` *listener*)
     Get the current media duration in milliseconds

     **Parameters:**

     * listener – (optional) DurationListener with methods to be called on success or failure

void **getPosition** (:doc:`PositionListener <and-positionlistener>` *listener*)
     Get the current playback position in milliseconds

     **Parameters:**

     * listener – (optional) PositionListener with methods to be called on success or failure

void **getPlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)
     Get the current state of playback

     **Parameters:**

     * listener – (optional) PlayStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`PlayStateListener <and-playstatelistener>`> **subscribePlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)
     Subscribe for playback state changes

     **Parameters:**

     * listener – receives play state notifications

     **Returns:** ServiceSubscription<PlayStateListener>
