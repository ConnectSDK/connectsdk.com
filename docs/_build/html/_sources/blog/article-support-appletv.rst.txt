Connect SDK now supports Apple TV
=================================

\|Henry Levak| Posted by Henry Levak \| June 10, 2014

All of the devices we use should work harmoniously together - and in
some cases they do. Take for example when you receive an email, you have
the ability to read it on your mobile phone, tablet, or PC. Similarly,
when you begin a Netflix movie on your desktop, you can finish watching
it on your tablet and many other devices. Consumers are beginning to
expect this connected experience between some of their devices - but few
expect it from the biggest screen in their house. Being able start
something on one device and continue it on the big screen is not as
widely supported as it should be - and we want to play a part in
changing that.

While many app developers acknowledge the opportunity a big, high
definition display can bring (other than a few Chromecast-enabled apps)
very few have implemented any app-to-TV functionality, and we don't
blame them. The reality is, there are too many second screen protocols
to choose from and the level of effort to integrate can be very high.
Not to mention, the market share of each protocol individually makes it
difficulty to prioritize it over other opportunities.

We saw these roadblocks for app developers as a huge opportunity and so
we designed and built Connect SDK. Our goal was simple, we wanted to
expand the reach of second screen development by tackling the ever
growing array of second screen protocols. Our result being, a single SDK
with integrated support for multiple protocols, in which the effort of
dealing with each one is abstracted away and the size of the opportunity
is an aggregation of multiple platforms.

It wasn't too long ago in April 2014 that we launched Connect SDK with
support for five TV platforms. Today we are excited to announce that
Connect SDK supports Apple TV with the release of version 1.3.

What does this mean?

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe src="https://www.youtube.com/embed/fZ6hFpZDmec" frameborder="0" width="100%" height="480"></iframe>
    </div>

For the **Android app developer**, you can now beam photos, videos, and
audio files to Apple TVs. By using an undocumented protocol, Connect SDK
lets Android developers discover, connect to, and control Apple TVs,
much like webOS and Roku devices (for a full list of supported features,
see :doc:`Supported Features <../fundamentals/supported-feature>`).
And, because Connect SDK abstracts all protocols, beaming a photo to an
Apple TV is just as easy as beaming it to a Chromecast or LG Smart TV '13.

For the **iOS developer**, you can choose between two modes, "Mirrored"
and "Media".

-  In **Mirrored mode**, web app beaming is accomplished by using
   AirPlay to mirror a secondary display that is actually being rendered
   on the iOS device. This allows developers to build full screen
   TV-optimzed web applications that work across webOS, Chromecast, and
   now Apple TV. In order to use this mode, the user will need to enable
   AirPlay mirroring in the Control Center. Also, as with any Airplay
   mirroring app - TV experience will end if the user switches away from
   your app.
-  In **Media mode**, photos, videos, and audio is beamed directly to an
   Apple TV. Using this mode provides the most seamless user experience,
   but before using it, please review Apple's developer guidelines as it
   is enabled by an undocumented protocol. While all protocols are
   subject to change with software updates, undocumented protocols may
   be particularly so.

As with any release, we look forward to your feedback. We have already
started working on Connect SDK v1.4 and look forward to sharing it with
you soon!
