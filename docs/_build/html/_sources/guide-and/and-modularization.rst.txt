Modularization
===============
Structure
-----------
The `Connect SDK repositories`_ are adopting
a modular approach with 1.4.0 release. Our aim is to provide flexibility to
the developers to be able pick and choose between the various devices.
Currently you can choose whether to include `Google Cast`_
and `Fire TV`_ devices or not.
We plan to include more device options in the upcoming releases.

.. _Connect SDK repositories: https://github.com/ConnectSDK
.. _Google Cast: https://developers.google.com/cast/
.. _Fire TV: https://developer.amazon.com/apps-and-games/fire-tv

The Connect SDK is split into modules with the help of
`git submodules`_.
There are two options:

.. _git submodules: https://git-scm.com/book/en/v2/Git-Tools-Submodules

1. The **full** project (*Connect-SDK-iOS* and *Connect-SDK-Android*) includes
three submodules: core, google-cast, and firetv and thus provides the full feature set.
The latter submodules are located in the modules directory.

2. The **lite** project (*Connect-SDK-iOS-Lite* and *Connect-SDK-Android-Lite*)
includes the core submodule only, therefore there is no need to download
any third-party dependencies.

Please refer to the figure below displaying dependencies between different
modules and libraries (for iOS and Android).

Components with a light green background are external dependencies.
The dashed lines show the submodule links, whereas the solid lines depict build
and/or runtime dependencies.

.. figure:: ../_static/image/android_modules@2x.png
   :alt: Android SDK Component Diagram

   Figure 1. Android SDK Component Diagram (showing Google Cast submodule as an example)

Links to the repositories are provided in the next table:

.. list-table:: Table 1. Links to the repositories of Android
   :widths: auto
   :header-rows: 1
   :stub-columns: 1

   * - Module
     - Link
   * - full
     - `https://github.com/ConnectSDK/Connect-SDK-Android`_
   * - lite
     - `https://github.com/ConnectSDK/Connect-SDK-Android-Lite`_
   * - core
     - `https://github.com/ConnectSDK/Connect-SDK-Android-Core`_
   * - google-cast
     - `https://github.com/ConnectSDK/Connect-SDK-Android-Google-Cast`_
   * - firetv
     - `https://github.com/ConnectSDK/Connect-SDK-Android-FireTV <https://github.com/ConnectSDK/Connect-SDK-Android-FireTV>`_

.. _https://github.com/ConnectSDK/Connect-SDK-Android: https://github.com/ConnectSDK/Connect-SDK-Android
.. _https://github.com/ConnectSDK/Connect-SDK-Android-Lite: https://github.com/ConnectSDK/Connect-SDK-Android-Lite
.. _https://github.com/ConnectSDK/Connect-SDK-Android-Core: https://github.com/ConnectSDK/Connect-SDK-Android-Core
.. _https://github.com/ConnectSDK/Connect-SDK-Android-Google-Cast: https://github.com/ConnectSDK/Connect-SDK-Android-Google-Cast
.. _https://github.com/ConnectSDK/Connect-SDK-Android-FireTV: https://github.com/ConnectSDK/Connect-SDK-Android-FireTV

Usage instructions can be found in the `full README`_ or `lite README`_.

.. _full README: https://github.com/ConnectSDK/Connect-SDK-iOS/blob/master/README.md
.. _lite README: https://github.com/ConnectSDK/Connect-SDK-iOS-Lite/blob/master/README.md

Contributing
-------------
Since the source code is split between three repositories now (in the full
version, whereas lite has only two), contributing is a bit more involved now.
If you add a new feature across all the modules, you will have to create
two GitHub pull requests, one for each module. Our team will check the code and
merge the changes into the submodules, then update the full and lite
repositories (as those just keep the project and track commits from the submodules).
If you have a simpler contributing workflow in mind, please `let us know`_.

.. _let us know: developer@lge.com
