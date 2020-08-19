ToastControl
============

The ToastControl capability protocol serves to define the methods
required for displaying toast messages on the TV.

Toasts may optionally provide an 80x80 pixel icon in PNG or JPEG format,
encoded as base64. The icon will be displayed alongside the toast
message.

Methods
-------

\- (id<:doc:`ToastControl <ios-toastcontrol>`>) **toastControl**

\- (:doc:`CapabilityPriorityLevel <ios-capabilityprioritylevel>`) **toastControlPriority**

\- (void) **showToast**:(NSString \*)\ *message* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Show a toast on the TV.

   **Parameters:**

   -  message – Message to display

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **showToast**:(NSString \*)\ *message* **iconData**:(NSString \*)\ *iconData* **iconExtension**:(NSString \*)\ *iconExtension* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Show a toast on the TV.

   **Parameters:**

   -  message – Message to display

   -  **iconData**: iconData – Base-64 encoded JPEG or PNG data

   -  **iconExtension**: iconExtension – File extension of icon

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **showClickableToast**:(NSString \*)\ *message* **appInfo**:(:doc:`AppInfo <ios-appinfo>` \*)\ *appInfo* **params**:(NSDictionary \*)\ *params* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Show a toast on the TV and perform an action when the toast is
   clicked on the TV.

   **Related capabilities:**

   -  ``ToastControl.Show.Clickable.App``
   -  ``ToastControl.Show.Clickable.App.Params``
   -  ``ToastControl.Show.Clickable.URL``

   **Parameters:**

   -  message – Message to display

   -  **appInfo**: appInfo – AppInfo for app to launch on click of toast

   -  **params**: params – Launch params for app

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **showClickableToast**:(NSString \*)\ *message* **appInfo**:(:doc:`AppInfo <ios-appinfo>` \*)\ *appInfo* **params**:(NSDictionary \*)\ *params* **iconData**:(NSString \*)\ *iconData* **iconExtension**:(NSString \*)\ *iconExtension* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Show a toast on the TV and perform an action when the toast is
   clicked on the TV.

   **Related capabilities:**

   -  ``ToastControl.Show.Clickable.App``
   -  ``ToastControl.Show.Clickable.App.Params``
   -  ``ToastControl.Show.Clickable.URL``

   **Parameters:**

   -  message – Message to display

   -  **appInfo**: appInfo – AppInfo for app to launch on click of toast

   -  **params**: params – Launch params for app

   -  **iconData**: iconData – Base-64 encoded JPEG or PNG data

   -  **iconExtension**: iconExtension – File extension of icon

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **showClickableToast**:(NSString \*)\ *message* **URL**:(NSURL \*)\ *URL* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Show a toast on the TV and perform an action when the toast is
   clicked on the TV.

   **Related capabilities:**

   -  ``ToastControl.Show.Clickable.App``
   -  ``ToastControl.Show.Clickable.App.Params``
   -  ``ToastControl.Show.Clickable.URL``

   **Parameters:**

   -  message – Message to display

   -  **URL**: URL – URL to launch in browser

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure

\- (void) **showClickableToast**:(NSString \*)\ *message* **URL**:(NSURL \*)\ *URL* **iconData**:(NSString \*)\ *iconData* **iconExtension**:(NSString \*)\ *iconExtension* **success**:(SuccessBlock)\ *success* **failure**:(FailureBlock)\ *failure*
   Show a toast on the TV and perform an action when the toast is
   clicked on the TV.

   **Related capabilities:**

   -  ``ToastControl.Show.Clickable.App``
   -  ``ToastControl.Show.Clickable.App.Params``
   -  ``ToastControl.Show.Clickable.URL``

   **Parameters:**

   -  message – Message to display

   -  **URL**: URL – URL to launch in browser

   -  **iconData**: iconData – Base-64 encoded JPEG or PNG data

   -  **iconExtension**: iconExtension – File extension of icon

   -  **success**: success – Optional SuccessBlock to be called on success

   -  **failure**: failure – Optional FailureBlock to be called on failure
