ExternalInputInfo
=================

Normalized reference object for information about a DeviceService's
external inputs. This object is required to set a DeviceService's
external input.

Properties
----------

NSString \* id
   ID of the external input on the first screen device.

NSString \* name
   User-friendly name of the external input (ex. AV, HDMI1, etc).

BOOL connected
   Whether the DeviceService is currently connected to this external
   input.

NSURL \* iconURL
   URL to an icon representing this external input.

id rawData
   Raw data from the first screen device about the external input. In
   most cases, this is an NSDictionary.

Methods
-------

\- (BOOL) **isEqual**:(:doc:`ExternalInputInfo <ios-externalinputinfo>` \*)\ *externalInputInfo*
   Compares two ExternalInputInfo objects.

   **Parameters:**

   * externalInputInfo – ExternalInputInfo object to compare.

   **Returns:** YES if both ExternalInputInfo id & name values are equal
