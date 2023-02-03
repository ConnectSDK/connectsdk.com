Connect SDK 1.4 is out
======================

\|Vivek Sekar| Posted by Vivek Sekar \| December 3, 2014

We have just pushed out the code for the 1.4.0 release. Here is a quick
overview of the additions we have made:

**1.4.0 release notes**

* Modularization of Connect SDK
* Improved support for DLNA devices

   * DLNA volume control subscriptions
   * DLNA play state subscriptions
   * DLNA media info

* Unit tests for the discovery services providers
* Bug fixes in iOS, Android and Google Cast modules

:doc:`**Modularization** <../guide-ios/ios-modularization>`

With the growing adoption of Connect SDK, a frequently requested feature
has been for the developers to be able to pick and choose the various
devices they want to support in their applications. As they put it – it
would allow them to only have the necessary components as part of their
application - so apps that directly stream media content does not have
to worry about the web app support or vice versa.

With the 1.4.0 release we are taking our first steps towards achieving
modularization within the features offered by Connect SDK. The 1.4.0
release allows developers to be able to pick between

*  **full** (all you can eat version)
*  **lite** (Connect SDK without the Google Cast) versions of Connect
   SDK.

Going forward in the upcoming releases we will add more and more of the
existing features into this modularized approach. So you can pick and
choose the features, like DIAL, Google Cast, Roku, Apple TV, LG Smart
TV’s, DLNA.

**DLNA**

WIth over 18,000 device models supporting DLNA, we are putting our
efforts to be able to address these plethora of devices. With the 1.4.0
release we have further improved the support for DLNA devices. With this
release we have added Volume control, play state & media info
subscription. Along with some bug fixes to improve stability.

**Unit tests**

As Connect SDK grows to support more and more platforms and their SDK's,
We have started work towards having a better overview on the quality of
the code we are pushing out and integrating with. With the 1.4.0
release, we have started adding unit test coverage for the search
discovery providers. Going forward the work on the test coverage will
continue independent of the Connect SDK's release cycle, so that we can
catch up to all the work that has been put out till now.

Just like the previous releases, we look forward to your feedback. We
have already started working on Connect SDK v1.4.1 and look forward to
sharing it with you soon!
