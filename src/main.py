import customtkinter as ctk
import generator
import decoder

class QRToolkit(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QR Toolkit")
        self.geometry("900x600")
        self.minsize(800,500)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.topbar = ctk.CTkFrame(
            self,
            height=60,
            corner_radius=0
        )
        self.mainframe = ctk.CTkFrame(
            self
        )
        self.statusbar = ctk.CTkFrame(
            self,
            height=30,
            corner_radius=0
        )
        self.topbar.grid_propagate(False)
        self.statusbar.grid_propagate(False)
        self.topbar.grid(row=0,column=0,sticky="ew")
        self.mainframe.grid(row=1,column=0,sticky="nsew")
        self.statusbar.grid(row=2,column=0,sticky="ew")

        self.topbar.grid_columnconfigure(0, weight=1)
        self.titleLabel = ctk.CTkLabel(
            self.topbar,
            text="QR Toolkit",
            font=("Segoe UI", 24, "bold")
        )
        self.titleLabel.grid(
            row=0,
            column=0,
            padx=20,
            pady=15,
            sticky="w"
        )
        self.aboutButton = ctk.CTkButton(
            self.topbar,
            text="About",
            width=100
        )
        self.aboutButton.grid(
            row=0,
            column=1,
            padx=20,
            pady=10
        )

        self.statusLabel = ctk.CTkLabel(
            self.statusbar,
            text="Status: Ready",
            anchor="w"
        )
        self.statusLabel.pack(
            fill="x",
            padx=15,
            pady=5
        )

if __name__ == "__main__":
    app = QRToolkit()
    app.mainloop()


