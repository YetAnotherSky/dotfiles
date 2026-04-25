# [UPDATE !] dotfiles (. 📁)

- My Fedora i3 dotfiles (Nord Theme)

## Preview ✨:

<img width="1919" height="1078" alt="2026-03-28_22-53" src="https://github.com/user-attachments/assets/576f6eaa-0fea-457c-acae-00293101bd21" />

<img width="1919" height="1079" alt="2026-03-25_02-42" src="https://github.com/user-attachments/assets/86187573-e6ce-47ec-8f86-ec60dcd65f33" />

## Requirements ❗:
```picom, starship, xautolock, xinput (to list your input devices that would be used for i3 config file) , rofi, polybar, zathura, nvim, >= 0.11, ghostty, cava, JetBrainsMono and FiraCode Nerd Fonts```
 - Link for starship: https://starship.rs/
 - Links for Nerd Fonts:
     - https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/JetBrainsMono.zip
     - https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/FiraCode.zip
 - Link for NvChad: https://nvchad.com/docs/quickstart/install

## Installation :

  - Manual
  ```bash
        git clone https://github.com/0x01sky/dotfiles && cd dotfiles
        cp -r .config/{i3,rofi,polybar,ghostty,zathura,picom,cava} "$HOME/.config/"
  ```
  - Automated
   ```bash
        wget https://raw.githubusercontent.com/0x01sky/dotfiles/main/setup/setup.py
        python3 setup.py
   ```
   *Note* : if you wish to update the dotfiles using automated installation, you should keep the script !

**Enjoy : - )**
