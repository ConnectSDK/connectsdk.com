WebAppSession 
===========================================================
``com.connectsdk.service.sessions.WebAppSession``

Overview When a web app is launched on a first screen device, there are
-----------------------------------------------------------------------

certain tasks that can be performed with that web app. WebAppSession
serves as a second screen reference of the web app that was launched. It
behaves similarly to LaunchSession, but is not nearly as static.

In Depth On top of maintaining session information (contained in the
--------------------------------------------------------------------

launchSession property), WebAppSession provides access to a number of
capabilities. - MediaPlayer - MediaControl - Bi-directional
communication with web app

MediaPlayer and MediaControl are provided to allow for the most common
first screen use cases a media player (audio, video, & images).

The Connect SDK JavaScript Bridge has been produced to provide
normalized support for these capabilities across protocols (Chromecast,
webOS, etc).

Properties
----------

:doc:`LaunchSession <and-launchsession>` launchSession
    LaunchSession object containing key session information. Much of this
    information is required for web app messaging & closing the web app.

Inner Classes
-------------

    * `LaunchListener <and-webappsession-launchlistener>`
    * `StatusListener <and-statuslistener>`
    * `WebAppPinStatusListener <and-webapppinstatuslistener>`
    * `WebAppStatus <and-webappstatus>`

Methods
-------


**WebAppSession** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`DeviceService <and-deviceservice>` *service*)
   
    Instantiates a WebAppSession object with all the information
    necessary to interact with a web app.

    **Parameters:**
        * launchSession – LaunchSession containing info about the web app session
        * service – DeviceService that was responsible for launching this web app

:doc:`ServiceSubscription <and-servicesubscription>` <MessageListener> **subscribeWebAppStatus** (MessageListener *listener*)
   
    Subscribes to changes in the web app's status.

    **Parameters:**
        * listener – (optional) MessageListener to be called on app status change

void **connect** (:doc:`ResponseListener <and-responselistener>` <Object> *connectionListener*)
   
    Establishes a communication channel with the web app.

    **Parameters:**
        * connectionListener – (optional) ResponseListener to be called on success

void **join** (:doc:`ResponseListener <and-responselistener>` <Object> *connectionListener*)
    
    Establishes a communication channel with a currently running web app.

    **Parameters:**
        * connectionListener

void **disconnectFromWebApp** ()
   
    Closes any open communication channel with the web app.

