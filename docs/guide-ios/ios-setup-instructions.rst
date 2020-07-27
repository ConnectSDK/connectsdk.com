Setup Instructions
==================

Using CocoaPods
---------------

#. Add ``pod "ConnectSDK"`` to your ``Podfile``
#. Run ``pod install``
#. Open the workspace file and run your project

**Important**: Unfortunately, Amazon Fling SDK is not distributed via
CocoaPods, so we cannot include its support in a subspec in an automated
way. If you need it, please use the source ConnectSDK project directly.

You can use \ ``pod "ConnectSDK/Core"``\  to get the \ `lite
version`_\ .

Without CocoaPods
-----------------

#. Clone the repository
   (``git clone https://github.com/ConnectSDK/Connect-SDK-iOS.git``)
#. Set up the submodules by running the following command (in the
   ``Connect-SDK-iOS/`` directory in this example):
   ``git submodule update --init``
#. Open your project in Xcode
#. Locate the Connect SDK Xcode project in Finder
#. Drag the Connect SDK Xcode project (``ConnectSDK.xcodeproj``) into
   your project's Xcode library
#. Navigate to your target's settings screen, then navigate to the
   "Build Phases" tab
#. Add the following in the "Link Binary With Libraries" section:

   -  ``libConnectSDK.a``
   -  ``libz.dylib``
   -  ``libicucore.dylib``

#. Navigate to the "Build Settings" tab and add ``-ObjC`` to your
   target's "Other Linker Flags"
#. Follow the setup instructions for the service submodules:

   -  `Connect-SDK-iOS-Google-Cast`_
   -  `Connect-SDK-iOS-FireTV`_

If these steps are failing, try checking the `repository`_ for the
latest setup instructions.

Include Strings File for Localization (optional)
------------------------------------------------

#. Locate the Connect SDK Xcode project in the Finder
#. Drag the ConnectSDKStrings folder into your project's Resources
   folder
#. You may make whatever changes you would like to the values and the
   SDK will use your strings file

.. _lite version: https://github.com/ConnectSDK/Connect-SDK-iOS-Lite
.. _Connect-SDK-iOS-Google-Cast: https://github.com/ConnectSDK/Connect-SDK-iOS-Google-Cast
.. _Connect-SDK-iOS-FireTV: https://github.com/ConnectSDK/Connect-SDK-iOS-FireTV
.. _repository: https://github.com/ConnectSDK/Connect-SDK-iOS/
