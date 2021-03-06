import argparse
import logging
import tempfile

import youtube_dl
import ipfshttpclient

logger = logging.getLogger(__name__)

class Youtube2IPFS(object):
	def __init__(self, tempdir, ipfsclient):
		self._tempdir = tempdir
		self._ipfsclient = ipfsclient

	def ipfs_add(self):
		nodes = self._ipfsclient.add(self._tempdir, recursive=True)
		for node in nodes:
			logger.info('Added %s as %s to IPFS', node['Name'], node['Hash'])

		# Return latest hash
		return nodes[-1]['Hash']

	def process(self, urls):
		logger.info("Processing %s", urls)

		def download_hook(d):
		    if d['status'] == 'error':
		    	logger.error('Error in download')
		    elif d['status'] == 'finished':
		        logger.info('Finished downloading %s', d['filename'])

		ydl_opts = {
		    'prefer_free_formats': True,
		    'logger': logger,
		    'progress_hooks': [download_hook],
		    'allsubtitles': True,
		    'writesubtitles': True,
		    'outtmpl': '{}/%(id)s-%(title)s/%(title)s.%(ext)s'.format(self._tempdir),
		    'restrictfilenames': True,
		    'format': 'best',
		    'postprocessors': [
			    {
			    	'key': 'FFmpegMetadata'
			    }
		    ],
		}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    result = ydl.download(urls)
		    if result != 0:
		    	logger.error('Error downloading, not adding to IPFS.')

		    return self.ipfs_add()

def setupLogging(verbose):
	logger.setLevel(logging.DEBUG)

	ch = logging.StreamHandler()

	if verbose == 0:
		ch.setLevel(logging.WARNING)
	if verbose == 1:
		ch.setLevel(logging.INFO)
	elif verbose >= 2:
		ch.setLevel(logging.DEBUG)

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)

	logger.addHandler(ch)

def main():
	parser = argparse.ArgumentParser(description='Download videos from YouTube (and similar video platforms) and add them to IPFS.')
	parser.add_argument('urls', metavar='urls', type=str, nargs='+',
	                    help='URLs of videos')
	parser.add_argument('--ipfs-address', type=str, default='/dns/localhost/tcp/5001/http', help='IPFS HTTP API (multiaddr, default: \'/dns/localhost/tcp/5001/http\')')
	parser.add_argument('--verbose', '-v', action='count', default=0)

	args = parser.parse_args()

	setupLogging(args.verbose)

	with ipfshttpclient.connect(args.ipfs_address) as ipfsclient:
		with tempfile.TemporaryDirectory() as tmpdirname:
			yt2ipfs = Youtube2IPFS(
				tempdir=tmpdirname,
				ipfsclient=ipfsclient
			)

			print(yt2ipfs.process(args.urls))

if __name__ == "__main__":
    main()
