ScreenMirroringControl
=============

The ScreenMirroringControl capability protocol serves to define the methods required for displaying
the mobile app screen to LG TV.

Methods
-------

\- (id<:doc:`ScreenMirroringControl <ios-screenmirroringcontrol>`>) **ScreenMirroringControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **screenMirroringControlPriority**

\- (void) **startScreenMirroring**
   Requests to start the screen mirroring

\- (void) **startScreenMirroringWithSettings**:(nullable NSDictionary<NSString *, id> *) *settings*
   Requests to start the screen mirroring after setting up.

   **Parameters:**

   -  settings – screen mirroring settings

\- (void) **pushSampleBuffer**:(CMSampleBufferRef)\ *sampleBuffer* **with**:(RPSampleBufferType)\ *sampleBufferType*
   Delivers video/audio data captured by Upload Extension to screen mirroring.

   **Parameters:**

   -  sampleBuffer – A reference to an immutable sample buffer object

   -  **with**: sampleBufferType – The type of sample buffered

\- (void) **stopScreenMirroring**
   Requests to stop the screen mirroring

\- (void) **setScreenMirroringDelegate**:(__weak id<ScreenMirroringControlDelegate>)\ *delegate*
   Registers a delegate to receive events while running the screen mirroring.

   **Parameters:**

   -  delegate
