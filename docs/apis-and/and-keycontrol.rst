KeyControl 
=======================================================
``com.connectsdk.service.capability.KeyControl``

*extends CapabilityMethods*

The KeyControl capability serves to define the methods required for
normalizing common key commands (up, down, left right, ok, back, home, key code).

Properties
----------

final String Any = "KeyControl.Any"

final String Up = "KeyControl.Up"

final String Down = "KeyControl.Down"

final String Left = "KeyControl.Left"

final String Right = "KeyControl.Right"

final String OK = "KeyControl.OK"

final String Back = "KeyControl.Back"

final String Home = "KeyControl.Home"

final String Send_Key = "KeyControl.SendKey"

final String KeyCode = "KeyControl.KeyCode"

final String[] Capabilities = { Up, Down, Left, Right, OK, Back, Home,**

Inner Classes
-------------

* :doc:`KeyCode <and-keycode>`

Methods
-------

:doc:`KeyControl <and-keycontrol>` **getKeyControl** ()


:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getKeyControlCapabilityLevel** ()


void **up** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Sends the up button key code to the TV.

     **Related capabilities:**

     * ``KeyControl.Up``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **down** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Sends the down button key code to the TV.

     **Related capabilities:**
   
     * ``KeyControl.Down``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **left** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Sends the left button key code to the TV.

     **Related capabilities:**

     * ``KeyControl.Left``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **right** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Sends the right button key code to the TV.

     **Related capabilities:**

     * ``KeyControl.Right``

     **Parameters:**
      
     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **ok** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Sends the OK button key code to the TV.

     **Related capabilities:**
     
     * ``KeyControl.OK``

     **Parameters:**
      
     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **back** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Sends the back button key code to the TV.

     **Related capabilities:**

     * ``KeyControl.Back``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **home** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Sends the home button key code to the TV.

     **Related capabilities:**

     * ``KeyControl.Home``

     **Parameters:**

     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **sendKeyCode** (:doc:`KeyCode <and-keycode>` *keycode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
     Sends a key code value to the TV.

     **Related capabilities:**

     * ``KeyControl.Send.KeyCode``

     **Parameters:**

     * keycode
     * listener – (optional) ResponseListener< Object > with methods to be called on success or failure
