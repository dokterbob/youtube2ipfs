# youtube2ipfs
Download videos from YouTube (and similar video platforms) and add them to IPFS.

Based on [youtube-dl](https://ytdl-org.github.io/youtube-dl/) and [py-ipfs-http-client](https://github.com/ipfs-shipyard/py-ipfs-http-client).

## Requirements
* [ffmpeg](https://www.ffmpeg.org/)
* [Python 3.8 or later](https://www.python.org/downloads/)
* [go-ipfs 0.7](https://dist.ipfs.io/go-ipfs/v0.7.0) (0.8 not yet supported by py-ipfs-http-client)

## Installation
```sh
pip install youtube2ipfs
```

## Usage
First, make sure you have an IPFS node running. Then:

```sh
youtube2ipfs -v https://www.youtube.com/watch?v=FHH6hIc2GyE
```

It accepts multiple URL's, as well as

## Workaround for using IPFS 0.8
Manually install a forked py-ipfs-http-client with go-ipfs version detection disabled:

```sh
pip install git+https://github.com/dokterbob/py-ipfs-http-client.git
```
