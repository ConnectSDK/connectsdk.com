Overview
========

What are TV web apps?
---------------------

-  Most TV apps are web apps that are packaged to run on the TV. They
   are developed using standard web technologies.
-  TV web apps can be viewed on a TV without a browser, since they
   execute inside a web runtime environment.

Why TV web apps?
----------------

webOS TV, Chromecast, and Apple TV allow synchronized experience across
multiple devices through web sockets. This enables users to interact
with a TV web app using their mobile devices.

For example, if you created a TV chess board game app, users would not
only interact with the app on the TV, they would also be able to
interact with the app using their mobile devices.

Web app IDs
-----------

Mobile web apps require a web app id in order to launch on webOS TV and
Chromecast. This web app id is translated into the mobile web app's URL
when it is launched on the TV.

.. list-table::
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   :align: center

   * - Paltform
     - URL
   * - Web app id for webOS TV
     - `http://lgsvl.com/connectSDK/index.php <http://lgsvl.com/connectSDK/index.php>`_
   * - Web app id for Chromecast
     - `https://developers.google.com/cast/docs/registration <https://developers.google.com/cast/docs/registration>`_
   * - Apple TV
     - Apple TV does not require a web app id.

.. important::
   When designing your TV web app, be mindful of
   `Overscan <http://en.wikipedia.org/wiki/Overscan>`__. To avoid having
   parts of your web app cut off, we recommend not placing UI elements near
   the corner of the screen and always test your web apps to ensure they
   display properly on each targeted platform.

Interaction with TV web apps
----------------------------

All interactions with Chromecast and Apple TV web apps occur from a
mobile device or laptop since the device does not support external
remote controls. On other platforms such as webOS, the TV ships with
traditional and `Magic Remotes <http://webostv.developer.lge.com/design/webos-tv-system-ui/remote-control/>`__.
When designing your web app, make sure to design for the platforms you intend
to support. On Chromecast and Apple TV, avoid using UI elements that
make users think they are clickable. On webOS, make UI elements
clickable since users may use their Magic Remote to interact with your
web app.

Make sure to review all design guidelines for each platform you intend
to support.

Web runtimes on various TV platforms may not be the same
--------------------------------------------------------

While the HTML5 spec brings us one step closer to the "write once, run
everywhere" utopia, we still recommend that you test your web app on
each TV platform you intend to support.

-  Web rendering engines vary which may cause inconsistency across
   platforms. For example, webOS uses WebKit 2.0 and it is not
   officially documented what Chromecast and others use.
-  Hardware differences between dongles, set-top boxes, and Smart TVs
   can be significant - therefore, complex animations and computations
   should be reviewed.
-  Screen resolution can vary between platforms and devices. webOS Smart
   TVs run at 1080P (1920x1080) while Chromecast currently renders
   WebView in 720P (1280x720). Apple TV automatically adjusts to match
   the resolution of the connected TV.
-  Lastly, video and audio codec support can also cause fragmentation
   across multiple platforms.

Our experience has shown that using standard design patterns such as
responsive design and standard video formats (MP4) - there is little
variation between most platforms.
