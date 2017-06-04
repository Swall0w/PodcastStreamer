import feedparser
import wget
import vlc

def main():
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

if __name__ == '__main__':
    main()
