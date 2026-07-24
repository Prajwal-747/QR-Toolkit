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
        self.mainframe.grid_rowconfigure(0, weight =1)
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(1, weight=2)
        self.controlPanel = ctk.CTkFrame(
            self.mainframe,
            corner_radius=10
        )
        self.previewPanel = ctk.CTkFrame(
            self.mainframe,
            corner_radius=10
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
        self.controlPanel.grid(
            row=0,
            column=0,
            padx=(15,8),
            pady = 15,
            sticky="nsew"
        )
        self.previewPanel.grid(
            row=0,
            column=1,
            padx=(8,15),
            pady=8,
            sticky="nsew"
        )
        self.controlPanel.grid_columnconfigure(0, weight=1)
        self.generateLabel=ctk.CTkLabel(
            self.controlPanel,
            text="Generate QR",
            font=("Segoe UI", 22, "bold")
        )
        self.generateLabel.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20,10),
            sticky="w"
        )

        self.dataLabel=ctk.CTkLabel(
            self.controlPanel,
            text="Data"
        )
        self.dataLabel.grid(
            row=2,
            column=0,
            padx=20,
            sticky="w"
        )

        self.dataEntry = ctk.CTkEntry(
            self.controlPanel,
            placeholder_text="Enter Text or URL..."
        )

        self.dataEntry.grid(
            row=3,
            column=0,
            padx=20,
            pady=(5,15),
            sticky="ew"
        )

        self.fileLabel=ctk.CTkLabel(
            self.controlPanel,
            text="Filename"
        )
        self.fileLabel.grid(
            row=4,
            column=0,
            padx=20,
            sticky="w"
        )

        self.fileEntry = ctk.CTkEntry(
            self.controlPanel,
            placeholder_text="qr_code.png"
        )

        self.fileEntry.grid(
            row=5,
            column=0,
            padx=20,
            pady=(5,15),
            sticky="ew"
        )

        self.foregroundlabel = ctk.CTkLabel(
            self.controlPanel,
            text="Foreground Color"
        )
        self.foregroundlabel.grid(
            row=6,
            column=0,
            padx=20,
            sticky="w"
        )
        self.foregroundMenu = ctk.CTkOptionMenu(
            self.controlPanel,
            values=[
                "Black",
                "Blue",
                "Red",
                "Green",
                "Purple"
            ]
        )
        self.foregroundMenu.grid(
            row=7,
            column=0,
            padx=20,
            pady=(5,15),
            sticky="ew"
        )
        self.backgroundlabel = ctk.CTkLabel(
            self.controlPanel,
            text="Background Color"
        )
        self.backgroundlabel.grid(
            row=8,
            column=0,
            padx=20,
            sticky="w"
        )
        self.backgroundMenu = ctk.CTkOptionMenu(
            self.controlPanel,
            values=[
                "White",
                "Black",
                "Gray",
                "Yellow"
            ]
        )
        self.backgroundMenu.grid(
            row=9,
            column=0,
            padx=20,
            pady=(5,15),
            sticky="ew"
        )

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


