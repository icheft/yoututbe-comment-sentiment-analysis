import yt_downloader
SORT_BY_POPULAR = 0
SORT_BY_RECENT = 1

if __name__ == '__main__':
    youtubeID = 'OscqgBj1HCw'
    limit = 100
    sort = SORT_BY_POPULAR
    output = None  # do not write out files

    df = yt_downloader.comment.download_helper(youtubeID=youtubeID, limit=limit,
                                               language='en', sort=sort, output=output)
    print(df.head())
