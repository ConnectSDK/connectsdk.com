ExternalInputControl
====================
``com.connectsdk.service.capability.ExternalInputControl``

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

-  :doc:`ExternalInputListListener <and-externalinputlistlistener>`

Methods
-------

:doc:`ExternalInputControl <and-externalinputcontrol>` **getExternalInput** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getExternalInputControlPriorityLevel** ()

void **launchInputPicker** (:doc:`AppLaunchListener <and-applaunchlistener>` *listener*)
    Launches the visual input picker on the device. This may be helpful
    for situations where the device does not support directly
    listing/modifying the external inputs.

    **Related capabilities:**

    -  ``ExternalInputControl.Picker.Launch``

    **Parameters:**

    -  listener – (optional) AppLaunchListener with methods to be called on success or failure

void **closeInputPicker** (:doc:`LaunchSession <and-launchsession>` *launchSessionm*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Closes the input picker on the device, if it is currently open.

    **Related capabilities:**

    -  ``ExternalInputControl.Picker.Close``

    **Parameters:**

    -  launchSessionm
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getExternalInputList** (:doc:`ExternalInputListListener <and-externalinputlistlistener>` *listener*)
    Get a list of input devices (HDMI, AV, etc) connected to the device

    **Related capabilities:**

    -  ``ExternalInputControl.List``

    **Parameters:**

    -  listener – (optional) ExternalInputListListener with methods to be called on success or failure

void **setExternalInput** (:doc:`ExternalInputInfo <and-externalinputinfo>` *input*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
    Switch to the specified external input

    **Related capabilities:**

    -  ``ExternalInputControl.Set``

    **Parameters:**

    -  input
    -  listener – (optional) ResponseListener< Object > with methods to be called on success or failure