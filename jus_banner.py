#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jus_Banner - Interactive CLI ASCII Banner Creator
Author: Solo
Description:
  Interactive version that asks user for banner text, font, and color.
  Built for fun, aesthetic command-line banner creation.
"""

import os
import random
from pyfiglet import Figlet, FigletFont
from colorama import Fore, Style, init

# Initialize Colorama for colorized output
init(autoreset=True)

# Predefined color options
COLOR_OPTIONS = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE
}

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def list_fonts():
    """Display a list of available fonts."""
    fonts = FigletFont.getFonts()
    print(Fore.CYAN + "\nAvailable Fonts:\n" + "-"*30)
    for i, f in enumerate(fonts, start=1):
        print(f"{Fore.YELLOW}{i:>3}. {f}")
    print(Fore.CYAN + f"\nTotal Fonts: {len(fonts)}")
    print(Fore.GREEN + "Tip: You can copy any font name for your next input!")

def choose_font():
    """Ask user for font choice or show list if they don’t know."""
    fonts = FigletFont.getFonts()
    while True:
        font_name = input(Fore.CYAN + "\n🎨 Enter a font name (or type 'list' to see all fonts): ").strip().lower()
        if font_name == "list":
            list_fonts()
            continue
        elif font_name in fonts:
            return font_name
        elif font_name == "":
            random_font = random.choice(fonts)
            print(Fore.YELLOW + f"No input given — using random font: {random_font}")
            return random_font
        else:
            print(Fore.RED + "❌ Invalid font name. Try again or type 'list'.")

def choose_color():
    """Ask user for color preference."""
    print(Fore.CYAN + "\n🎨 Available Colors:")
    print(", ".join([Fore.YELLOW + c for c in COLOR_OPTIONS.keys()]))
    while True:
        color_choice = input(Fore.CYAN + "\nEnter color name (leave blank for random): ").strip().lower()
        if color_choice in COLOR_OPTIONS:
            return COLOR_OPTIONS[color_choice]
        elif color_choice == "":
            random_color = random.choice(list(COLOR_OPTIONS.values()))
            print(Fore.YELLOW + "Random color selected.")
            return random_color
        else:
            print(Fore.RED + "❌ Invalid color. Try again.")

def show_tool_banner():
    """Display Jus_Banner in random font and color."""
    # Select random font
    fonts = FigletFont.getFonts()
    font = random.choice(fonts)
    
    # Select random color
    color = random.choice(list(COLOR_OPTIONS.values()))
    
    # Render banner
    fig = Figlet(font=font)
    banner = fig.renderText("Jus_Banner")
    
    print(color + banner + Style.RESET_ALL)
    print(Fore.GREEN + f"✅ Font: {font} | Color: {[k for k, v in COLOR_OPTIONS.items() if v == color][0].title()}\n")

def create_banner():
    """Main logic to create and display banner."""
    clear_screen()
    
    # First, show the tool banner with random font and color
    show_tool_banner()
    
    print(Fore.GREEN + "✨ Welcome to Jus_Banner - Interactive CLI Banner Creator ✨")
    
    # Step 1: Get banner text
    text = input(Fore.CYAN + "\n📝 Enter the text for your banner (default: Jus_Banner): ").strip()
    if not text:
        text = "Jus_Banner"
    
    # Step 2: Font choice
    font = choose_font()
    
    # Step 3: Color choice
    color = choose_color()
    
    # Step 4: Render banner
    fig = Figlet(font=font)
    banner = fig.renderText(text)
    
    clear_screen()
    print(color + banner + Style.RESET_ALL)
    print(Fore.GREEN + f"\n✅ Displayed '{text}' using font '{font}'.\n")

if __name__ == "__main__":
    try:
        create_banner()
    except KeyboardInterrupt:
        print(Fore.RED + "\nExited by user. Goodbye! 👋")