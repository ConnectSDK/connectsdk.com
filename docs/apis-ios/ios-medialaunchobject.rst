MediaLaunchObject
=================

MediaLaunchObject is a container object which holds LaunchSession
object,MediaControl object/or and PlayListControl object

Properties
----------

id<`MediaControl </apis/1-6-0/ios/MediaControl>`__> mediaControl
   MediaControl object of Media player

id<`PlayListControl </apis/1-6-0/ios/PlayListControl>`__> playListControl
   PlayList Control Object of Media player

`LaunchSession </apis/1-6-0/ios/LaunchSession>`__ \* session
   Launch Session object of Media player

Methods
-------

\- (instancetype) **initWithLaunchSession**:(`LaunchSession </apis/1-6-0/ios/LaunchSession>`__ \*)\ *session* **andMediaControl**:(id<`MediaControl </apis/1-6-0/ios/MediaControl>`__>)\ *mediaControl*
   Creates an instance of MediaLaunchObject with given property values.

   **Parameters:**

   -  session

   -  **andMediaControl**: mediaControl – MediaControl object used to control playback

\- (instancetype) **initWithLaunchSession**:(`LaunchSession </apis/1-6-0/ios/LaunchSession>`__ \*)\ *session* **andMediaControl**:(id<`MediaControl </apis/1-6-0/ios/MediaControl>`__>)\ *mediaControl* **andPlayListControl**:(id<`PlayListControl </apis/1-6-0/ios/PlayListControl>`__>)\ *playListControl*
   **Parameters:**

   -  session
   -  **andMediaControl**: mediaControl
   -  **andPlayListControl**: playListControl
