Testing & Debugging
=====================
Due to the abstracted nature of Connect SDK, it may not be necessary for you to
have a suite of test devices. For many use cases, testing on one supported
platform can be sufficient.

However, depending on your application and use case, it may be advisable to test
each platform before you release your application. For example, while video
beaming is abstracted, each platform supports different video protocols and you
should make sure that your specific app's video content is playable on your
desired platform.

webOS
-------
The webOS TV emulator is currently available through the LG developer portal,
`download here`_.

.. _download here: http://webostv.developer.lge.com/sdk/installation/

The emulator is limited in that it cannot download/install apps from LG Store.
This will limit your testing on the emulator to web app & media support.
NOTE: The Emulator's network setting has to be set  to "Bridged Adapter" mode
for the Emulator to be discoverable.

If you have need of production hardware, the line of 2014 LG Smart TVs with
webOS are currently available from major electronic retailers. Loaner devices
are made available to select partners — contact
`partners@connectsdk.com <partners@connectsdk.com>`_ for more information.

Chromecast
------------
To test your application with a Chromecast device, you need to purchase a
Chromecast dongle.

2012 and 2013 LG Smart TVs
----------------------------
To test your application with LG 2012 and 2013 Smart TVs, we recommend you
purchase the targeted device. The emulators available `here`_ are meant to
be used exclusively for first-screen TV App development.

.. _here: http://webostv.developer.lge.com/discover/netcast/sdk/

Roku
-----
In order to test your application, you should purchase a Roku device.
In general, Roku devices have the same features across all models,
however Roku 3 and Roku Streaming Stick have a larger app catalog, including
support for YouTube videos.

Fire TV
--------
To test your application with Fire TV, you should purchase a Fire TV device.

Apple TV
----------
To test your application with Apple TV, you should purchase an Apple TV device.
