import argparse
import logging

logger = logging.getLogger(__name__)

class Youtube2IPFS(object):
	def extract(self, url):
		logger.info("Processing %s", url)

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
	parser.add_argument('--verbose', '-v', action='count', default=0)

	args = parser.parse_args()

	setupLogging(args.verbose)

	yt2ipfs = Youtube2IPFS()

	for url in args.urls:
		yt2ipfs.extract(url)

if __name__ == "__main__":
    main()
