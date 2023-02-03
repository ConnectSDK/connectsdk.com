ExternalInputControl
====================

The ExternalInputControl capability serves to define the methods required for normalizing all functions regarding external input switching and general info.

Methods
-------

\- (id<:doc:`ExternalInputControl <ios-externalinputcontrol>`>) **externalInputControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **externalInputControlPriority**

\- (void) **launchInputPickerWithSuccess**:(AppLaunchSuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Launches the visual input picker on the device. This may be helpful
   for situations where the device does not support directly
   listing/modifying the external inputs.

   **Related capabilities:**

   * ``ExternalInputControl.Picker.Launch``

   **Parameters:**

   * success – Optional AppLaunchSuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **closeInputPicker**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *launchSession* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Closes the input picker on the device, if it is currently open.

   **Related capabilities:**

   * ``ExternalInputControl.Picker.Close``

   **Parameters:**

   * launchSession – LaunchSession from the ExternalInputListSuccessBlock
   * **success**: success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **getExternalInputListWithSuccess**:(`ExternalInputListSuccessBlock <#externalinputlistsuccessblock>`__)\ *success* **failure**:(FailureBlock)\ *failure*
   Get a list of input devices (HDMI, AV, etc) connected to the device

   **Related capabilities:**

   * ``ExternalInputControl.List``

   **Parameters:**

   * success – Optional ExternalInputListSuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **setExternalInput**:(:doc:`ExternalInputInfo <ios-externalinputinfo>` \*)\ *externalInputInfo* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Switch to the specified external input

   **Related capabilities:**

   * ``ExternalInputControl.Set``

   **Parameters:**

   * externalInputInfo – Object containing the proper info to set current input. For best cross-platform support, it is suggested to get ExternalInputInfo references from getExternalInputList, if possible.
   * **success**: success – Optional SuccessBlock to be called on success
   * **failure**: failure – Optional FailureBlock to be called on failure

Typedefs
--------

ExternalInputListSuccessBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

void(^)(NSArray \*externalInputList)

Success block that is called upon successfully getting the external
input list.

* externalInputList

   Array containing an ExternalInputInfo object for each available
   external input on the device
