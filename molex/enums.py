from enum import Enum


class ArtistRole(Enum):
    VOLCALIST = 'VOCALIST'
    LYRICIST = 'LYRICIST'
    PRODUCER = 'PRODUCER'
    REMIXER = 'REMIXER'
    ARTIST = 'ARTIST'

    @classmethod
    def is_role(cls, role):
        if isinstance(role, cls):
            role=role.value
        if not role in cls.__members__:
            return False
        else:
            return True


class SongSection(Enum):
    MUSIC = 'MUSIC' # Entire length of music; can be used for gapless playback
    INTRO = 'INTRO'
    VERSE = 'VERSE'
    PRE_CHORUS = 'PRE_CHORUS'
    CHORUS = 'CHORUS'
    HOOK = 'HOOK'
    REFRAIN = 'REFRAIN'
    BREAK = 'BREAK'
    SOLO = 'SOLO'
    BRIDGE = 'BRIDGE'
    OUTRO = 'OUTRO'


class LyricType(Enum):
    OTHER = 0
    STATIC_LYRICS = 1
    LINE_TIMED_LYRICS = 2
    WORD_TIMED_LYRICS = 3
    SYLLABLE_TIMED_LYRICS = 4
    TRIVIA_POP_UP_INFO = 5
    CHORD = 6

