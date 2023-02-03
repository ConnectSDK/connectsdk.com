CapabilityFilter
================

CapabilityFilter consists of a list of capabilities which must all be
present in order for the filter to match.

For example,

.. code-block:: java
    
    new ConnectSDK.CapabilityFilter([ConnectSDK.Capabilities.MediaPlayer.Play.Video, 
                                     ConnectSDK.Capabilities.MediaControl.Pause])

describes a device that supports showing a video and pausing it.

Methods
-------

new **CapabilityFilter** (*capabilities*)
    
    Create a CapabilityFilter
    
    **Parameters:**
        * capabilities (string[]) – array of capabilities

capabilityFilter. **getCapabilities** ()

    **Returns:** string[] – list of capabilities in filter
