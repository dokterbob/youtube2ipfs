# youtube2ipfs
Download videos from YouTube (and similar video platforms) and add them to IPFS.

Based on [youtube-dl](https://ytdl-org.github.io/youtube-dl/) and [py-ipfs-http-client](https://github.com/ipfs-shipyard/py-ipfs-http-client).

## Requirements
* [ffmpeg](https://www.ffmpeg.org/)
* [Python 3.8 or later](https://www.python.org/downloads/)
* [go-ipfs 0.7](https://dist.ipfs.io/go-ipfs/v0.7.0) (0.8 not yet supported by py-ipfs-http-client)

## Installation
Latest published version:
```sh
$ pip install youtube2ipfs
```

Bleeding edge:
```sh
$ pip install git+https://github.com/dokterbob/youtube2ipfs
```

## Usage
First, make sure you have an IPFS node running. Then:

```sh
$ youtube2ipfs https://www.youtube.com/watch?v=FHH6hIc2GyE
QmaqcMNVRvet1ZfRFoEBkGaEVLHKTUtkgX3139gpPc1zve
```

It accepts multiple URL's, as well as channels and playlists. Multiple files will be added to the same top-level directory. Subtitles will also be downloaded and metadata is added to the video file.

For more details, use the `--verbose` or `-v` option (once or twice). A custom IPFS node can also be specified.
