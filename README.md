# too-lazy-decrease-reading
A simple TL;DR service

## Building it locally

In order to build it locally for personal use, you need Docker installed.

Once you have Docker available on your system, you can run the following commands:

```
# clone the repository
$ git clone https://github.com/FenrirUnbound/too-lazy-decrease-reading

# enter into the folder so that it's your cwd
$ cd too-lazy-decrease-reading

# builds the UI
$ make docker-build-ui

# bakes the UI with the API & builds the whole app
$ make docker-build

# run it locally
$ make run
```
