# err-discord - Discord utilities for Errbot

[![Build Status](https://travis-ci.org/Djiit/err-discord.svg?branch=master)](https://travis-ci.org/Djiit/err-discord) [![Coverage Status](https://coveralls.io/repos/github/Djiit/err-discord/badge.svg?branch=master)](https://coveralls.io/github/Djiit/err-discord?branch=master)

Err-discord is a plugin for [Err](https://github.com/gbin/err) that helps you use Discord as a backend. **It requires Python 3.6+**.

## Features

* Add `/discord/invite` webhook that redirects to Discord invitation link.
* Add `!discord` command that displays a Discord invitation link.

Have an idea ? Open an [issue](https://github.com/Djiit/err-discord/issues) or send me a [Pull Request](https://github.com/Djiit/err-discord/pulls).

## Usage

### Installation

As admin of an err chatbot, send the following command over XMPP:

```
!repos install https://github.com/Djiit/err-discord.git
```

### Commands

Use `!help Discord` to see the available commands and their explanation.

## Configuration

Send configuration commands through chat message to this plugins as in :

```
!plugin config Discord {'DISCORD_CLIENT_ID': 'your_client_id_here'}
```
