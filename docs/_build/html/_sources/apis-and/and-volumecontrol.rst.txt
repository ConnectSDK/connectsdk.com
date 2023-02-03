VolumeControl 
=============================================================
``com.connectsdk.service.capability.VolumeControl``

*extends CapabilityMethods*

The VolumeControl capability protocol serves to define the methods
required for normalizing common volume specific commands (volume
up/down, mute, etc).

Properties
----------

**final String Any = "VolumeControl.Any"**

**final String Volume_Get = "VolumeControl.Get"**

**final String Volume_Set = "VolumeControl.Set"**

**final String Volume_Up_Down = "VolumeControl.UpDown"**

**final String Volume_Subscribe = "VolumeControl.Subscribe"**

**final String Mute_Get = "VolumeControl.Mute.Get"**

**final String Mute_Set = "VolumeControl.Mute.Set"**

**final String Mute_Subscribe = "VolumeControl.Mute.Subscribe"**

**final String[] Capabilities = { Volume_Get, Volume_Set, Volume_Up_Down, Volume_Subscribe, Mute_Get, Mute_Set, Mute_Subscribe }**

Inner Classes
-------------

* :doc:`MuteListener <and-mutelistener>`
* :doc:`VolumeListener <and-volumelistener>`
* :doc:`VolumeStatus <and-volumestatus>`
* :doc:`VolumeStatusListener <and-volumestatuslistener>`

Methods
-------

:doc:`VolumeControl <and-volumecontrol>` **getVolumeControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getVolumeControlCapabilityLevel** ()

void **volumeUp** (:doc:`ResponseListener <and-responselistener>`\ <Object> *listener*)
    
    Sends the volume up command to the device.

    **Related capabilities:**
        * ``VolumeControl.UpDown``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **volumeDown** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Sends the volume down command to the device.

    **Related capabilities:**
        * ``VolumeControl.UpDown``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **setVolume** (float *volume*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Set the volume of the device.

    **Related capabilities:**
        * ``VolumeControl.Set``

    **Parameters:**
        * volume – Volume as a float between 0.0 and 1.0

        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getVolume** (:doc:`VolumeListener <and-volumelistener>` *listener*)
    
    Get the current volume of the device.

    **Related capabilities:**
        * ``VolumeControl.Get``

    **Parameters:**
        * listener – (optional) VolumeListener with methods to be called on success or failure

void **setMute** (boolean *isMute*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    
    Set the current volume.

    **Related capabilities:**
        * ``VolumeControl.Mute.Set``

    **Parameters:**
        * isMute
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getMute** (:doc:`MuteListener <and-mutelistener>` *listener*)
    
    Get the current mute state.

    **Related capabilities:**
        * ``VolumeControl.Mute.Get``

    **Parameters:**
        * listener – (optional) MuteListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`VolumeListener <and-volumelistener>`> **subscribeVolume** (:doc:`VolumeListener <and-volumelistener>` *listener*)
   
    Subscribe to the volume on the TV.

    **Related capabilities:**
        * ``VolumeControl.Subscribe``

    **Parameters:**
        * listener – (optional) VolumeListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MuteListener <and-mutelistener>`> **subscribeMute** (:doc:`MuteListener <and-mutelistener>` *listener*)
   
    Subscribe to the mute state on the TV.

    **Related capabilities:**
        * ``VolumeControl.Mute.Subscribe``

    **Parameters:**
        * listener – (optional) MuteListener with methods to be called on success or failure
