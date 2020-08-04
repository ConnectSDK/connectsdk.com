Setup Instructions
====================
Dependencies
-------------
This project has the following dependencies, some of which require manual setup.
If you would like to use a version of the SDK which has no manual setup, consider
using the `lite version`_ of the SDK. This project can be built in Android Studio or
directly with Gradle. Eclipse IDE is not supported since 1.5.0 version.

.. _lite version: https://github.com/ConnectSDK/Connect-SDK-Android-Lite

This project has the following dependencies.

* `Connect-SDK-Android-Core`_ submodule

  * Requires `Java-WebSocket library`_
  * Requires `jmDNS library`_

* `Connect-SDK-Android-Google-Cast`_ submodule

  * Requires `GoogleCast.framework`_

* `Connect-SDK-Android-FireTV`_ submodule

  * Requires Amazon Fling SDK

.. _Connect-SDK-Android-Core: https://github.com/ConnectSDK/Connect-SDK-Android-Core
.. _Java-WebSocket library: https://github.com/TooTallNate/Java-WebSocket
.. _jmDNS library: https://github.com/jmdns/jmdns
.. _Connect-SDK-Android-Google-Cast: https://github.com/ConnectSDK/Connect-SDK-Android-Google-Cast
.. _GoogleCast.framework: https://developers.google.com/cast
.. _Connect-SDK-Android-FireTV: https://github.com/ConnectSDK/Connect-SDK-Android-FireTV

Setup Connect SDK in Android Studio
------------------------------------
Edit your project's build.gradle to add this in the "dependencies" section.

.. code-block:: groovy

   dependencies {
    //...
    compile 'com.connectsdk:connect-sdk-android:1.6.0'
   }

This prebuilt library doesn't have Amazon Fling SDK support, because
it’s not available on maven. You need to set the project up from sources
if you want to have Amazon Fling SDK support.

Setup Connect SDK in Android Studio from sources
------------------------------------------------

#. Open your terminal and execute these commands

   *  cd your_project_folder
   *  git clone https://github.com/ConnectSDK/Connect-SDK-Android.git
   *  cd Connect-SDK-Android
   *  git submodule init
   *  git submodule update

#. On the root of your project directory create/modify the
   settings.gradle file. It should contain something like the following:

    ::

           include ':app', ':Connect-SDK-Android'

#. Edit your project's build.gradle to add this in the "dependencies"
   section:

    ::

           dependencies {
            //...
            compile project(':Connect-SDK-Android')
           }

#. Setup `FireTV module`_

#. Sync project with gradle files

#. Add permissions to your manifest

.. _FireTV module: https://github.com/ConnectSDK/Connect-SDK-Android-FireTV

Permissions to include in manifest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Required for SSDP & Chromecast/Zeroconf discovery

   *  ``android.permission.INTERNET``
   *  ``android.permission.CHANGE_WIFI_MULTICAST_STATE``

* Required for interacting with devices

   *  ``android.permission.ACCESS_NETWORK_STATE``
   *  ``android.permission.ACCESS_WIFI_STATE``

* Required for storing device pairing information

   *  ``android.permission.WRITE_EXTERNAL_STORAGE``

.. code-block:: xml

   <uses-permission android:name="android.permission.INTERNET"/>
   <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
   <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
   <uses-permission android:name="android.permission.CHANGE_WIFI_MULTICAST_STATE"/>
   <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

Metadata for application tag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This metadata tag is necessary to enable Chromecast support.

.. code-block:: xml
   :force:

   <application ... >
       ...

       <meta-data
           android:name="com.google.android.gms.version"
           android:value="@integer/google_play_services_version" />

   </application>
