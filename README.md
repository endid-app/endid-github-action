# Endid GitHub Action

## Usage

Install [Endid](https://endid.app/) in your Slack workspace and obtain a token by typing 
`/endid` in a channel, or in a conversation with the Endid bot.

Endid is a simple Slack integration for developers with some basic APIs (Python, command-line, REST) to 
ping a Slack channel with a message when something has happened, such as a long-running 
task ending.

All you need is the channel token.

The token should be stored in a GitHub secret especially if your repo is public.

### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master

    - name: Notify via Endid

      uses: endid-app/endid-github-action@master

      with:
        token: ${{ secrets.endid_token }}
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `token`  | The Endid token for your Slack channel    |
| `message` _(optional)_  | A message to display in Slack    |

### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `response`  | Any text returned from Endid's API    |

## Examples

### Using the optional input

This is how to use the optional input.

```yaml
with:
  token: ${{ secrets.endid_token }}
  message: "The very important GitHub Action has completed"
```

