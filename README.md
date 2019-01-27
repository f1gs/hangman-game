# Hangman
This is my first personal project, inspired by the classic game.

![Game Screenshot](https://raw.githubusercontent.com/rafaelfigs/hangman-game/master/screenshot/screenshot.PNG)

## Requirements
* Python 3.6+
    * Download: https://www.python.org/downloads

## Usage
After you clone this repository to your desktop, go to its directory and run `main.py`.

## Changelog

### [0.1.2] - 2019-01-27
#### Changed
* Part of code was rewritten.

### [0.1.1] - 2019-01-19
#### Added
* A tool that optimize the search time of words randomly in a text file (especially for the hard difficulty).
    * To use this tool, go to `words` folder and make sure there is a `.txt` file in this folder and run `file_creation_tool.py`. Three files will be created, containing words for each difficulty.
* Huge performance gains for word search. In worst case scenarios, the search time would last up to 15 seconds. Now the searches are instant.
#### Changed
* Small part of code was rewritten and improved.

### [0.1.0] - 2019-01-08
#### Added
* Some performance improvements.
* Beep sounds when the player wins or loses.
#### Changed
* Code was rewritten and rearranged.
* Major improvements in the code.
#### Fixed
* Fixed minor bugs.
#### Removed
* Portuguese words.

### [0.0.7] - 2018-07-09
#### Added
* Language menu.
#### Changed
* Language changed from Portuguese to English.
* Improvements in the difficulty selection.
* Header is now more compact.
* Minor improvements in the code.

### [0.0.6] - 2018-05-13
#### Fixed
* Fixed a bug that apostrophe is not showed correctly.
* Fixed a bug that in some cases the number of letters are not correctly shown. 
#### Changed
* Minor improvements in the code.

### [0.0.5] - 2018-05-10
#### Removed
* Music playback.
#### Changed
* Minor improvements in the code.

### [0.0.4] - 2018-02-24
#### Fixed
* Fixed a bug that prints the hyphen where the letters entered by the player are.
#### Changed
* Victory and defeat messages.
* Minor improvements in the code.

### [0.0.3] - 2018-02-22
#### Added
* Music playback.
* Possibility to choose the level of difficulty.
#### Changed
* Number of lives reduced to six.
* Minor improvements in the code.

### [0.0.2] - 2018-02-21
#### Fixed
* Fixed a bug that allows multiple characters to be entered at the same time.
#### Changed
* Minor improvements in the code.

### [0.0.1] - 2018-02-20
#### Added
* First version of the game.
