MediaLaunchObject
=================

MediaLaunchObject is a container object which holds LaunchSession
object,MediaControl object/or and PlayListControl object

Properties
----------

id<:doc:`MediaControl <ios-mediacontrol>`> mediaControl
   MediaControl object of Media player

id<:doc:`PlayListControl <ios-playlistcontrol>`> playListControl
   PlayList Control Object of Media player

:doc:`LaunchSession <ios-launchsession>` \* session
   Launch Session object of Media player

Methods
-------

\- (instancetype) **initWithLaunchSession**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *session* **andMediaControl**:(id<`MediaControl </apis/1-6-0/ios/MediaControl>`__>)\ *mediaControl*
   Creates an instance of MediaLaunchObject with given property values.

   **Parameters:**

   -  session

   -  **andMediaControl**: mediaControl – MediaControl object used to control playback

\- (instancetype) **initWithLaunchSession**:(:doc:`LaunchSession <ios-launchsession>` \*)\ *session* **andMediaControl**:(id<`MediaControl </apis/1-6-0/ios/MediaControl>`__>)\ *mediaControl* **andPlayListControl**:(id<:doc:`PlayListControl <ios-playlistcontrol>`>)\ *playListControl*
   **Parameters:**

   -  session
   -  **andMediaControl**: mediaControl
   -  **andPlayListControl**: playListControl
