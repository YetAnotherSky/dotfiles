#!/bin/bash

# This Copies the config files to your config directory

set -e

CONFIG="$HOME/.config"
DOTFILES="$PWD/dotfiles"

cd "$DOTFILES"

install() {
  local src="$1"
  local dest="$2"

  mkdir -p "$dest"
  cp -r "$src"/. "$dest/"
}

install "i3" "$CONFIG/i3"
install "picom" "$CONFIG/picom"
install "ghostty" "$CONFIG/ghostty"
install "polybar" "$CONFIG/polybar"
install "fastfetch" "$CONFIG/fastfetch"
install "zathura" "$CONFIG/zathura"

mkdir -p "$HOME/Pictures/Wallpapers"
cp -r Wallpapers/. "$HOME/Pictures/Wallpapers/"

mkdir -p "$CONFIG"
cp starship.toml "$CONFIG/"

# Fonts Installation

cd ~/Downloads 
mkdir ~/.local/share/fonts
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/JetBrainsMono.zip"
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/FiraCode.zip"
unzip JetBrainsMono.zip -d JetBrainsMono && unzip FiraCode.zip -d FiraCode
cd JetBrainsMono && mv *.ttf ~/.local/share/fonts/
cd .. && cd FiraCode && mv *.ttf ~/.local/share/fonts/
fc-cache -fv

echo "[+] Your Dotfiles are installed, enjoy :-) !"
echo "[+] Adding more stuffs soon :-)"
