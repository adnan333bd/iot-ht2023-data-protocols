# pyenv setup in ubuntu

apt update; apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash

### Load pyenv automatically by appending
### the following to
### ~/.bash_profile if it exists, otherwise ~/.profile (for login shells)
### and ~/.bashrc (for interactive shells) :

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

### Restart your shell for the changes to take effect.

### Load pyenv-virtualenv automatically by adding
### the following to ~/.bashrc:

eval "$(pyenv virtualenv-init -)"

source ~/.bashrc && exec $SHELL