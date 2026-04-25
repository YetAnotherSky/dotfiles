# If there is any issue regarding the script make sure to open an issue on https://github.com/0x01sky/dotfiles

import subprocess as sb
from pathlib import Path
import logging
import glob

logging.basicConfig(level=logging.INFO)
lg = logging.getLogger(__name__)

# Used Calligraphy to generate the ascii art

def Logo():
    print(r"""          

          
 ██████   █████                        █████    ██████████             █████       ██████   ███  ████                  
░░██████ ░░███                        ░░███    ░░███░░░░███           ░░███       ███░░███ ░░░  ░░███                  
 ░███░███ ░███   ██████  ████████   ███████     ░███   ░░███  ██████  ███████    ░███ ░░░  ████  ░███   ██████   █████ 
 ░███░░███░███  ███░░███░░███░░███ ███░░███     ░███    ░███ ███░░███░░░███░    ███████   ░░███  ░███  ███░░███ ███░░  
 ░███ ░░██████ ░███ ░███ ░███ ░░░ ░███ ░███     ░███    ░███░███ ░███  ░███    ░░░███░     ░███  ░███ ░███████ ░░█████ 
 ░███  ░░█████ ░███ ░███ ░███     ░███ ░███     ░███    ███ ░███ ░███  ░███ ███  ░███      ░███  ░███ ░███░░░   ░░░░███
 █████  ░░█████░░██████  █████    ░░████████    ██████████  ░░██████   ░░█████   █████     █████ █████░░██████  ██████ 
░░░░░    ░░░░░  ░░░░░░  ░░░░░      ░░░░░░░░    ░░░░░░░░░░    ░░░░░░     ░░░░░   ░░░░░     ░░░░░ ░░░░░  ░░░░░░  ░░░░░░  
                                                                                                                       
                                                                                                                       
                                                                                                                       
                                                                                                        Made By 0x01sky
          """)

# Packages listed to be installed

Packages = [
    "picom", "polybar", "neovim", "zathura",
    "brightnessctl", "xinput", "starship",
    "rofi", "fastfetch", "btop", "flameshot",
    "cava", "ghostty"
]

# Links for the nerd fonts and the dotfiles

links = [
    "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/JetBrainsMono.zip",
    "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/FiraCode.zip",
    "https://github.com/0x01sky/dotfiles"
]

files = ["JetBrainsMono.zip", "FiraCode.zip"]

home = Path.home()
fonts_dir = home / ".local/share/fonts"
downloads_dir = home / "Downloads/Fonts"
wallpapers_dir = home / "Pictures/Wallpapers"

def copr_ghostty():
    lg.info("Adding Ghostty copr repository..")
    sb.run(["sudo", "dnf", "copr", "enable", "scottames/ghostty"], check=True)

def inst():
    lg.info("Installing packages...")
    sb.run(["sudo", "dnf", "install", "-y", *Packages], check=True)

def setup_dirs():
    fonts_dir.mkdir(parents=True, exist_ok=True)
    downloads_dir.mkdir(parents=True, exist_ok=True)
    wallpapers_dir.mkdir(parents=True, exist_ok=True)

def download_fonts():
    sb.run(["wget", *links[:2]], cwd=downloads_dir, check=True)

def unzip_fonts():
    for f in files:
        sb.run(["unzip", f], cwd=downloads_dir, check=True)

def install_fonts():
    for font in glob.glob(str(downloads_dir / "*.ttf")):
        sb.run(["mv", font, str(fonts_dir)], check=True)

    sb.run(["fc-cache", "-fv"], check=True)

def clone_repo():
    sb.run(["git", "clone", links[2], str(home)], check=True)

def copy_configs():
    config_src = home / "dotfiles/config"
    
    for folder in ["polybar", "rofi", "zathura", "picom", "fastfetch", "cava"]:
        sb.run(["cp", "-r", str(config_src / folder), str(home / ".config")], check=True)

def main():
    Logo()
    copr_ghostty()
    inst()
    setup_dirs()
    download_fonts()
    unzip_fonts()
    install_fonts()
    clone_repo()
    copy_configs()

    lg.info("Setup complete!")

if __name__ == "__main__":
    main()
