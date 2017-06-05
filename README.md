# PodcastStreamer

This is a simple CLI podcast streamer in Python3.

## Attributes
* Stream Play
* Download

You can modify .channels file that contains URLs of RSS by your hands and --add, --delete.

## Demo
Streaming podcast

    python podstreamer.py --play --channel 0 --track 10

Download podcast

    python podstreamer.py --download --channel 0 --track 10

## Usage
while playing, you can use some keybinds. See below.

* k - volume 10 up
* j - volume 10 down
* l - Fast-Foward 10 sec 
* h - Rewind 10 sec 
* q - quit
* white space  - pause/play

There's a library warning when FF, RW, pause but it works well.


## Requirement
* python3.6
* feedparser
* vlc
* cursers
* wget

## Licence

[MIT](https://github.com/Swall0w/PodcastStreamer/blob/master/LICENSE)

## Author
[Swall0w](https://github.com/Swall0w)
