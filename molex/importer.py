from tinytag import TinyTag
from main import ArtistRole, RoleDict, Tag, Artist, Track, Album
from utils import split_tag
from config import load_config

import re

def process_tags(tag_object: TinyTag):
    

    # Process titles
    titles = split_tag(tag_object.title, load_config().metadata.DELIMITERS['SONG_TITLE'])
    # Extract featured artist
    _featured_artists = []
    feat_patterns = [
        r"\(feat\. (.+?)\)", # for "Song Title (feat. Featured Artist)"
    ]
    for title in titles:
        for pattern in title:
            match = re.search(pattern, title)

            # Check if a match was found
            if match:
                result = match.group(1)
                print(result)
                _featured_artists.append(result)
    
    primary_title = titles[0]
    alternate_titles = titles[1:]

    # Process album
    album_name = tag_object.album





def import_track(file_path, audio_path, move=False):
    # Extract all id3 tags
    tags = TinyTag.get(file_path)
    # Process Metadata & add to db
    # Copy/Move it over to the audio_path
    pass

def edit_track(track:Track):
    pass