RemoteCameraControl
=============

The RemoteCameraControl capability protocol serves to define the methods required for using
the mobile camera for the LG TV.

Methods
-------

\- (id<:doc:`RemoteCameraControl <ios-remotecameracontrol>`>) **remoteCameraControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **remoteCameraControlPriority**

\- (UIView \*) **startRemoteCamera**
   Requests to start the remote camera.

   - Default Camera Settings: Front

   - Default Sound Settings: With Sound

   **Returns:**

   - UIView - Returns an object for the UIView created to show the camera preview.

\- (UIView \*) **startRemoteCameraWithSettings**:(nullable NSDictionary<NSString \*, id> \*) *settings*
   Requests to start the remote camera after setting up the camera.

   - kRemoteCameraSettingsMicMute: Mute setting

   - kRemoteCameraSettingsLensFacing: Front/rear camera settings

   **Parameters:**

   -  settings – Camera settings

   **Returns:**

   - UIView - Returns an object for the UIView created to show the camera preview.

\- (void) **stopRemoteCamera**
   Requests to stop the remote camera

\- (void) **setLensFacing**:(int)\ *lensFacing*
   Sets the front/rear camera lens use.

   - Front camera settings: RemoteCameraLensFacingFront (Default)

   - Rear camera settings: RemoteCameraLensFacingBack

   **Parameters:**

   -  lensFacing – Camera lens direction

\- (void) **setMicMute**:(BOOL)\ *micMute*
   Sets the mute function of the microphone. (Default: NO)

   **Parameters:**

   -  micMute – Microphone mute settings

\- (void) **setRemoteCameraDelegate**:(__weak id<RemoteCameraControlDelegate>)\ *delegate*
   Registers a delegate to receive events while running the remote camera.

   **Parameters:**

   -  delegate
