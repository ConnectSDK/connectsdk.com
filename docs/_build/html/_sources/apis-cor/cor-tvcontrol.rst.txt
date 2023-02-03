TVControl
=========

The TVControl capability protocol serves to define the methods required
for normalizing common TV-specific commands (channel up/down, channel
list, channel info, etc).

ChannelInfo objects are plain JavaScript objects with the following
properties:

-  id (string): A platform-specific id used to identify the channel
-  name (string): A human-readable name of the channel, if available
-  number (string): Channel number such as "54-1"
-  majorNumber (number): Major channel number
-  minorNumber (minorNumber: Minor channel number (subchannel number)

Methods
-------

tvControl.\ **channelUp** ()
   Sends a channel up command to the TV.

   **Related capabilities:**

   -  ``TVControl.Channel.Up``

   **Returns:** :doc:`Command <cor-command>`

tvControl.\ **channelDown** ()
   Sends a channel down command to the TV.

   **Related capabilities:**

   -  ``TVControl.Channel.Down``

   **Returns:** :doc:`Command <cor-command>`

tvControl.\ **setChannel** (*channelInfo*)
   Sets the current channel to the channel provided by the ChannelInfo
   object provided.

   **Related capabilities:**

   -  ``TVControl.Channel.Set``

   **Parameters:**

   -  channelInfo (object) – ChannelInfo object containing information about the desired
      channel

   **Returns:** :doc:`Command <cor-command>`

tvControl.\ **getChannelList** ()
   Get a list of available channels from the TV.

   On success, the success event/callback will be fired with the
   arguments (channelInfoList)

   -  channelInfoList: ChannelInfo[]

   **Related capabilities:**

   -  ``TVControl.Channel.List``

   **Returns:** :doc:`Command <cor-command>`

tvControl.\ **getCurrentChannel** ()
   Gets the current channel info from the TV.

   On success, the success event/callback will be fired with the
   arguments (channelInfo)

   -  channelInfo: ChannelInfo

   **Related capabilities:**

   -  ``TVControl.Channel.Get``

   **Returns:** :doc:`Command <cor-command>`

tvControl.\ **subscribeCurrentChannel** ()
   Subscribes to any changes in the current channel. Each time the
   channel is changed, the new channel's info will be provided to the
   success callback.

   On success, the success event/callback will be fired with the
   arguments (channelInfo)

   -  channelInfo: ChannelInfo

   **Related capabilities:**

   -  ``TVControl.Channel.Subscribe``

   **Returns:** :doc:`Subscription <cor-subscription>`
