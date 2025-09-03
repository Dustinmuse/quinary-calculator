# --- Simple theme (drop-in) ------------------------------------
APP_BG = "#0f1115"
CARD_BG = "#161a20"
BTN_BG = "#2a2f3a"
BTN_FG = "#e6e6e6"
BTN_HOVER = "#3a4150"
ACCENT = "#7dd3fc"
TEXT_MUTED = "#9aa3b2"
FONT_UI = ("Segoe UI", 11)  # pick any: ("Helvetica", 12), ("Arial", 12)


def apply_theme(root, display_label, buttons):
    # window + grid padding
    root.configure(bg=APP_BG)
    for i in range(5):
        root.grid_columnconfigure(i, pad=2)
    for i in range(5):
        root.grid_rowconfigure(i, pad=2)

    # display area
    display_label.configure(
        bg=CARD_BG,
        fg=ACCENT,
        font=("Segoe UI", 14, "bold"),
        anchor="w",
        padx=12,
        pady=10,
        relief="flat",
    )

    def style_button(b):
        b.configure(
            bg=BTN_BG,
            fg=BTN_FG,
            activebackground=BTN_HOVER,
            activeforeground=BTN_FG,
            bd=0,
            relief="flat",
            font=FONT_UI,
            highlightthickness=0,
            cursor="hand2",
        )
        b.bind("<Enter>", lambda e: b.configure(bg=BTN_HOVER))
        b.bind("<Leave>", lambda e: b.configure(bg=BTN_BG))

    for b in buttons:
        style_button(b)
