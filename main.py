import feedparser
import vlc
import argparse

def arg():
    parser = argparse.ArgumentParser(description='Simple Podcast Streamer.')
    parser.add_argument('--add','-a',type=str,help='Podcast URL')
    parser.add_argument('--list','-l',action='store_true',help='Podcast list')
    parser.add_argument('--delete','-d',type=int,help='delete podcast channel.')
    parser.add_argument('--detail',type=int,help='podcast channel detail.')
    parser.add_argument('--play','-p',action='store_true',help='Podcast URL')
    parser.add_argument('--channel','-c',type=int,help='Podcast Channel that you want to listen.')
    parser.add_argument('--track','-t',type=int,help='Podcast tracl that you want to listen.')
    return parser.parse_args()

def stream():
    RSS_URL = 'http://feeds.feedburner.com/tabitabi-podcast/artlife'
    news_dic = feedparser.parse(RSS_URL)
#    print(news_dic.feed.title)
#    print(news_dic.key)

    for index, entry in enumerate(news_dic.entries):
        title = entry.title
        link  = entry.link
        media = entry.media_content
        if index == 0:
            mp3_url = media[0]['url']
            player = vlc.MediaPlayer(mp3_url)
            player.play()
            while True:
                print('playing')
                pass
#        filename = wget.download(mp3_url)

def main():
    args = arg()

# Load Channels
    with open('.channels','r') as f:
        channels = [item.strip() for item in f.readlines()]
    
    if args.list:
        for index, channel in enumerate(channels):
            print(index, channel)


if __name__ == '__main__':
    main()
