MediaControl
============

The MediaControl capability protocol serves to define the methods
required for normalizing the control of media playback (play, pause,
fast forward, etc) as well as obtaining media information (playhead
position, duration, etc).

Methods
-------

\- (id<:doc:`MediaControl <ios-mediacontrol>`>) **mediaControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **mediaControlPriority**

\- (void) **playWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Send play command.

   **Related capabilities:**

   -  ``MediaControl.Play``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **pauseWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Send pause command.

   **Related capabilities:**

   -  ``MediaControl.Pause``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **stopWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Send play command.

   **Related capabilities:**

   -  ``MediaControl.Stop``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **rewindWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Send rewind command.

   **Related capabilities:**

   -  ``MediaControl.Rewind``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **fastForwardWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Send play command.

   **Related capabilities:**

   -  ``MediaControl.FastForward``

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **seek**:(NSTimeInterval)\ *position* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Seeks to a new position within the current media item

   **Related capabilities:**

   -  ``MediaControl.Seek``

   **Parameters:**

   -  position

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getDurationWithSuccess**:(`MediaDurationSuccessBlock <#mediadurationsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  success – Optional MediaDurationSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getPositionWithSuccess**:(`MediaPositionSuccessBlock <#mediadurationsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  success – Optional MediaPositionSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getMediaMetaDataWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getPlayStateWithSuccess**:(`MediaPlayStateSuccessBlock <#mediaplaystatesuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  success – Optional MediaPlayStateSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (:doc:`ServiceSubscription <ios-servicesubscription>` \*) **subscribePlayStateWithSuccess**:(`MediaPlayStateSuccessBlock <#mediaplaystatesuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  success – Optional MediaPlayStateSuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (:doc:`ServiceSubscription <ios-servicesubscription>` \*) **subscribeMediaInfoWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

Typedefs
--------

MediaPlayStateSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~

void(^)(:doc:`MediaControlPlayState <ios-mediacontrolplaystate>`
playState)

Success block that is called upon any change in a media file's play
state.

-  playState

   Play state of the current media file

MediaPositionSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~~~

void(^)(NSTimeInterval position)

Success block that is called upon successfully getting the media file's
current playhead position.

-  position

   Current playhead position of the current media file, in seconds

MediaDurationSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~~~

void(^)(NSTimeInterval duration)

Success block that is called upon successfully getting the media file's
duration.

-  duration

   Duration of the current media file, in seconds
