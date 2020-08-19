PlayListControl
===============

Methods
-------

\- (id<`PlayListControl </apis/1-6-0/ios/PlayListControl>`__>) **playListControl**

\- (`CapabilityPriorityLevel </apis/1-6-0/ios/CapabilityPriorityLevel>`__) **playListControlPriority**

\- (void) **playNextWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Plays the next track in the playlist

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **playPreviousWithSuccess**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Plays the previous track in the playlist

   **Parameters:**

   -  success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **jumpToTrackWithIndex**:(NSInteger)\ *index* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Jumps to track in the playlist

   **Parameters:**

   -  index – NSInteger a zero based index parameter.

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure
