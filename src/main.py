import customtkinter as ctk
from tkinter import filedialog
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
        self.controlTabs = ctk.CTkTabview(
            self.mainframe
        )
        self.controlTabs.add("Generate")
        self.controlTabs.add("Decode")
        self.generateTab = self.controlTabs.tab("Generate")
        self.decodeTab = self.controlTabs.tab("Decode")
        self.previewPanel = ctk.CTkFrame(
            self.mainframe,
            corner_radius=10
        )
        self.previewTitle = ctk.CTkLabel(
            self.previewPanel,
            text="Preview",
            font=("Segoe UI", 22, "bold")
        )
        self.previewTitle.pack(pady=20)
        self.previewLabel = ctk.CTkLabel(
            self.previewPanel,
            text="Generate a QR Code",
            width=350,
            height=350
        )
        self.previewLabel.pack(expand = True)
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
        self.controlTabs.grid(
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
        self.generateTab.grid_columnconfigure(0, weight=1)
        self.decodeTab.grid_columnconfigure(0, weight=1)
        self.generateLabel=ctk.CTkLabel(
            self.generateTab,
            text="Generate",
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
            self.generateTab,
            text="Data"
        )
        self.dataLabel.grid(
            row=2,
            column=0,
            padx=20,
            sticky="w"
        )

        self.dataEntry = ctk.CTkEntry(
            self.generateTab,
            placeholder_text="Enter Text or URL..."
        )

        self.dataEntry.grid(
            row=3,
            column=0,
            padx=20,
            pady=(5,15),
            sticky="ew"
        )

        self.foregroundlabel = ctk.CTkLabel(
            self.generateTab,
            text="Foreground Color"
        )
        self.foregroundlabel.grid(
            row=6,
            column=0,
            padx=20,
            sticky="w"
        )
        self.foregroundMenu = ctk.CTkOptionMenu(
            self.generateTab,
            values=[
                "black",
                "blue",
                "red",
                "green",
                "purple"
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
            self.generateTab,
            text="Background Color"
        )
        self.backgroundlabel.grid(
            row=8,
            column=0,
            padx=20,
            sticky="w"
        )
        self.backgroundMenu = ctk.CTkOptionMenu(
            self.generateTab,
            values=[
                "white",
                "black",
                "gray",
                "yellow"
            ]
        )
        self.backgroundMenu.grid(
            row=9,
            column=0,
            padx=20,
            pady=(5,20),
            sticky="ew"
        )
        self.generateButton = ctk.CTkButton(
            self.generateTab,
            text="Generatate QR",
            command=self.generateQR
        )
        self.saveButton = ctk.CTkButton(
            self.generateTab,
            text="Save QR",
            command=self.saveQR
        )
        self.generateButton.grid(
            row=10,
            column=0,
            padx=20,
            pady=(0,10),
            sticky="ew"
        )
        self.saveButton.grid(
            row=11,
            column=0,
            padx=20,
            sticky="ew"
        )
        self.decodeLabel = ctk.CTkLabel(
            self.decodeTab,
            text="Decode",
            font=("Segoe UI", 22, "bold")
        )
        self.decodeLabel.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20,10),
            sticky="w"
        )
        self.browseButton = ctk.CTkButton(
            self.decodeTab,
            text="Browse Image"
        )
        self.browseButton.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )
        self.resultTextbox = ctk.CTkTextbox(
            self.decodeTab,
            height=150
        )
        self.resultTextbox.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )
        self.copyButton = ctk.CTkButton(
            self.decodeTab,
            text="Copy Result"
        )
        self.copyButton.grid(
            row=3,
            column=0,
            padx=20,
            pady=10,
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

    def generateQR(self):
        data = self.dataEntry.get()
        fg=self.foregroundMenu.get()
        bg=self.backgroundMenu.get()

        image = generator.generateQR(data,fg,bg)
        self.currentQR = image
        image = image.convert("RGB")
        preview = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(300,300)
        )
        self.previewLabel.configure(
            image=preview,
            text=""
        )
        self.statusLabel.configure(
            text="Status: QR Code Generated Successfully"
        )
        self.previewLabel.image = preview
        
    def saveQR(self):
        if not hasattr(self, "currentQR"):
            self.statusLabel.configure(
                text="Status: Generate a QR code first."
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG Image", "*.png"),
                ("JPEG Image", "*.jpg"),
                ("All Files", "*.*")
            ],
            title="Save QR Code"
        )

        if file_path:
            self.currentQR.save(file_path)
            self.statusLabel.configure(
                text="Status: QR Code Saved Successfully"
            )

if __name__ == "__main__":
    app = QRToolkit()
    app.mainloop()


