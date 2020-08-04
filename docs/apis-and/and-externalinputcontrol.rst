ExternalInputControl com.connectsdk.service.capability.ExternalInputControl
===========================================================================

*extends CapabilityMethods*

The ExternalInputControl capability serves to define the methods
required for normalizing all functions regarding external input
switching and general info.

Properties
----------

final String Any = "ExternalInputControl.Any"
final String Picker_Launch = "ExternalInputControl.Picker.Launch"
final String Picker_Close = "ExternalInputControl.Picker.Close"
final String List = "ExternalInputControl.List"
final String Set = "ExternalInputControl.Set"
final String[] Capabilities = { Picker_Launch, Picker_Close, List, Set }

Inner Classes
-------------

-  `ExternalInputListListener </apis/1-6-0/android/ExternalInputListListener>`__

Methods
-------

`ExternalInputControl </apis/1-6-0/android/ExternalInputControl>`__ **getExternalInput** ()

`CapabilityPriorityLevel </apis/1-6-0/android/CapabilityPriorityLevel>`__ **getExternalInputControlPriorityLevel** ()

void **launchInputPicker** (`AppLaunchListener </apis/1-6-0/android/AppLaunchListener>`__ *listener*)
   Launches the visual input picker on the device. This may be helpful
   for situations where the device does not support directly
   listing/modifying the external inputs.

   .. rubric:: Related capabilities:
      :name: related-capabilities
      :class: method-detail-label

   -  ``ExternalInputControl.Picker.Launch``

   .. rubric:: Parameters:
      :name: parameters
      :class: method-detail-label

   -  listener –

      (optional) AppLaunchListener with methods to be called on success
      or failure

void **closeInputPicker** (`LaunchSession </apis/1-6-0/android/LaunchSession>`__ *launchSessionm*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Closes the input picker on the device, if it is currently open.

   .. rubric:: Related capabilities:
      :name: related-capabilities-1
      :class: method-detail-label

   -  ``ExternalInputControl.Picker.Close``

   .. rubric:: Parameters:
      :name: parameters-1
      :class: method-detail-label

   -  launchSessionm

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure

void **getExternalInputList** (`ExternalInputListListener </apis/1-6-0/android/ExternalInputListListener>`__ *listener*)
   Get a list of input devices (HDMI, AV, etc) connected to the device

   .. rubric:: Related capabilities:
      :name: related-capabilities-2
      :class: method-detail-label

   -  ``ExternalInputControl.List``

   .. rubric:: Parameters:
      :name: parameters-2
      :class: method-detail-label

   -  listener –

      (optional) ExternalInputListListener with methods to be called on
      success or failure

void **setExternalInput** (`ExternalInputInfo </apis/1-6-0/android/ExternalInputInfo>`__ *input*, `ResponseListener </apis/1-6-0/android/ResponseListener>`__\ <Object> *listener*)
   Switch to the specified external input

   .. rubric:: Related capabilities:
      :name: related-capabilities-3
      :class: method-detail-label

   -  ``ExternalInputControl.Set``

   .. rubric:: Parameters:
      :name: parameters-3
      :class: method-detail-label

   -  input

   -  listener –

      (optional) ResponseListener< Object > with methods to be called on
      success or failure
