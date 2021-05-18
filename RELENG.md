## Publishing a release
1. Bump version in `setup.py`
2. Build and upload package: `rm -f dist/* && python setup.py sdist bdist_wheel && twine check dist/* && twine upload dist/*`
3. Tag and upload release `git tag v<version>` and `git push --tags`