void **pinWebApp** (String *webAppId*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Pin the web app on the launcher.

    **Parameters:**
        * webAppId
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **unPinWebApp** (String *webAppId*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    UnPin the web app on the launcher.

    **Parameters:**
        * webAppId – NSString webAppId to be unpinned.
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **isWebAppPinned** (String *webAppId*, :doc:`WebAppPinStatusListener <and-webapppinstatuslistener>` *listener*)
   
    To check if the web app is pinned or not

    **Parameters:**
        * webAppId
        * listener – (optional) WebAppPinStatusListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`WebAppPinStatusListener <and-webapppinstatuslistener>`> **subscribeIsWebAppPinned** (String *webAppId*, :doc:`WebAppPinStatusListener <and-webapppinstatuslistener>` *listener*)
   
    Subscribe to check if the web app is pinned or not

    **Parameters:**
        * webAppId
        * listener – (optional) WebAppPinStatusListener with methods to be called on success or failure

void **close** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Closes the web app on the first screen device.

    **Parameters:**
        * listener – (optional) ResponseListener to be called on success

void **sendMessage** (String *message*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Sends a simple string to the web app. The Connect SDK JavaScript
    Bridge will receive this message and hand it off as a string object.

    **Parameters:**
        * message
        * listener – (optional) ResponseListener to be called on success

void **sendMessage** (JSONObject *message*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Sends a JSON object to the web app. The Connect SDK JavaScript Bridge
    will receive this message and hand it off as a JavaScript object.

    **Parameters:**
        * message
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`WebAppSessionListener <and-webappsessionlistener>` **getWebAppSessionListener** ()
   
    When messages are received from a web app, they are parsed into the
    appropriate object type (string vs JSON/NSDictionary) and routed to
    the WebAppSessionListener.

void **setWebAppSessionListener** (:doc:`WebAppSessionListener <and-webappsessionlistener>` *listener*)
   
    When messages are received from a web app, they are parsed into the
    appropriate object type (string vs JSON/NSDictionary) and routed to
    the WebAppSessionListener.

    **Parameters:**
        * listener – WebAppSessionListener to be called when messages are received from the web app

Inherited Methods
-----------------

:doc:`MediaControl <and-mediacontrol>` **getMediaControl** ()
   
    Get MediaControl implementation

    **Returns:** MediaControl

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaControlCapabilityLevel** ()
   
    Get a capability priority for current implementation

    **Returns:** CapabilityPriorityLevel

void **play** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Send play command.

    **Related capabilities:**
        * ``MediaControl.Play``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **pause** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Send pause command.

    **Related capabilities:**
        * ``MediaControl.Pause``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **stop** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Send play command.

    **Related capabilities:**
        * ``MediaControl.Stop``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **rewind** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Send rewind command.

    **Related capabilities:**
        * ``MediaControl.Rewind``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **fastForward** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Send play command.

    **Related capabilities:**
        * ``MediaControl.FastForward``

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **previous** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    This method is deprecated. Use ``PlaylistControl::previous(ResponseListener<Object> listener)`` instead.

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **next** (:doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    This method is deprecated. Use ``PlaylistControl::next(ResponseListener<Object> listener)`` instead.

    **Parameters:**
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **seek** (long *position*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Seeks to a new position within the current media item

    **Related capabilities:**
        * ``MediaControl.Seek``

    **Parameters:**
        * position – The new position, in milliseconds from the beginning of the stream
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

void **getDuration** (:doc:`DurationListener <and-durationlistener>` *listener*)
   
    Get the current media duration in milliseconds

    **Parameters:**
        * listener – (optional) DurationListener with methods to be called on success or failure

void **getPosition** (:doc:`PositionListener <and-positionlistener>` *listener*)
   
    Get the current playback position in milliseconds

    **Parameters:**
        * listener – (optional) PositionListener with methods to be called on success or failure

void **getPlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)
   
    Get the current state of playback

    **Parameters:**
        * listener – (optional) PlayStateListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`PlayStateListener <and-playstatelistener>`> **subscribePlayState** (:doc:`PlayStateListener <and-playstatelistener>` *listener*)
   
    Subscribe for playback state changes

    **Parameters:**
        * listener – receives play state notifications

    **Returns:** ServiceSubscription<PlayStateListener>

:doc:`MediaPlayer <and-mediaplayer>` **getMediaPlayer** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getMediaPlayerCapabilityLevel** ()

void **getMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
    
    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

:doc:`ServiceSubscription <and-servicesubscription>` <:doc:`MediaInfoListener <and-mediainfolistener>`> **subscribeMediaInfo** (:doc:`MediaInfoListener <and-mediainfolistener>` *listener*)
    
    **Parameters:**
        * listener – (optional) MediaInfoListener with methods to be called on success or failure

void **displayImage** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, LaunchListener *listener*)
   
    Display an image on the device. Not all devices support all of the
    parameters -- supply as many as you have available.

    **Related capabilities:**
        * ``MediaPlayer.Display.Image``
        * ``MediaPlayer.MediaData.Title``
        * ``MediaPlayer.MediaData.Description``
        * ``MediaPlayer.MediaData.Thumbnail``
        * ``MediaPlayer.MediaData.MimeType``

    **Parameters:**
        * mediaInfo – Object of MediaInfo class which includes all the information about an image to display.
        * listener – (optional) LaunchListener with methods to be called on success or failure

void **playMedia** (:doc:`MediaInfo <and-mediainfo>` *mediaInfo*, boolean *shouldLoop*, LaunchListener *listener*)
   
    Play an audio or video file on the device. Not all devices support
    all of the parameters -- supply as many as you have available.

    **Related capabilities:**
        * ``MediaPlayer.Play.Video``
        * ``MediaPlayer.Play.Audio``
        * ``MediaPlayer.MediaData.Title``
        * ``MediaPlayer.MediaData.Description``
        * ``MediaPlayer.MediaData.Thumbnail``
        * ``MediaPlayer.MediaData.MimeType``

    **Parameters:**
        * mediaInfo – Object of MediaInfo class which includes all the information about an image to display.
        * shouldLoop – Whether to automatically loop playback
        * listener – (optional) LaunchListener with methods to be called on success or failure

void **closeMedia** (:doc:`LaunchSession <and-launchsession>` *launchSession*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Close a running media session. Because media is handled differently
    on different platforms, it is required to keep track of LaunchSession
    and MediaControl objects to control that media session in the future.
    LaunchSession will be required to close the media and mediaControl
    will be required to control the media.

    **Related capabilities:**
        * ``MediaPlayer.Close``

    **Parameters:**
        * launchSession – LaunchSession object for use in closing media instance
        * listener – (optional) ResponseListener< Object > with methods to be called on success or failure

:doc:`PlaylistControl <and-playlistcontrol>` **getPlaylistControl** ()

:doc:`CapabilityPriorityLevel <and-capabilityprioritylevel>` **getPlaylistControlCapabilityLevel** ()

void **jumpToTrack** (long *index*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Jump the playlist to the designated track.

    Play a track specified by index in the playlist

    **Related capabilities:**
        * ``PlaylistControl.JumpToTrack``

    **Parameters:**
        * index – index in the playlist, it starts from zero like index of array
        * listener – optional response listener

void **setPlayMode** (:doc:`PlayMode <and-playmode>` *playMode*, :doc:`ResponseListener <and-responselistener>` <Object> *listener*)
   
    Set order of playing tracks

    **Parameters:**
        * playMode
        * listener – optional response listener
