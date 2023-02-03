Screen Mirroring
==================

With Connect SDK integrated in the mobile app, it can cast the screen and sound into the TV screen. 
This allows you to extend the screen of a mobile app to a larger TV screen and share it with your family. 
This guide assumes that you completed the setup described in the :doc:`Setup Instructions <and-setup-instructions>`.

There are two ways to display the screen to your TV. 

- Screen mirroring: A way to dispay the entire app screen to the TV.

- Dual screen: A way to create a second screen of the app and display it on the TV while leaving the app screen separate. Dual screen is provided as a screen mirroring function.

.. note::
    This feature is only supported on webOS TV 22.


How to Use Screen Mirroring
-------------------------

To use screen mirroring, follow these steps.



1. Check the Android Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Screen mirroring runs on Android version 10 (Q, API Level 29) and higher, so you need to check the OS version when starting the app.
If the OS version does not support the screen mirroring function, the function will not work or the app will close.

.. code-block:: java

   if (ScreenMirroringControl.isCompatibleOsVersion() == false) {
       // The OS version is lower than Android 10
       // and screen mirroring is not supported
    }


2. Search Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search for devices (TVs) connected to your home network. You can set the filter to only search for TVs that support the screen mirroring function.
Since the search for TVs takes some time, it should be started as soon as the app is running.

.. code-block:: java

    // Initializes DiscoveryManager
    DiscoveryManager.init(this);
 
    // Sets a device search filter for devices that support screen mirroring (dual screen).
    ArrayList<String> capabilities = new ArrayList<>();
    capabilities.add(ScreenMirroringControl.ScreenMirroring);
    CapabilityFilter filter = new CapabilityFilter(capabilities);
 
    // Searches devices
    DiscoveryManager.getInstance().setPairingLevel(DiscoveryManager.PairingLevel.ON);
    DiscoveryManager.getInstance().setCapabilityFilters(filter);
    DiscoveryManager.getInstance().registerDeviceService(WebOSTVService.class, SSDPDiscoveryProvider.class);
    DiscoveryManager.getInstance().start();


3. Request Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The screen mirroring requires the audio permission (android.permission.RECORD_AUDIO). 
The permission agreement is executed only once on the first run or when there is no permission.


.. code-block:: java

    // Requests permissions
    String[] permissions = new String[]{Manifest.permission.RECORD_AUDIO};
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
        return ActivityCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED;
    }



4. Get User Approval for Screen Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~

User approval is required to capture the screen.
Intent data must be delivered to the screen mirroring API when consenting to screen capture.

.. code-block:: java

    // User approval is required to capture the screen
    // Displays the system dialog for user approval
    MediaProjectionManager projectionManager = (MediaProjectionManager) getSystemService(Context.MEDIA_PROJECTION_SERVICE);
    startActivityForResult(projectionManager.createScreenCaptureIntent(), REQUEST_CODE_CAPTURE_CONSENT);
 
    // Passes the user approval result to onActivityResult
    public void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
 
        if (requestCode == REQUEST_CODE_CAPTURE_CONSENT) {
            if (resultCode == Activity.RESULT_OK) {
                // Succeed to get user approval
                // Intent data must be saved and delivered to screen mirroring API
                mProjectionData = data;
            } else {
                // User Approval Failed
            }
        }
    }



5. Select a TV
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the TV to run the screen mirroring on by using the Picker. 
After selecting a TV, get a ScreenMirroringControl object to use the screen mirroring API.

.. code-block:: java

    private ScreenMirroringControl mScreenMirroringControl;

    AdapterView.OnItemClickListener listener = (adapter, parent, position, id) -> {
        ConnectableDevice connectableDevice = (ConnectableDevice) adapter.getItemAtPosition(position);
        mScreenMirroringControl = connectableDevice.getScreenMirroringControl();
        ...
    };
 
    // Displays a TV search picker dialog
    AlertDialog dialog = new DevicePicker(this).getPickerDialog(getString(R.string.dialog_select_tv), listener);
    dialog.show();


6. Start Screen Mirroring
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you can run the screen mirroring. 
Pairing is required when you connect to a TV for the first time, and the user is informed about this.

The following runtime errors might occur while the screen mirroring is running.

   - When the network connection is terminated
   - When the TV is turned off
   - When the screen mirroring is terminated on the TV
   - When the mobile device’s notification terminates the screen mirroring
   - When other exceptions occurred

For these errors, it is necessary to receive the error in real-time through the listener and respond appropriately.

