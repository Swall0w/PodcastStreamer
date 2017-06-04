import feedparser
import vlc
import argparse
import sys
import time

def arg():
    parser = argparse.ArgumentParser(description='Simple Podcast Streamer.')
    parser.add_argument('--add','-a',type=str,help='Podcast URL')
    parser.add_argument('--list','-l',action='store_true',help='Podcast list')
    parser.add_argument('--delete','-d',type=int,help='delete podcast channel.')
    parser.add_argument('--detail',type=int,default=-1,help='podcast channel detail.')
    parser.add_argument('--play','-p',action='store_true',help='Podcast URL')
    parser.add_argument('--channel','-c',type=int,help='Podcast Channel that you want to listen.')
    parser.add_argument('--track','-t',type=int,help='Podcast tracl that you want to listen.')
    return parser.parse_args()

def converttime(millis):
    seconds = (millis/1000)%60
    minutes = (millis/(1000*60))%60
    hours = (millis/(1000*60*60))%24
    return hours, minutes, seconds

def stream(rss_url, track):
    rssdata = feedparser.parse(rss_url).entries[track]
#    print(rssdata.entries[track].keys())
#    print(rssdata.entries[track].summary)
    print(rssdata.summary)
    mp3_url = rssdata.media_content[0]['url']
    player = vlc.MediaPlayer(mp3_url)
    player.play()
#    print(total_time)
    while True:
        total_time = player.get_length()
        minutes, seconds = divmod(player.get_time()/1000, 60)
        hours, minutes = divmod(minutes, 60)
        #comment = '\r{0}  time: {1}:{2}:{3}'.format('playing...',player.get_time()/1000))
        comment = '\r{0}  time: {1}:{2}:{3}'.format('playing...', int(hours), int(minutes), int(seconds))
        sys.stdout.write(comment)
        sys.stdout.flush()
        time.sleep(0.1)

#    RSS_URL = 'http://feeds.feedburner.com/tabitabi-podcast/artlife'
#    news_dic = feedparser.parse(RSS_URL)
#    print(news_dic.feed.title)
#    print(news_dic.key)
#
#    for index, entry in enumerate(news_dic.entries):
#        title = entry.title
#        link  = entry.link
#        media = entry.media_content
#        if index == 0:
#            mp3_url = media[0]['url']
#            player = vlc.MediaPlayer(mp3_url)
#            player.play()
#            while True:
#                print('playing')
#                pass
##        filename = wget.download(mp3_url)

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
