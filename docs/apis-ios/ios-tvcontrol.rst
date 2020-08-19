TVControl
=========

The TVControl capability protocol serves to define the methods required
for normalizing common TV-specific commands (channel up/down, channel
list, channel info, etc).

Methods
-------

\- (id<`TVControl </apis/1-6-0/ios/TVControl>`__>) **tvControl**

\- (`CapabilityPriorityLevel </apis/1-6-0/ios/CapabilityPriorityLevel>`__) **tvControlPriority**

\- (void) **channelUpWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends a channel up command to the TV.

   **Related capabilities:**

   -  ``TVControl.Channel.Up``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **channelDownWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends a channel down command to the TV.

   **Related capabilities:**

   -  ``TVControl.Channel.Down``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **setChannel**:(`ChannelInfo </apis/1-6-0/ios/ChannelInfo>`__ \*)\ *channelInfo* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sets the current channel to the channel provided by the ChannelInfo
   object provided.

   **Related capabilities:**

   -  ``TVControl.Channel.Set``

   **Parameters:**

   -  channelInfo – ChannelInfo object containing information about the desired
      channel

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getCurrentChannelWithSuccess**:(`CurrentChannelSuccessBlock <#currentchannelsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Gets the current channel info from the TV.

   **Related capabilities:**

   -  ``TVControl.Channel.Get``

   **Parameters:**

   -  success – Optional CurrentChannelSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (`ServiceSubscription </apis/1-6-0/ios/ServiceSubscription>`__ \*) **subscribeCurrentChannelWithSuccess**:(`CurrentChannelSuccessBlock <#currentchannelsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribes to any changes in the current channel. Each time the
   channel is changed, the new channel's info will be provided to the
   success callback.

   **Related capabilities:**

   -  ``TVControl.Channel.Subscribe``

   **Parameters:**

   -  success – Optional CurrentChannelSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getChannelListWithSuccess**:(`ChannelListSuccessBlock <#channellistsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Get a list of available channels from the TV.

   **Related capabilities:**

   -  ``TVControl.Channel.List``

   **Parameters:**

   -  success – Optional ChannelListSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getProgramInfoWithSuccess**:(`ProgramInfoSuccessBlock <#programinfosuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Gets the current program info from the TV.

   **Related capabilities:**

   -  ``TVControl.Program.Get``

   **Parameters:**

   -  success – Optional ProgramInfoSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (`ServiceSubscription </apis/1-6-0/ios/ServiceSubscription>`__ \*) **subscribeProgramInfoWithSuccess**:(`ProgramInfoSuccessBlock <#programinfosuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribes to any changes in the current program. Each time the
   channel is changed or a new program starts, the new program's info
   will be provided to the success callback.

   **Related capabilities:**

   -  ``TVControl.Program.Subscribe``

   **Parameters:**

   -  success – Optional ProgramInfoSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getProgramListWithSuccess**:(`ProgramListSuccessBlock <#programlistsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Gets a list of all programs scheduled to play on the current channel.

   **Related capabilities:**

   -  ``TVControl.Program.List``

   **Parameters:**

   -  success – Optional ProgramListSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (`ServiceSubscription </apis/1-6-0/ios/ServiceSubscription>`__ \*) **subscribeProgramListWithSuccess**:(`ProgramListSuccessBlock <#programlistsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribes to any changes in the current program. Each time the
   channel is changed or a new program starts, the new program's info
   will be provided to the success callback.

   **Related capabilities:**

   -  ``TVControl.Program.List.Subscribe``

   **Parameters:**

   -  success – Optional ProgramListSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **get3DEnabledWithSuccess**:(`TV3DEnabledSuccessBlock <#tv3denabledsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Gets the current 3D status of the TV.

   **Related capabilities:**

   -  ``TVControl.3D.Get``

   **Parameters:**

   -  success – Optional TV3DEnabledSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **set3DEnabled**:(BOOL)\ *enabled* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sets the current 3D status of the TV.

   **Related capabilities:**

   -  ``TVControl.3D.Set``

   **Parameters:**

   -  enabled – Whether the TV's 3D mode should be on or off

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (`ServiceSubscription </apis/1-6-0/ios/ServiceSubscription>`__ \*) **subscribe3DEnabledWithSuccess**:(`TV3DEnabledSuccessBlock <#tv3denabledsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribes to changes in the TV's 3D status.

   **Related capabilities:**

   -  ``TVControl.3D.Subscribe``

   **Parameters:**

   -  success – Optional TV3DEnabledSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

Typedefs
--------

CurrentChannelSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~

void(^)(`ChannelInfo </apis/1-6-0/ios/ChannelInfo>`__ \*channelInfo)

Success block that is called upon successfully getting the current
channel's information.

-  channelInfo

   Object containing information about the current channel

ChannelListSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~

void(^)(NSArray \*channelList)

Success block that is called upon successfully getting the channel list.

-  channelList

   Array containing a ChannelInfo object for each available channel on
   the TV

ProgramInfoSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~

void(^)(`ProgramInfo </apis/1-6-0/ios/ProgramInfo>`__ \*programInfo)

Success block that is called upon successfully getting the current
program's information.

-  programInfo

   Object containing information about the current program

ProgramListSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~

void(^)(NSArray \*programList)

Success block that is called upon successfully getting the program list
for the current channel.

-  programList

   Array containing a ProgramInfo object for each available program on
   the TV's current channel

TV3DEnabledSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~

void(^)(BOOL tv3DEnabled)

Success block that is called upon successfully getting the TV's 3D mode

-  tv3DEnabled

   Whether 3D mode is currently enabled on the TV