.. code-block:: java

    ProgressDialog progress = new ProgressDialog(this);
    progress.setMessage(getString(R.string.dialog_connecting_tv));
    progress.show();
 
    // Displays the pairing pop-up
    AlertDialog pairingAlert = new AlertDialog.Builder(this)
            .setTitle(getString(R.string.dialog_title_notice))
            .setCancelable(false)
            .setMessage(getString(R.string.dialog_allow_pairing))
            .setNegativeButton(android.R.string.ok, null)
            .create();
 
    // Start the screen mirroring
    // Each progress is passed through a callback function
    mScreenMirroringControl.startScreenMirroring(this, mProjectionData, new ScreenMirroringStartListener() {
        // When connecting to a TV for the first time, a pop-up about the mobile connection is displayed on the TV, 
        // and a pairing procedure is required once in which the user selects [OK] with the remote control
        // To do this, the app should display a pop-up with information about pairing
        public void onPairing() {
            pairingAlert.show();
        }
 
        // This is a callback function when the screen mirroring starts
        // and whether or not it succeeds is passed through the result parameter
        public void onStart(boolean result, Presentation secondScreen) {
            updateButtonVisibility();
            pairingAlert.dismiss();
            progress.dismiss();
 
            if (result == true) Toast.makeText(ScreenMirroringActivity.this, getString(R.string.toast_start_completed), Toast.LENGTH_SHORT).show();
            else Toast.makeText(ScreenMirroringActivity.this, getString(R.string.toast_start_failed), Toast.LENGTH_SHORT).show();
        }  
    });
 
    // This is a callback function when an unexpected error occurs while running the screen mirroring
    // An error occurs when the network is disconnected, or the TV is shut down, etc.
    mScreenMirroringControl.setErrorListener(this, error -> {
        // Error occurred
    });


7. Stop Screen Mirroring
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you want to stop mirroring, call stopScreenMirroring.

.. code-block:: java

    // Stops screen mirroring. Whether or not to stop normally is passed through the result parameter
    // Abnormal termination is a case in which screen mirroring is stopped without running, etc.
    mScreenMirroringControl.stopScreenMirroring(this, result -> {
        Toast.makeText(ScreenMirroringActivity.this, getString(R.string.toast_stopped), Toast.LENGTH_SHORT).show();
        updateButtonVisibility();
    });

    // Stops device search
    DiscoveryManager.getInstance().stop();
    DiscoveryManager.destroy();



How to Use Dual Screen
---------------------------

Dual screen is a function that creates a second screen, separate from the app screen, and displays it on the TV.
The basic procedure is the same as with the screen mirroring above, and only the differences are explained below.
When mirroring starts, you just need to deliver the user-defined second screen class.


Define Second Screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Inherit Android Presentation class to define a second screen class for dual screen.

.. code-block:: java

    public class SecondScreenDemo extends Presentation implements SnakeGameListener {
        private Context mOuterContext;
     
        public SecondScreenDemo(@NonNull Context outerContext, @NonNull Display display) {
            super(outerContext, display);
            mOuterContext = outerContext;
        }
 
        @Override
        public void onCreate(@NonNull Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            super.setContentView(R.layout.snake_game_second_screen_layout);
        }
        ...
    }


Start Dual Screen
~~~~~~~~~~~~~~~~~~~~~~

Dual screen starts mirroring the screen by using the user-defined, Presentation inherited class.
When the mobile device is connected to the TV, it creates a virtual display for the second screen, creates an instance of the second screen class, and passes it to the onStart callback. 
The user can then access the Second Screen class to control the dual screen.

.. code-block:: java

    mScreenMirroringControl.startScreenMirroring(this, projectionData, SecondScreenDemo.class, new ScreenMirroringControl.ScreenMirroringStartListener() {
       ...
 
        // This is a callback function when screen mirroring starts
        // and whether or not it succeeds is passed through the result parameter
        public void onStart(boolean result, Presentation secondScreen) {
            updateButtonVisibility();
            pairingAlert.dismiss();
            progress.dismiss();
 
            if (result == true) Toast.makeText(getBaseContext(), getString(R.string.toast_start_completed), Toast.LENGTH_SHORT).show();
            else Toast.makeText(getBaseContext(), getString(R.string.toast_start_failed), Toast.LENGTH_SHORT).show();
 
            if (secondScreen != null) {
                mSecondScreenDemo = (SecondScreenDemo) secondScreen;
                mSecondScreenDemo = mSecondScreenDemo.start();           
            }
        }
    });

