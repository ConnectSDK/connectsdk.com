VolumeControl
=============

The VolumeControl capability protocol serves to define the methods
required for normalizing common volume specific commands (volume
up/down, mute, etc).

Methods
-------

\- (id<:doc:`VolumeControl <ios-volumecontrol>`>) **volumeControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **volumeControlPriority**

\- (void) **volumeUpWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends the volume up command to the device.

   **Related capabilities:**

   -  ``VolumeControl.UpDown``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **volumeDownWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Sends the volume down command to the device.

   **Related capabilities:**

   -  ``VolumeControl.UpDown``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getVolumeWithSuccess**:(`VolumeSuccessBlock <#volumesuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Get the current volume of the device.

   **Related capabilities:**

   -  ``VolumeControl.Get``

   **Parameters:**

   -  success – Optional VolumeSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **setVolume**:(float)\ *volume* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Set the volume of the device.

   **Related capabilities:**

   -  ``VolumeControl.Set``

   **Parameters:**

   -  volume – Volume as a float between 0.0 and 1.0

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (:doc:`ServiceSubscription <ios-servicesubscription>` \*) **subscribeVolumeWithSuccess**:(`VolumeSuccessBlock <#volumesuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribe to the volume on the TV.

   **Related capabilities:**

   -  ``VolumeControl.Subscribe``

   **Parameters:**

   -  success – Optional VolumeSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getMuteWithSuccess**:(`MuteSuccessBlock <#mutesuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Get the current mute state.

   **Related capabilities:**

   -  ``VolumeControl.Mute.Get``

   **Parameters:**

   -  success – Optional MuteSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **setMute**:(BOOL)\ *mute* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Set the current volume.

   **Related capabilities:**

   -  ``VolumeControl.Mute.Set``

   **Parameters:**

   -  mute

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (:doc:`ServiceSubscription <ios-servicesubscription>` \*) **subscribeMuteWithSuccess**:(`MuteSuccessBlock <#mutesuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Subscribe to the mute state on the TV.

   **Related capabilities:**

   -  ``VolumeControl.Mute.Subscribe``

   **Parameters:**

   -  success – Optional MuteSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

Typedefs
--------

VolumeSuccessBlock
~~~~~~~~~~~~~~~~~~

void(^)(float volume)

Success block that is called upon successfully getting the device's
system volume.

-  volume

   Current system volume, value is a float between 0.0 and 1.0

MuteSuccessBlock
~~~~~~~~~~~~~~~~

void(^)(BOOL mute)

Success block that is called upon successfully getting the device's
system mute status.

-  mute

   Current system mute status
