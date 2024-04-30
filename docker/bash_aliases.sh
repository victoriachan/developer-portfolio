# This is copied to Docker wagtail user's ~/.bash_aliases file at build time
# Note: This file only loaded on dev container

alias dj="python manage.py"

# For nvm to work locally in docker container
if [ -a "$HOME/.nvm/nvm.sh" ]; then
  export NVM_DIR="$HOME/.nvm"
  source "$NVM_DIR/nvm.sh"
fi