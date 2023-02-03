Connect SDK Smart Home demo
===========================

\|Vivek Sekar| Posted by Vivek Sekar \| April 8, 2015

We have spent the last month working with some exciting Smart Home
products & technologies. Now we are ready to showcase our work.

We believe the Smart Homes of the future, are not going to be driven by
devices from a single manufacturer, instead a network of devices from
various manufacturers. And interoperability will be a key part of the
experience for these devices to be able to deliver on the promise of
simplifying the user's life.

We hope to use the understanding from this showcase, to be able to
deliver a solution for developers to be able to leverage the various
SDK's out there to provide novel and innovative application solutions
for the user.

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe src="https://www.youtube.com/embed/s2E5ck1J5vM" frameborder="0" width="100%" height="480"></iframe>
    </div>

We have made the Smart Home sampler app source code available in github.

This demo app demonstrates a scenario of using various Smart Home
devices in two home scenes. They represent a living room and a family
room, each containing a media device, light bulbs, and possibly other
devices. The supported devices come from different categories (media
players, light bulbs, switches, and iBeacons) and multiple
manufacturers.

The scenario of the app is:

#. You enter the living room, which is detected by an iBeacon,
#. A playlist starts to play on a TV or speaker, and the light bulbs
   change color to match one of the colors of the album art during
   playback.
#. Then the user moves from the living room scene to the family room
   scene.
#. Where the session information is transfered from the living room to
   the family room.

   -  The devices in the living switch off and the session is picked up
      in the family room

#. The user put the scene to sleep using voice command (to replicate
   control using Siri or Google Now or other voice engine/assitants)

   -  The speaker fades out the music, while the LED bulb fade out and
      switch off.

#. The Scene wakes up after a defined time - to mimic waking up from an
   alarm.

   -  The Led Bulbs switch on along with speaker.

| For the source code & additional information
| - https://github.com/ConnectSDK/SmartHomeSamplerAndroid
| - https://github.com/ConnectSDK/SmartHomeSampleriOS

Support our work by providing your valuable :doc:`feedback to
us <../contact>`.
