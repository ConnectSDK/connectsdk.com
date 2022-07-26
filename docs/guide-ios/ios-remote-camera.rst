Remote Camera
================

With Connect SDK integrated in the mobile app, it can display camera preview on the TV screen.
This allows you to use your mobile device’s camera as a remote camera for the TV that does not have an internal or USB camera.

.. note::
    This feature is only supported on webOS TV 22.


Requirements
-------------------------

**Including the Connect SDK using CocoaPods and setting up for remote camera**

Add ``pod "ConnectSDK"`` to your ``Podfile``, and run ``pod install``. Open the workspace file and run your project.

Note that remote camera runs on iOS 12 and higher. Refer to the ``Podfile`` example below.

.. code-block:: obj-c

    platform :ios, '12.0'
	
    def app_pods
        pod 'ConnectSDK/Core', :git => 'https://github.com/ConnectSDK/Connect-SDK-iOS.git', :branch => 'master', :submodules => true
    end
	
    target 'RemoteCamera-Sampler' do
      use_frameworks!
      app_pods
	
    end


How to Use Remote Camera
-------------------------

To use a remote camera, follow the steps below.


1. Search Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search for devices (TVs) connected to your home network. You can set the filter to only search for TVs that support the remote camera function.

.. code-block:: obj-c

    ...
    
    - (void)startDiscoveryTV {
        _isDiscoveringTV = YES;
 
        if (_discoveryManager == nil) {
            _discoveryManager = [DiscoveryManager sharedManager];
        }
             
        NSArray *capabilities = @[
            kRemoteCameraControlRemoteCamera
        ];
 
        CapabilityFilter *filter = [CapabilityFilter filterWithCapabilities:capabilities];
        [_discoveryManager setCapabilityFilters:@[filter]];
        [_discoveryManager setPairingLevel:DeviceServicePairingLevelOn];
        [_discoveryManager registerDeviceService:[WebOSTVService class] withDiscovery:[SSDPDiscoveryProvider class]];
        [_discoveryManager startDiscovery];
    }
    
    ...


2. Request Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The remote camera function requires the camera and microphone permission. The user must grant these permissions when the remote camera is first executed.
Register NSCameraUsageDescription and NSMicrophoneUsageDescription in ``Info.plist``.

.. code-block:: obj-c

    <key>NSCameraUsageDescription</key>
    <string></string>
    <key>NSMicrophoneUsageDescription</key>
    <string></string>


3. Select a TV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the TV to run the remote camera on by using the Picker. Implement DevicePickerDelegate to receive TV selection events.

.. code-block:: obj-c

    _discoveryManager.devicePicker.delegate = self;
    [_discoveryManager.devicePicker showPicker:nil];

Create a ViewController to display the camera preview after the TV is selected. You need to make ViewController work only in landscape mode.

.. code-block:: obj-c

    // MARK: DevicePickerDelegate
    - (void)devicePicker:(DevicePicker *)picker didSelectDevice:(ConnectableDevice *)device {
        RemoteCameraViewController *vc = [self.storyboard instantiateViewControllerWithIdentifier:@"RemoteCameraViewController"];
        [vc setDevice:device];
        [self presentViewController:vc animated:YES completion:nil];
    }

Get a RemoteCameraControl object to use the remote camera API. And implement RemoteCameraControlDelegate to receive events that occur during remote camera operation.

.. code-block:: obj-c

    _remoteCameraControl = [_device remoteCameraControl];
    [_remoteCameraControl setRemoteCameraDelegate:self];


4. Start Remote Camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you can run the remote camera.
First, connect with the selected TV device through startRemoteCamera of RemoteCameraControl. Then show the camera preview in the returned UIView.
Paring is required if this is the first time connecting to a TV.

.. code-block:: obj-c

    UIView *previewView = [_remoteCameraControl startRemoteCamera];
    [previewView setFrame:UIScreen.mainScreen.bounds];
    [self.view addSubview:previewView];
    [self.view sendSubviewToBack:previewView];


5. Start Camera Playback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select iPhone camera on your TV. It will start sending and playing the camera stream. At this time, you can receive callbacks by designating a delegate.

.. code-block:: obj-c

    // MARK: RemoteCameraControlDelegate
    - (void)remoteCameraDidPlay {
        NSLog(@"remoteCameraDidPlay");
    }
    
    - (void)remoteCameraDidChange:(RemoteCameraProperty)property {
        NSLog(@"remoteCameraDidChange");
    }


6. Stop Remote Camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you want to stop the remote camera, call stopRemoteCamera.

.. code-block:: obj-c

    if (_remoteCameraControl != nil) {
        [_remoteCameraControl stopRemoteCamera];
	    _remoteCameraControl = nil;
    }


Features
-----------------------------


Change Camera Property
~~~~~~~~~~~~~~~~~~~~~~~

You can change camera properties such as brightness and AWB on the TV, and you can receive callbacks by designating a delegate.

.. code-block:: obj-c

    // MARK: RemoteCameraControlDelegate
    - (void)remoteCameraDidChange:(RemoteCameraProperty)property {
        NSLog(@"remoteCameraDidChange");
    }


Handle Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~

The following runtime error might occur while the remote camera is running.

  - When the network connection is terminated
  - When the TV is turned off
  - When the remote camera is terminated on the TV
  - When the mobile device’s notification terminates the remote camera
  - When other exceptions occurred

For these errors, it is necessary to receive the error in real-time through the listener and respond appropriately.


.. code-block:: obj-c

    - (void)remoteCameraErrorDidOccur:(RemoteCameraError)error {
        NSLog(@"remoteCameraErrorDidOccur");
        
        if (_remoteCameraControl != nil) {
            [_remoteCameraControl stopRemoteCamera];
    	    _remoteCameraControl = nil;
        }
    }


Also, if the app is in the background state, the remote camera function does not work, so you have to handle these situations appropriately.

.. code-block:: obj-c

    - (void)viewDidAppear:(BOOL)animated {
        [super viewDidAppear:animated];
    
        ...
    
        [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(didEnterBackground)
                                                 name:UIApplicationDidEnterBackgroundNotification object:nil];
    }

    - (void)didEnterBackground {
	    if (_remoteCameraControl != nil) {
    	    [_remoteCameraControl stopRemoteCamera];
        	_remoteCameraControl = nil;
  		}
    }

    - (void)viewWillDisappear:(BOOL)animated {
        [super viewWillDisappear:animated];

        [[NSNotificationCenter defaultCenter] removeObserver:self
                                                    name:UIApplicationDidEnterBackgroundNotification
                                                  object:nil];
    }


Set the Microphone Mute State
~~~~~~~~~~~~~~~~~~~~~~

If you change the microphone mute state, it must be transmitted. The app must maintain the current mute setting value.

.. code-block:: obj-c

    if (_remoteCameraControl != nil) {
        [_remoteCameraControl setMicMute:_isMuted];
    }


Switch between Front and Back Cameras
~~~~~~~~~~~~~~~~~

When the direction of the camera is switched between front and rear, the camera direction is transmitted.
The app must maintain the current camera direction value.


.. code-block:: obj-c

    if (_remoteCameraControl != nil) {
	    [_remoteCameraControl setLensFacing:lensFacing];
    }

