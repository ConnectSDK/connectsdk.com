TextInputStatusInfo
===================

Normalized reference object for information about a text input event.

Properties
----------

UIKeyboardType keyboardType
   Type of keyboard that should be displayed to the user.

BOOL isVisible
   Whether the keyboard is/should be visible to the user.

id rawData
   Raw data from the first screen device about the text input status. In
   most cases, this is an NSDictionary.
