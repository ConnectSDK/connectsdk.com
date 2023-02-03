PlaylistControl
=================================================================
``com.connectsdk.service.capability.PlaylistControl``

*extends CapabilityMethods*

The PlaylistControl capability interface serves to define the methods
required for normalizing the control of playlist (next, previous, jumpToTrack, etc)

Properties
----------

final String Any = "PlaylistControl.Any"

final String JumpToTrack = "PlaylistControl.JumpToTrack"

final String SetPlayMode = "PlaylistControl.SetPlayMode"

final String Previous = "PlaylistControl.Previous"

final String Next = "PlaylistControl.Next"

final String[] Capabilities = { Previous, Next, JumpToTrack, SetPlayMode, JumpToTrack, }

Inner Classes
-------------

* :doc:`PlayMode <and-playmode>`

Methods
-------

:doc:`PlaylistControl <and-playlistcontrol>` **getPlaylistControl** ()


:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPlaylistControlCapabilityLevel** ()


void **previous** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Jump playlist to the previous track.

     Play previous track in the playlist

     **Related capabilities:**

     * ``PlaylistControl.Previous``

     **Parameters:**

     * listener – optional response listener

void **next** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Jump playlist to the next track.

     Play next track in the playlist

     **Related capabilities:**

     * ``PlaylistControl.Next``

     **Parameters:**

     * listener – optional response listener

void **jumpToTrack** (long *index*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Jump the playlist to the designated track.

     Play a track specified by index in the playlist

     **Related capabilities:**

     * ``PlaylistControl.JumpToTrack``

     **Parameters:**

     * index – index in the playlist, it starts from zero like index of array
     * listener – optional response listener

void **setPlayMode** (:doc:`PlayMode <and-playmode>` *playMode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Set order of playing tracks

     **Parameters:**
     
     * playMode
     * listener – optional response listener
