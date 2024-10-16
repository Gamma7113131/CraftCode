# scratch-translate-extension-languages
#### Languages used by the Scratch 3.0 Translate Extension

[![Build Status](https://travis-ci.com/LLK/scratch-translate-extension-languages.svg?token=Yfq2ryN1BwaxDME69Lnc&branch=master)](https://travis-ci.com/LLK/scratch-translate-extension-languages)

## Configuration
| Variable              | Default     | Required | Description                 |
| --------------------- | ----------- | -------- | --------------------------- |
| `GOOGLE_CLIENT_EMAIL` | `null`      | Yes      | Google authentication email |
| `GOOGLE_PRIVATE_KEY`  | `null`      | Yes      | Google authentication key   |

_Note that to properly format `GOOGLE_PRIVATE_KEY` in an environment variable,
newlines should be escaped properly:_

```bash
export GOOGLE_PRIVATE_KEY=$'-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----'
```

## Committing

This project uses [semantic release](https://github.com/semantic-release/semantic-release) to ensure version bumps
follow semver so that projects depending on it don't break unexpectedly.

In order to automatically determine version updates, semantic release expects commit messages to follow the
[conventional-changelog](https://github.com/bcoe/conventional-changelog-standard/blob/master/convention.md)
specification.

You can use the [commitizen CLI](https://github.com/commitizen/cz-cli) to make commits formatted in this way:

```bash
npm install -g commitizen@latest cz-conventional-changelog@latest
```

Now you're ready to make commits using `git cz`.
