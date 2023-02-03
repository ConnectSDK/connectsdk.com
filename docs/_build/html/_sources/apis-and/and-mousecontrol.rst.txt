MouseControl
===========================================================
``com.connectsdk.service.capability.MouseControl``

*extends CapabilityMethods*

The MouseControl capability serves to define the methods required for
normalizing a mouse/trackpad (move/scroll with relative coordinates and click).

Properties
----------

final String Any = "MouseControl.Any"

final String Connect = "MouseControl.Connect"

final String Disconnect = "MouseControl.Disconnect"

final String Click = "MouseControl.Click"

final String Move = "MouseControl.Move"

final String Scroll = "MouseControl.Scroll"

final String[] Capabilities = { Connect, Disconnect, Click, Move, Scroll }

Methods
-------

:doc:`MouseControl <and-mousecontrol>` **getMouseControl** ()


:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMouseControlCapabilityLevel** ()


void **connectMouse** ()
     Establish a connection with the DeviceService's mouse communication medium (WebSocket, HTTP, etc). 
     While this step may not be necessary with certain platforms, it is suggested to call it anyways, 
     for purposes of seamless normalization. Calling connect on a non-connectable protocol will just trigger 
     the success callback immediately.

     **Related capabilities:**

     * ``MouseControl.Connect``

void **disconnectMouse** ()
     Disconnects from the mouse communication medium.

     **Related capabilities:**

     * ``MouseControl.Disconnect``

void **click** ()
     Perform a click action at the current mouse position.

     **Related capabilities:**

     * ``MouseControl.Click``

void **move** (double *dx*, double *dy*)
     Move the mouse by the given distance values.

     **Related capabilities:**

     * ``MouseControl.Move``

     **Parameters:**

     * dx – Distance to move the mouse on the x-axis relative to its current position
     * dy – Distance to move the mouse on the y-axis relative to its current position

void **move** (PointF *distance*)
     Move the mouse by the given distance values.

     **Related capabilities:**

     * ``MouseControl.Move``

     **Parameters:**

     * distance – Distance to move the mouse relative to its current position

void **scroll** (double *dx*, double *dy*)
     Scroll by the given distance values.

     **Related capabilities:**

     * ``MouseControl.Scroll``

     **Parameters:**

     * dx – Distance to scroll the mouse on the x-axis relative to its current position
     * dy – Distance to scroll the mouse on the y-axis relative to its current position

void **scroll** (PointF *distance*)
     Scroll by the given distance values.

     **Related capabilities:**

     * ``MouseControl.Scroll``

     **Parameters:**

     * distance – Distance to scroll relative to current position
