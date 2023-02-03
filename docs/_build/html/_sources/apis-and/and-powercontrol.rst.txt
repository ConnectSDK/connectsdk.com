PowerControl
===========================================================
``com.connectsdk.service.capability.PowerControl``

*extends CapabilityMethods*

The PowerControl capability protocol serves to define the methods 
required for normalizing power off functionality.

Properties
----------

final String Any = "PowerControl.Any"

final String Off = "PowerControl.Off"

final String On = "PowerControl.On"

final String[] Capabilities = { Off, On }

Methods
-------

:doc:`PowerControl <and-powercontrol>` **getPowerControl** ()


:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPowerControlCapabilityLevel** ()


void **powerOff** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Sends a power off signal to the TV. A success message will, internally, trigger a disconnection with the device.

     **Related capabilities:**

     * ``PowerControl.Off``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **powerOn** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure
