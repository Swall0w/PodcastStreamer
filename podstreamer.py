import feedparser
import vlc
import argparse
import sys
import time
import curses

def arg():
    parser = argparse.ArgumentParser(description='Simple Podcast Streamer.')
    parser.add_argument('--add','-a',type=str,help='Podcast URL')
    parser.add_argument('--list','-l',action='store_true',help='Podcast list')
    parser.add_argument('--delete','-d',type=int,help='delete podcast channel.')
    parser.add_argument('--detail',type=int,default=-1,help='podcast channel detail.')
    parser.add_argument('--play','-p',action='store_true',help='Podcast URL')
    parser.add_argument('--download',action='store_true',help='Podcast Download')
    parser.add_argument('--channel','-c',type=int,help='Podcast Channel that you want to listen.')
    parser.add_argument('--track','-t',type=int,help='Podcast tracl that you want to listen.')
    return parser.parse_args()

def converttime(times):
    minutes, seconds = divmod(times,60)
    hours, minutes = divmod(minutes, 60)
    return int(hours), int(minutes), int(seconds)

def stream(rss_url, track):
    rssdata = feedparser.parse(rss_url).entries[track]
    mp3_url = rssdata.media_content[0]['url']
    player = vlc.MediaPlayer(mp3_url)
    player.play()
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(1) 

    while True:
        try:
            if player.is_playing():
                status = 'playing...'
            else:
                status = 'pause...'

            key_input = stdscr.getch()
            if key_input == ord('k'):
                player.audio_set_volume(int(player.audio_get_volume()+10))
            elif key_input == ord('j'):
                player.audio_set_volume(int(player.audio_get_volume()-10))
            elif key_input == ord('l'):
                player.set_time(player.get_time()+10000)
            elif key_input == ord('h'):
                player.set_time(player.get_time()-10000)
            elif key_input == ord(' '):
                player.pause()

            elif key_input == ord('q'):
                curses.nocbreak()
                curses.echo()
                curses.endwin()
                sys.exit(0)
            else:
                pass

            hours, minutes, seconds = converttime(player.get_time()/1000)
            m_hours, m_minutes, m_seconds = converttime(player.get_length()/1000)
            comment = '\r{0}  time: {1:0>2}:{2:0>2}:{3:0>2} / {4:0>2}:{5:0>2}:{6:0>2}  volume:{7} key:{8}'.format(\
            status, hours, minutes, seconds, m_hours, m_minutes, m_seconds,player.audio_get_volume(),key_input
            )
            stdscr.addstr(0,0,rssdata.title)
            stdscr.addstr(1,0,comment)
            stdscr.refresh()
            time.sleep(0.1)
        except KeyboardInterrupt:
            curses.nocbreak()
            curses.echo()
            curses.endwin()


def detail(channel_url):
    rssdata = feedparser.parse(channel_url)
    for index, entry in enumerate(rssdata.entries):
        print(index, entry.title)

def main():
    args = arg()

# Load Channels
    with open('.channels','r') as f:
        channels = [item.strip() for item in f.readlines()]
    
    if args.list:
        for index, channel in enumerate(channels):
            print(index, channel)

    if args.detail >= 0:
        detail(channels[args.detail])

    if args.play:
        stream(channels[args.channel], args.track)


if __name__ == '__main__':
    main()
