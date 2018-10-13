# Plexamp Chrome Global Media Key Hog Fix

Google Chrome allows extensions the option to utilize your media keys globally so you can control your media without having to have Chrome in focus. The problem with this is Chrome hogs the inputs of these keys so you can't use them in other local apps. The only suggested solution was to just uninstall these extensions, or set the media keys to only work when Chrome is in focus. This provides a way to disable the Chrome global options when launchign a local app that you want to have media key support for. Currently Plexamp and Streamkeys are the only supported local apps and Chrome extensions.

## Getting Started

You can opt to run this through a Python interpreter, compile it into an executable yourself, or run it from a precompiled build. That build for now has only been tested on Windows 7 - 64 bit, but I intend to package up builds for both Linux and macOs. Currently installer.py is currently written to generate .bat and .vbs scripts for windows, but again I intend on writing .sh options for UNIX systems.

### Prerequisites

If you wish to run this from a python interpreter, you should be able to run it with standalone python. I've only tested with 3.5 so far, but I'll update as other versions get tested.

If you want to compile your own exe the only dependency is cx_Freeze === 5.1.1.

If you want to use a precompiled build, that should be sufficient.


### Installing with just Python

If you intend on running the underlying scripts using Python, you'll first need to make sure python is installed.

The installation should be pretty painless if Plexamp and Chrome are installed to their default locations. These locations are generally:

```
C:\Users\User\App Data\Local\Programs\plexamp
C:\Users\User\App Data\Local\Google\Chrome\User Data\Default
```

If those are not the install paths, simply go into the config.txt file and add the install locations in resepectively

```
Chrome=Directory\To\Google\Chrome\User Data\Default
Plexamp=Directory\To\plexamp
```

Then once you have your paths configured you simply have to run the installer script.

```
path/to/python.exe installer.py
```

and then you'll have a shortcut created on the Desktop that will allow you to enable stream keys for plex when it's watched

### Compiling to your own exe

To compile to executables, so you don't have to rely on a python interpreter, first make sure cx_Freeze is installed

```
pip install -r requirements.txt
```

and then you can compile a local build by calling

```
path/to/python.exe setup.py build
```

### Installing from a precompiled build

To install from a precompiled build, first unzip the archive.

Then if your Chrome and Plexamp aren't installed in the default locations, go into the config.txt file anda enter those paths similair to above.

Once your paths are configured, go ahead and run Setup.exe, and you should have a shortcut on your Desktop ready to go 

### Using this fix and swapping between what can use media keys

While this does provide somewhat of a painless way to be able to use media keys globally for both local applications and Chrome, chrome only updates when it is shutdown. So before you launch the fix, chrome must be closed.

NOTE: Simply closing out of chrome from the browser doesn't completely close chrome. Chrome will still operate in the background, and you can go into your hidden icons on a windows enviornment and right click on it and close it from there.

Opening the fix when Chrome is completely closed will give the local app complete control of the media keys.

After the local app opens, feel free to fire up chrome and use it like normal.

If you wish to switch back to giving chrome access to the media keys, simply close out of the local media app completely. Again that might be from the bottom toolbar. Once the app is closed, if you have opened Chrome, give Chrome a full restsart, again from the bottom toolbar, and upon reopening, Chrome will have complete control of your media keys again.

### Trobleshooting

## What if the installer.py/Setup.exe doesn't create a shortcut?

Check the errors.txt file. That should point you in the direction if your path to the apps aren't configured correctly.

## What if when I click on the shortcut nothing happens

Navigate to where you installed unzipped the file, you can find this by right clicking the shortcut and clicking open file location in windows. Once there check the errors.txt, again this will tell you if you have any issues with the path.

## I exited the local app and my media keys aren't working with Chrome

There's two things to try here. First make sure Chrome was completely shutdown, again checking in the taskbar to see if it's running down there as well.

If Chrome was shutdown, make sure it again is completely off, and click on the Desktop shortcut, and then close the local app. That should allow Chrome to have access again once it is reopened.

## I've checked my paths and it still won't launch the app

What you can do here is go ahead to the directory, right click on the shortcut and go to file location, and click on Setup.exe again, and that will refresh your shortcut.

Or if you installed from python re-run

```
path/to/python.exe installer.py
```

Add additional notes about how to deploy this on a live system

### Future Additions

Currently this only supports Plexamp in conjuction with the Streamkeys extension on Windows. I'd like to be able to extend this to other local player apps, and other chrome extentions that allow you to control your media globally.

Just as much I'm looking to extend the functionality outside of Windows and into Linux and macOS enviornments as well.

Suggestions are greatly welcome, as are pull requests. If you can add something that I missed or fix something, please do!

### Currenlt Compatible With

[Plexamp](https://plexamp.com/)
[Streamkeys](https://www.streamkeys.com/)
 

## Authors

* **Joe Habel** - *Initial work* - [PurpleBooth](https://github.com/joe-habel)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* There's always a room to give a shoutout to those working on Plex [Thanks Plex](https://www.plex.tv/plex-pass/)!
* Also a shouout to those at Streamkeys [Thanks Streamkeys](https://www.streamkeys.com/donate.html)!
* Support the Devs!
