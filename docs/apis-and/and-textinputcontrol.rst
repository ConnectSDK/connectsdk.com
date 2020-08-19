TextInputControl 
===================================================================
``com.connectsdk.service.capability.TextInputControl``

*extends CapabilityMethods*

The TextInputControl capability serves to define the methods required
for normalizing common text input commands (send text, enter, delete,
keyboard status).

Properties
----------

**final String Any = "TextInputControl.Any"**

**final String Send = "TextInputControl.Send"**

**final String Send_Enter = "TextInputControl.Enter"**

**final String Send_Delete = "TextInputControl.Delete"**

**final String Subscribe = "TextInputControl.Subscribe"**

**final String[] Capabilities = { Send, Send_Enter, Send_Delete, Subscribe }**

Inner Classes
-------------

* :doc:`TextInputStatusListener <and-textinputstatuslistener>`

Methods
-------

:doc:`TextInputControl <and-textinputcontrol>` **getTextInputControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getTextInputControlCapabilityLevel** ()

:doc:`ServiceSubscription <and-servicesubscription>` < :doc:`TextInputStatusListener <and-textinputstatuslistener>`> 
**subscribeTextInputStatus** ( :doc:`TextInputStatusListener <and-textinputstatuslistener>` *listener*)

    Subscribe to information about the current text field.

    **Related capabilities:**
        * ``TextInputControl.Subscribe``

    **Parameters:**
        * listener – (optional) TextInputStatusListener with methods to be called on success or failure

void **sendText** (String *input*)

    Send text to the current text field.

    **Related capabilities:**
        * ``TextInputControl.Send.Text``

    **Parameters:**
        * input

void **sendEnter** ()

    Send enter key to the current text field.

    **Related capabilities:**
        * ``TextInputControl.Send.Enter``

void **sendDelete** ()

    Send delete event to the current text field.

    **Related capabilities:**
        * ``TextInputControl.Send.Delete``
