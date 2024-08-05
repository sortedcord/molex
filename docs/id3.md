# New ID3 Tags

To preserve comptatibility with legacy music applications or those that do not support or follow the molex standard, there are several proprietary ID3 tags that will be appended to a music track file in addition to the default ones to serve molex's new features.

| Tag Name               | Type   | Description                                                                                                       | Example                                                             |
| ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| BPM                    | Int    | Average BPM across the entire length of the music                                                                 | Self-Explanatory                                                    |
| Molex:ID               | String | ID of the song corresponding to the one stored in the db                                                          | Self-Explanatory                                                    |
| Molex:Processed        | Bool   | A tag which is set to `True` if the said music file has been processed (or imported) in Molex successfully.       | Self-Explanatory                                                    |
| Molex:Alternate Titles | String | Alternative titles to music titles (For other languages and translations)                                         | `Title1;Title2;Title2`                                              |
| Molex:People           | String | List of people associated with the particular track. Role is specified with `::Role`                              | `John Doe::Lyricist;Jane Doe::Vocalist;SmithAB::Album Artist`       |
| Molex:Tags             | String | List of tags                                                                                                      | `Old Music; 2013 Road Trip`                                         |
| Molex:Playcount        | Int    | Number of times the track has been played                                                                         | 123                                                                 |
| Molex:Sections         | Dict   | Timestamps of the song separating it into different sections. Format: `HH:MM:SS.sss,HH:MM:SS.sss::<Section Name>` | `00:00:00.121,00:00:14:232::Intro;00:00:14.232,00:34:11.870::Verse` |
