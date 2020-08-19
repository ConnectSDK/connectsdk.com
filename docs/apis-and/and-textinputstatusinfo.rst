TextInputStatusInfo 
===========================================================
``com.connectsdk.core.TextInputStatusInfo``

Normalized reference object for information about a text input event.

Methods
-------

**TextInputStatusInfo** ()

boolean **isFocused** ()

void **setFocused** (boolean *focused*)

    **Parameters:**
        * focused

TextInputType **getTextInputType** ()
    
    Gets the type of keyboard that should be displayed to the user.

void **setTextInputType** (TextInputType *textInputType*)
    
    Sets the type of keyboard that should be displayed to the user.

    **Parameters:**
        * textInputType

void **setContentType** (String *contentType*)

    **Parameters:**
        * contentType

boolean **isPredictionEnabled** ()

void **setPredictionEnabled** (boolean *predictionEnabled*)

    **Parameters:**
        * predictionEnabled

boolean **isCorrectionEnabled** ()

void **setCorrectionEnabled** (boolean *correctionEnabled*)

    **Parameters:**
        * correctionEnabled

boolean **isAutoCapitalization** ()

void **setAutoCapitalization** (boolean *autoCapitalization*)

    **Parameters:**
        * autoCapitalization

boolean **isHiddenText** ()

void **setHiddenText** (boolean *hiddenText*)

    **Parameters:**
        * hiddenText

JSONObject **getRawData** ()
    
    Gets the raw data from the first screen device about the text input status.

void **setRawData** (JSONObject *data*)
    
    Sets the raw data from the first screen device about the text input status.

    **Parameters:**
        * data

boolean **isFocusChanged** ()

void **setFocusChanged** (boolean *focusChanged*)

    **Parameters:**
        * focusChanged
