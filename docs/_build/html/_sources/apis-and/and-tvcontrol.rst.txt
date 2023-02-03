TVControl 
=====================================================
``com.connectsdk.service.capability.TVControl``

*extends CapabilityMethods*

The TVControl capability protocol serves to define the methods required
for normalizing common TV-specific commands (channel up/down, channel
list, channel info, etc).

Properties
----------

**final String Any = "TVControl.Any"**

**final String Channel_Get = "TVControl.Channel.Get"**

**final String Channel_Set = "TVControl.Channel.Set"**

**final String Channel_Up = "TVControl.Channel.Up"**

**final String Channel_Down = "TVControl.Channel.Down"**

**final String Channel_List = "TVControl.Channel.List"**

**final String Channel_Subscribe = "TVControl.Channel.Subscribe"**

**final String Program_Get = "TVControl.Program.Get"**

**final String Program_List = "TVControl.Program.List"**

**final String Program_Subscribe = "TVControl.Program.Subscribe"**

**final String Program_List_Subscribe = "TVControl.Program.List.Subscribe"**

**final String Get_3D = "TVControl.3D.Get"**

**final String Set_3D = "TVControl.3D.Set"**

**final String Subscribe_3D = "TVControl.3D.Subscribe"**

**final String[] Capabilities = { Channel_Get, Channel_Set, Channel_Up, Channel_Down, Channel_List, Channel_Subscribe, Program_Get, Program_List, Program_Subscribe, Program_List_Subscribe, Get_3D, Set_3D, Subscribe_3D }**

Inner Classes
-------------

* :doc:`ChannelListener <and-channellistener>`
* :doc:`ChannelListListener <and-channellistlistener>`
* :doc:`ProgramInfoListener <and-programinfolistener>`
* :doc:`ProgramListListener <and-programlistlistener>`
* :doc:`State3DModeListener <and-state3dmodelistener>`

Methods
-------

:doc:`TVControl <and-tvcontrol>` **getTVControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getTVControlCapabilityLevel** ()

void **channelUp** (:doc:`ResponseListener <and-responselistener>`\ <Object> *listener*)

    Sends a channel up command to the TV.

    **Related capabilities:**
        * ``TVControl.Channel.Up``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **channelDown** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Sends a channel down command to the TV.

    **Related capabilities:**
        * ``TVControl.Channel.Down``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **setChannel** (:doc:`ChannelInfo <and-channelinfo>` *channelNumber*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Sets the current channel to the channel provided by the ChannelInfo object provided.

    **Related capabilities:**
        * ``TVControl.Channel.Set``

    **Parameters:**
        * channelNumber
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getCurrentChannel** (:doc:`ChannelListener <and-channellistener>` *listener*)
   
    Gets the current channel info from the TV.

    **Related capabilities:**
        * ``TVControl.Channel.Get``

    **Parameters:**
        * listener – (optional) ChannelListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ChannelListener <and-channellistener>`> **subscribeCurrentChannel** (`ChannelListener <and-channellistener>` *listener*)
   
    Subscribes to any changes in the current channel. Each time the channel is changed, the new channel's info 
    will be provided to the success callback.

    **Related capabilities:**
        * ``TVControl.Channel.Subscribe``

    **Parameters:**
        * listener – (optional) ChannelListener with methods to be called on success or failure

void **getChannelList** (:doc:`ChannelListListener <and-channellistlistener>` *listener*)
    
    Get a list of available channels from the TV.

    **Related capabilities:**
        * ``TVControl.Channel.List``

    **Parameters:**
        * listener – (optional) ChannelListListener with methods to be called on success or failure

void **getProgramInfo** (:doc:`ProgramInfoListener <and-programinfolistener>` *listener*)
   
    Gets the current program info from the TV.

    **Related capabilities:**
        * ``TVControl.Program.Get``

    **Parameters:**
        * listener – (optional) ProgramInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ProgramInfoListener <and-programinfolistener>`> **subscribeProgramInfo** (:doc:`ProgramInfoListener <and-programinfolistener>` *listener*)
   
    Subscribes to any changes in the current program. Each time the
    channel is changed or a new program starts, the new program's info
    will be provided to the success callback.

    **Related capabilities:**
        * ``TVControl.Program.Subscribe``

    **Parameters:**
        * listener – (optional) ProgramInfoListener with methods to be called on success or failure

void **getProgramList** (:doc:`ProgramListListener <and-programlistlistener>` *listener*)
   
    Gets a list of all programs scheduled to play on the current channel.

    **Related capabilities:**
        * ``TVControl.Program.List``

    **Parameters:**
        * listener – (optional) ProgramListListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`ProgramListListener <and-programlistlistener>`> **subscribeProgramList** (:doc:`ProgramListListener <and-programlistlistener>` *listener*)
   
    Subscribes to any changes in the current program. Each time the
    channel is changed or a new program starts, the new program's info
    will be provided to the success callback.

    **Related capabilities:**
        * ``TVControl.Program.List.Subscribe``

    **Parameters:**
        * listener – (optional) ProgramListListener with methods to be called on success or failure

void **get3DEnabled** (:doc:`State3DModeListener <and-state3dmodelistener>` *listener*)
   
    Gets the current 3D status of the TV.

    **Related capabilities:**
        * ``TVControl.3D.Get``

    **Parameters:**
        * listener – (optional) State3DModeListener with methods to be called on success or failure

void **set3DEnabled** (boolean *enabled*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
  
    Sets the current 3D status of the TV.

    **Related capabilities:**
        * ``TVControl.3D.Set``

    **Parameters:**
        * enabled – Whether the TV's 3D mode should be on or off
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`State3DModeListener <and-state3dmodelistener>`> **subscribe3DEnabled** (:doc:`State3DModeListener <and-state3dmodelistener>` *listener*)
   
    Subscribes to changes in the TV's 3D status.

    **Related capabilities:**
        * ``TVControl.3D.Subscribe``

    **Parameters:**
        * listener – (optional) State3DModeListener with methods to be called on success or failure
