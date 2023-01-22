from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#000000"),
                widget.Image(filename="~/.config/qtile/themeimgs/Places-start-here-arch-icon.png", margin=3, background="#000000", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}), 
                widget.Sep(padding=4, linewidth=0, background="#000000"), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                background="#000000"),  
                widget.Prompt(),
                widget.Spacer(length = 20),
                widget.WindowName(foreground='#99c0de',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
             
                widget.Systray(icon_size = 20),
                widget.TextBox(
                       text = ' ',
                       padding = 0,
                       fontsize = 28,
                       foreground='#000000'
                       ), 
                widget.Volume(
                       foreground='#ff3399'
                       ),
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#000000',
                       ),   
                widget.Net(
                       foreground ='#9f79ee',
                       padding = 0,
                       fontsize = 11,
                       ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#000000'
                       ),    
                widget.Clock(format=' %Y-%m-%d %a %I:%M %p',
                             background="#000000",
                             foreground='#9bd689'),
                                                widget.TextBox(                                                
                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#000000',
                       ),   
                widget.TextBox(
                    #text=''                    
                    text = '',
                    fontsize = 32,
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    #foreground='#e39378'
                    foreground='#e6f3ff'
                )
                
            ],
            30,  # height in px
            background='#000000'  # background color
        ), ),
]
