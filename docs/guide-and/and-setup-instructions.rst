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

   allprojects {
    repositories {
        google()
        jcenter()
        maven { url "https://jitpack.io" }
    }
   }

   //...

   dependencies {
      //...
      implementation 'com.github.ConnectSDK:Connect-SDK-Android:master-SNAPSHOT'
   }


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
            implementation project(':Connect-SDK-Android')
           }

#. Sync project with gradle files

#. Add permissions to your manifest


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

* Required for Screen Mirroring and Remote Camera

   * ``android.permission.RECORD_AUDIO``
   * ``android.permission.FOREGROUND_SERVICE``
   * ``android.permission.CAMERA``

.. code-block:: xml

   <uses-permission android:name="android.permission.INTERNET"/>
   <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
   <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
   <uses-permission android:name="android.permission.CHANGE_WIFI_MULTICAST_STATE"/>
   <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
   <uses-permission android:name="android.permission.RECORD_AUDIO" />
   <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
   <uses-permission android:name="android.permission.CAMERA" />


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
