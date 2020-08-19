ToastControl
============

The ToastControl capability protocol serves to define the methods
required for displaying toast messages on the TV.

Toasts may optionally provide an 80x80 pixel icon in PNG or JPEG format,
encoded as base64. The icon will be displayed alongside the toast
message.

Methods
-------

toastControl.\ **showToast** (*message*, [*options*])
   Show a toast on the TV.

   **Parameters:**

   -  message (string) – Message to display

      Message to display

   -  options (object) [optional] –

      -  iconData (string): base64-encoded image
      -  iconExtension (string): file extension of icon (.png or .jpg)

   **Returns:** :doc:`Command <cor-command>`

toastControl.\ **showClickableToast** (*message*, *options*)
   Show a toast on the TV and perform an action when the toast is
   clicked on the TV.

   **Related capabilities:**

   -  ``ToastControl.Show.Clickable.App``
   -  ``ToastControl.Show.Clickable.App.Params``
   -  ``ToastControl.Show.Clickable.URL``

   **Parameters:**

   -  message (string) – Message to display

      Message to display

   -  options (object) –

      -  iconData (string): base64-encoded image
      -  iconExtension (string): file extension of icon (.png or .jpg)
      -  appId (string): app to launch when clicked OR
      -  url (string): url to launch in browser when clicked

   **Returns:** :doc:`Command <cor-command>`
