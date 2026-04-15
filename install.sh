#!/bin/bash
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

cd ~/Downloads 

wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/JetBrainsMono.zip"
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/FiraCode.zip"
fc-cache -fv

echo "[+] Your Dotfiles are installed, enjoy :-) !"
echo "[+] Adding more stuffs soon :-)"
