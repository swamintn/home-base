# .bashrc

# User specific aliases and functions

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# Aliases
# Common commands
alias h='history'
alias c='clear'
alias ls='ls -G'
alias ll='ls -lG'

# User prompt 
export PS1="\u-mbp \w> "

