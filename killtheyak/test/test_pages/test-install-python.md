title: Install Python 2 and 3
updated: 2013-07-07 00:00:00
os: [macosx]
deps: [test-install-homebrew]

## MacOSX 

Verified on MacOSX 10.7.

```bash
# Mac
## Install Python 2
$ brew install python
## Install Python 3
$ brew install python3
## Follow instructions that come up after each install
```

Be sure to follow any instructions that appear after the install. If you missed it, you can always see it again with `brew info python`.

If things are still aren't working, try to solve *every* issue that comes is listed when you run `brew doctor`.

```bash
# Is everything working?
$ brew doctor
# Listen to the doctor!
```

You now have both Python 2 *and* 3 installed.

```
# Use python 2
$ python 
# Use python 3
$ python
# Install a package for python 2
$ pip install package-name
# Install a package for python 3
$ pip3 install package-name
```
