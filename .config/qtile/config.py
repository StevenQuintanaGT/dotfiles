# Qtile COnfig mamalona de steven

import os
import subprocess
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

# Autostart

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

# Colors

bg = "#282a36"
blue = "#96CDFB"
cyan = "#89DCEB"
fg = "#d9e0ee"
gray = "#6E6C7E"
magenta = "#F5C2E7"
red = "#F28FAD"
yellow = "#FAE3B0"
purple = "#bd93f9"

# Apps

mod = "mod4"
terminal = "alacritty"
browser = "firefox"
menu = "rofi -show drun"
file_manager = "Thunar"

# Keys

keys = [

    # ---------------------Apps-----------------------

    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "m", lazy.spawn(menu)),

    # --------------------Utilities--------------------

    # Volume

    Key ([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key ([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness

    Key ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 50%-")),

    # Screenshot

     Key([], "Print", lazy.spawn("flameshot gui")),

    # ----------------------------- Window ----------------------------
    
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle Floating"),
    
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "w", lazy.window.kill()),

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split()),

    # ------------------------- Layouts -----------------------

    Key([mod], "Tab", lazy.next_layout()),

    # --------------------------- Qtile -----------------------------

    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

]

# Groups

groups = [Group(f"{i+1}", 
         label = "") 
         for i in range(6)
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

# Layouts


layout_theme = {
    "border_width": 3,
    "margin": 6,
    "border_focus": cyan,
}
layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.RatioTile(**layout_theme),
]

# Widgets

widget_defaults = dict(
    font="UbuntuMono Nerd Font Bold",
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                 widget.TextBox(
                    text="    ",
                    background = bg,
                    foreground = cyan,
                    padding = 0,
                    fontsize = 17,
                ),

                widget.Sep(
                    foreground = gray,
                    line_width = 9,
                    padding = 6,
                ),

                widget.GroupBox(
                    fontsize = 20,
                    active = cyan,
                    inactive = gray,
                    foreground = cyan,
                    rounded = False,
                    borderwidth = 2,
                    margin = 4,
                    padding = 5,
                    highlight_method = "line",
                    highlight_color = bg,
                    other_screen_border = gray,
                    other_current_screen_border = cyan,
                    this_current_screen_border = cyan,
                    this_screen_border = gray,
                ),

                   widget.Sep(
                    foreground = gray,
                    padding = 10,
                    size_percent=70,
                ),

                widget.WindowName(
                    foreground=fg,
                ),

                widget.Systray(icon_size=15),

                widget.Sep(
                    foreground=gray,
                    padding = 10,
                    size_percent=70,
                ),

                widget.Battery(
                    foreground=fg,
                    low_foreground=red,
                    low_percentage=0.3,
                    format="{char} {percent:2.0%}",
                    charge_char="",
                    discharge_char="",
                    full_char="",
                    unknown_char="",
                    empty_char="",
                ),

                widget.Sep(
                    foreground=gray,
                    padding = 6,
                    size_percent=70,
                ),

                widget.TextBox(
                    text="﬙",
                    background=bg,
                    foreground=cyan,
                    padding=0,
                    fontsize=17,
                ),

                 widget.Memory(
                    measure_mem='G',
                    fontsize = 14,
                    foreground = cyan,
                ),

                widget.Sep(
                    padding = 6,
                    line_width = 0,
                ),

                widget.CPU(
                    fontsize = 14,
                    foreground = magenta,
                ),

                widget.Sep(
                    foreground=gray,
                    padding = 6,
                    size_percent=70,
                ),

                widget.TextBox(
                    text=" ",
                    background=bg,
                    foreground=yellow,
                    padding=0,
                    fontsize=17,
                ),

                widget.PulseVolume(
                    foreground=fg,
                    background=bg,
                ),

                widget.Sep(
                    foreground=gray,
                    padding = 6,
                    size_percent=70,
                ),

                widget.TextBox(
                    text=" ",
                    background=bg,
                    foreground=blue,
                    padding=0,
                    fontsize=17,
                ),

                widget.Clock(
                    background=bg,
                    foreground=fg,
                    format="%b %d - %I:%M%p",
                ),

                widget.Sep(
                    foreground=gray,
                    padding = 6,
                    size_percent=70,
                ),          

                widget.QuickExit(
                    background=bg,
                    foreground=red,
                    default_text="   ",
                    fontsize = 18,
                ),

            ],
            30,
            background=bg,
            opacity=20,
            margin=[7, 10, -2, 10],
        ),
    ),
]


# Drag floating layouts

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
