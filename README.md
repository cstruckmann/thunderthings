# thunderthings

Integration between Thunderbird and Cultured Code's Things on macOS.

This Thunderbird add-on provides a mechanism to create a Things to-do that contains a link to an email message. When the link in the to-do is clicked, Thunderbird will open and display the message (requires Thunderbird version 98 or later for message links to work on macOS).

ThunderThings consists of two components: a Thunderbird add-on and a macOS application that must be installed on the system and run once (to install some files). The Thunderbird extension communicates with the app to create items using Things' Quick Entry interface.

Please note that I have no affiliation or connection to Cultured Code other than being a user of their software.


## Installation

You must install two components.

1. ThunderThings add-on. In Thunderbird, go to Tools > Add-ons and Themes and search for "ThunderThings". 

2. ThunderThings macOS application. Download the zip file from https://github.com/snchong/thunderthings/releases/latest and open it. Move the ThunderThings application to the `/Applications` directory on your computer and run it.

  When the application is run, it installs files that allows the Thunderbird add-on to communicate with the ThunderThings app, which is what opens the Things' Quick Entry interface. In more detail, it installs a manifest file as required by [Mozilla's native messaging](https://wiki.mozilla.org/WebExtensions/Native_Messaging) in the directory `~/Library/Application Support/Mozilla/NativeMessagingHosts/` and in the directory `/Library/Application Support/Mozilla/NativeMessagingHosts/`. (Installation in the latter directory is required to get it to work on some machines, as manifest file in the user directory does not seem to be used.)


## Usage

When a message is selected (or window/tab that shows a single message is active), you can activate ThunderThings by (a) clicking the "Add to Things..." button in the toolbar; (b) selecting "Add to Things..." in the context menu; or (c) pressing ctrl-shift-A.

There are currently no configurable options.


## Feedback or suggestions

Contact thunderthings@gajong.com.