ToastControl 
===========================================================
com.connectsdk.service.capability.ToastControl

*extends CapabilityMethods*

The ToastControl capability protocol serves to define the methods
required for displaying toast messages on the TV.

Toasts may optionally provide an 80x80 pixel icon in PNG or JPEG format,
encoded as base64. The icon will be displayed alongside the toast
message.

Properties
----------

**final String Any = "ToastControl.Any"**

**final String Show_Toast = "ToastControl.Show"**

**final String Show_Clickable_Toast_App = "ToastControl.Show.Clickable.App"**

**final String Show_Clickable_Toast_App_Params = "ToastControl.Show.Clickable.App.Params"**

**final String Show_Clickable_Toast_URL = "ToastControl.Show.Clickable.URL"**

**final String[] Capabilities = { Show_Toast, Show_Clickable_Toast_App, Show_Clickable_Toast_App_Params, Show_Clickable_Toast_URL }**

Methods
-------

:doc:`ToastControl <and-toastcontrol>` **getToastControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getToastControlCapabilityLevel** ()

void **showToast** (String *message*, :doc:`ResponseListener <and-responselistener>`\ <Object> *listener*)

    Show a toast on the TV.

    **Parameters:**
        * message – Message to display
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showToast** (String *message*, String *iconData*, String *iconExtension*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Show a toast on the TV.

    **Parameters:**
        * message – Message to display
        * iconData – Base-64 encoded JPEG or PNG data
        * iconExtension – File extension of icon
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForApp** (String *message*, :doc:`AppInfo <and-appinfo>` *appInfo*, JSONObject *params*, 
:doc:`ResponseListener <and-responselistener>` <Object> *listener*)

    Show a toast on the TV and perform an action when the toast is clicked on the TV.

    **Related capabilities:**
        * ``ToastControl.Show.Clickable.App``
        * ``ToastControl.Show.Clickable.App.Params``

    **Parameters:**
        * message – Message to display
        * appInfo – AppInfo for app to launch on click of toast
        * params – Launch params for app
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForApp** (String *message*, :doc:`AppInfo <and-appinfo>` *appInfo*, JSONObject *params*, String *iconData*, 
String *iconExtension*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Show a toast on the TV and perform an action when the toast is clicked on the TV.

    **Related capabilities:**
        * ``ToastControl.Show.Clickable.App``
        * ``ToastControl.Show.Clickable.App.Params``

    **Parameters:**
        * message – Message to display
        * appInfo – AppInfo for app to launch on click of toast
        * params – Launch params for app
        * iconData – Base-64 encoded JPEG or PNG data
        * iconExtension – File extension of icon
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForURL** (String *message*, String *url*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Show a toast on the TV and perform an action when the toast is clicked on the TV.

    **Related capabilities:**
        * ``ToastControl.Show.Clickable.URL``

    **Parameters:**
        * message – Message to display
        * url
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **showClickableToastForURL** (String *message*, String *url*, String *iconData*, String *iconExtension*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Show a toast on the TV and perform an action when the toast is clicked on the TV.

    **Related capabilities:**
        * ``ToastControl.Show.Clickable.URL``

    **Parameters:**
        * message – Message to display
        * url
        * iconData – Base-64 encoded JPEG or PNG data
        * iconExtension – File extension of icon
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure
