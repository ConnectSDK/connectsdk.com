Remote Camera
================

With Connect SDK integrated in the mobile app, it can display camera preview on the TV screen. 
This allows you to use your mobile device’s camera as a remote camera for the TV that does not have an internal or USB camera. 
This guide assumes that you completed the setup described in the :doc:`Setup Instructions <and-setup-instructions>`.

.. note::
    This feature is only supported on webOS TV 22.


How to Use Remote Camera
-------------------------

To use a remote camera, follow the steps below.


1. Check the Android Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The remote camera function is supported by Android 7 (N, API Level 24) and higher.
When you run the app, check the OS version to see if the remote camera is available. 
If the OS version does not support the remote camera function, the function will not work or the app will close.


.. code-block:: java

   if (RemoteCameraApi.getInstance().isCompatibleOsVersion() == false) {
       // The OS version is lower than Android 7
       // and remote camera is not supported
   }


2. Search Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search for devices (TVs) connected to your home network. You can set the filter to only search for TVs that support the remote camera function. 
Since the search for TVs takes some time, it should be started as soon as the app is running.

.. code-block:: java

    // Initializes DiscoveryManager
    DiscoveryManager.init(this);
 
    // Sets a device search filter for devices that support remote camera
    ArrayList<String> capabilities = new ArrayList<>();
    capabilities.add(RemoteCameraControl.RemoteCamera);
    CapabilityFilter filter = new CapabilityFilter(capabilities);
 
    // Searches devices
    DiscoveryManager.getInstance().setPairingLevel(DiscoveryManager.PairingLevel.ON);
    DiscoveryManager.getInstance().setCapabilityFilters(filter);
    DiscoveryManager.getInstance().registerDeviceService(WebOSTVService.class, SSDPDiscoveryProvider.class);
    DiscoveryManager.getInstance().start();


3. Request Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The remote camera function requires the camera permission (android.permission.CAMERA) and audio permission (android.permission.RECORD_AUDIO). 
The user must grant these permissions when the remote camera is first executed.



.. code-block:: java

    // Requests permissions
    String[] permissions = new String[]{android.permission.CAMERA, Manifest.permission.RECORD_AUDIO};
    ActivityCompat.requestPermissions(this, permissions, REQUEST_CODE_ACCESS_PERMISSIONS);
 
    // Delivers request results to onRequestPermissionsResult
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
 
        if (requestCode == REQUEST_CODE_ACCESS_PERMISSIONS) {
            if (hasPermission() == true) {
                // Succeeded to get permission
            } else {
                // Failed to get permission
            }
        }
    }
 
    // Checks the permissions 
    private boolean hasPermission() {
        return ActivityCompat.checkSelfPermission(this, Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED &&
            ActivityCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED;
    }



4. Select a TV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the TV to run the remote camera on by using the Picker. 
After selecting a TV, get a RemoteCameraControl object to use the remote camera API.

.. code-block:: java

    private RemoteCameraControl mRemoteCameraControl ;
 
    AdapterView.OnItemClickListener listener = (adapter, parent, position, id) -> {
        ConnectableDevice connectableDevice = (ConnectableDevice) adapter.getItemAtPosition(position);
        mRemoteCameraControl  = connectableDevice.getRemoteCameraControlControl();
        ...
    };
 
    // Displays a TV search picker dialog
    AlertDialog dialog = new DevicePicker(this).getPickerDialog(getString(R.string.dialog_select_tv), listener);
    dialog.show();


5. Start Remote Camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you can run the remote camera.
First, create a SurfaceView component to show a camera preview, and then pass its Surface as a parameter. 
If the preview is not needed, set the Surface to null. In addition, set initial values such as the microphone mute settings or the camera lens direction and pass them as parameters.
Pairing is required when you connect to a TV for the first time, and the user is informed about it.

.. code-block:: java

    // Create a SurfaceView to display the camera preview
    SurfaceView surfaceView = findViewById(R.id.surfaceView);
    SurfaceHolder holder = surfaceView.getHolder();
 
    holder.addCallback(new SurfaceHolder.Callback() {
        public void surfaceCreated(SurfaceHolder holder) {
            // When the SurfaceView is created, pass it as an argument to request the remote camera to start
            startRemoteCamera(holder.getSurface());
        }
 
        ...
    });
 
    private void startRemoteCamera(Surface surface) {
        AlertDialog pairingAlert = new AlertDialog.Builder(this)
            .setTitle(getString(R.string.dialog_title_notice))
            .setCancelable(false)
            .setMessage(getString(R.string.dialog_allow_pairing))
            .setNegativeButton(android.R.string.ok, null)
            .create();
 
        // Starts the remote camera
        // Each progress is passed through a callback function
        mRemoteCameraControl.startRemoteCamera(this, surface, mMicMute, mLensFacing, new RemoteCameraStartListener() {
            // When connecting to a TV for the first time, a pop-up about the mobile connection is displayed on the TV, 
            // and a pairing procedure procedure is required once in which the user selects [OK] with the remote control. 
            // To do this, the app should display a pop-up with information about pairing
            public void onPairing() {
                pairingAlert.show();
            }
 
            // This is a callback function when the remote camera starts 
            // and whether or not it succeeds is passed through the result parameter
            public void onStart(boolean result) {
                if (result == true) {
                    mPlayingAlert.show();
                } else {
                    Toast.makeText(CameraPreviewActivity.this, getString(R.string.toast_start_failed), Toast.LENGTH_SHORT).show();
                    finish();
                }
                pairingAlert.dismiss();
            }
        });
 
 
 
        // Handles the callback when camera properties are changed on the TV
        mRemoteCameraControl.setPropertyChangeListener(this, property -> {
            Toast.makeText(this, getString(R.string.toast_property_changed) + ": " + property, Toast.LENGTH_SHORT).show();
        });
 
        // This is a callback function when an unexpected error occurs while running the remote camera
        // An error occurs when the network is disconnected, the TV is shut down, etc.
        mRemoteCameraControl.setErrorListener(this, error -> {
            Toast.makeText(this, getString(R.string.toast_running_error) + ": " + error, Toast.LENGTH_SHORT).show();
            mPlayingAlert.dismiss();
        });
    }


6. Start Camera Playback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can designate setCameraPlayingListener to receive a callback when camera stream transmission and playback start by selecting the mobile device's camera on the TV. 
When the camera playback starts on the TV, take appropriate actions such as removing pop-ups.

.. code-block:: java

    // Handles the callback function when the remote camera preview screen starts by selecting the mobile on the TV
    mRemoteCameraControl.setCameraPlayingListener(this, () -> {
        Toast.makeText(this, getString(R.string.toast_play_started), Toast.LENGTH_SHORT).show();
        mPlayingAlert.dismiss();
    });


7. Stop Remote Camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you want to stop the remote camera, call stopRemoteCamera. 


.. code-block:: java

    mRemoteCameraControl.stopRemoteCamera(this, result->{
        ...           
    });



Features
-----------------------------


Change Camera Property
~~~~~~~~~~~~~~~~~~~~~~~

You can change camera properties such as brightness and AWB on the TV, and you can receive callbacks by designating a setPropertyChangeListener listener.


.. code-block:: java

    // Handles the callback function when changing camera properties on the TV
    mRemoteCameraControl.setPropertyChangeListener(this, property -> {
        Toast.makeText(this, getString(R.string.toast_property_changed) + ": " + property, Toast.LENGTH_SHORT).show();
    });



Handle Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~

The following runtime error might occur while the remote camera is running.

  - When the network connection is terminated 
  - When the TV is turned off
  - When the remote camera is terminated on the TV 
  - When the mobile device’s notification terminates the remote camera
  - When other exceptions occurred

For these errors, it is necessary to receive the error in real-time through the listener and respond appropriately.


.. code-block:: java

    // This is a callback function when an unexpected error occurs while running a remote camera
    // An error occurs when the network connection is disconnected, the TV is shut down, etc.
    mRemoteCameraControl.setErrorListener(this, error -> {
        Toast.makeText(this, getString(R.string.toast_running_error) + ": " + error, Toast.LENGTH_SHORT).show();
        mPlayingAlert.dismiss();
    });



Set the Microphone Mute State
~~~~~~~~~~~~~~~~~~~~~~
If you change the microphone mute state, it must be transmitted. The app must maintain the current mute setting value.

.. code-block:: java

    mRemoteCameraControl.setMicMute(this, mMicMute); // true or false


Switch between Front and Back Cameras
~~~~~~~~~~~~~~~~~

When the direction of the camera is switched between front and rear, the camera direction is transmitted. 
The app must maintain the current camera direction value.


.. code-block:: java

    mRemoteCameraControl.setLensFacing(this, mLensFacing); // RemoteCameraApi.LENS_FACING_BACK or RemoteCameraApi.LENS_FACING_FRONT

