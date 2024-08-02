from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple, Dict
from pathlib import Path

from enums import *


@dataclass
class Tag:
    name: str
    children: List = []


@dataclass
class Artist:
    name: str


@dataclass
class Lyric:
    type_:LyricType
    content: str
    source: str


@dataclass
class Audio():
    original_path: Path
    current_path: Path

@dataclass
class Image():
    type_: str

@dataclass
class Track():
    id_: str
    title: str
    alternate_titles: List[str]
    people: Dict[Artist:ArtistRole]
    release_date: datetime
    genre: list[str]
    playcount: int
    is_podcast: bool
    lyrics: dict[str:Lyric]

    initial_key: str
    bpm: int
    bitrate: str
    samplerate: str
    comment: str

    filesize: int

    tags: list[Tag]

    sections: dict[Tuple[int, int], SongSection] # {(start_time, end_time): SongSection}

    versions: List


@dataclass
class Album():
    title: str
    tracks: dict[Tuple[int, int]:Track] # (disc_number:track_number) : Track
    people: Dict[Artist:ArtistRole]

    feature: str # Special Version, Deluxe Version, etc.
    versions: List

    is_compilation: bool = False

@dataclass
class PlaylistItem:
    index: int
    date: datetime
    added_by: str
    track: Track

@dataclass
class AccessControlListItem():
    target: str
    read: bool
    add: bool
    update: bool
    delete: bool

@dataclass
class Playlist:
    id: str
    title: str
    source: str
    author: str
    items: List[PlaylistItem]

    acl: List[AccessControlListItem]


@dataclass
class Collection:
    pass
