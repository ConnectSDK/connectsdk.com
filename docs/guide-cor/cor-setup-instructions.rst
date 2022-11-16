Setup Instructions
==================

Requirements
------------

This guide assumes basic familiarity with Cordova (PhoneGap), Xcode, and
Eclipse. For a more detailed walkthrough of setting up a Cordova
project, see the `Cordova platform guides`_.

You should also have:

-  Cordova 5.0 or later. We strongly encourage you to use the latest
   Cordova tools (5.2.0 at the time of this release)
-  iOS: Xcode and Xcode command line tools
-  Android: Android SDK with "android" tool in PATH or ANDROID_HOME
   environment variable (`Cordova's Setup Guide`_)

Creating a Cordova app
----------------------

Open a command terminal and cd to the directory where you want to create
your Cordova project:

.. code::

   cordova create hello_connect com.example.helloconnect HelloConnect

This will create a directory named "hello_connect" with a basic Cordova
app. Use the following commands to create iOS and Android projects:

.. code::

   cd hello_connect
   cordova platform add android
   cordova platform add ios

.. note::

   Due to a bug in the current version of Cordova, do not put any
   spaces in the app name.

Add the Connect SDK Cordova plugin
----------------------------------

This will download and install the Connect SDK plugin:

.. code:: 

   cordova plugin add cordova-plugin-connectsdk

The plugin will set up the projects automatically. If you run into any
issues with the automatic setup process, please email
developer@lge.com or file an issue on Github.

.. _Cordova platform guides: https://cordova.apache.org/docs/en/5.0.0/guide_platforms_index.md.html#Platform%20Guides
.. _Cordova's Setup Guide: http://cordova.apache.org/docs/en/5.0.0/guide_platforms_android_index.md.html#Android%20Platform%20Guide
