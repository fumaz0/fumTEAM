import customtkinter as ctk


ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class ClickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Clicker")
        self.geometry("600x450")

        
        self.score = 0
        self.click_power = 1
        self.auto_click_speed = 0
        self.power_cost = 10
        self.auto_cost = 50

        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        
        
        self.sidebar = ctk.CTkFrame(self, width=110, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        ctk.CTkLabel(self.sidebar, text="Вкладки", font=("Arial", 14, "bold")).pack(pady=15)

        
        self.create_tab("Главная", self.show_main)
        self.create_tab("Магазин", self.show_shop)
        self.create_tab("Настройки", self.show_settings)

        self.footer = ctk.CTkLabel(self.sidebar, text="fumTEAM", font=("Arial", 10, "italic"), text_color="gray")
        self.footer.pack(side="bottom", pady=10)

        
        self.main_frame = self.setup_main_frame()
        self.shop_frame = self.setup_shop_frame()
        self.settings_frame = self.setup_settings_frame()

        self.show_main()
        self.update_auto_click()

    def create_tab(self, text, command):
        btn = ctk.CTkButton(self.sidebar, text=text, command=command,
                            fg_color="transparent", 
                            text_color=("black", "white"), # Черный в светлой, белый в темной
                            hover_color=("gray85", "gray25"),
                            anchor="center", height=35, corner_radius=5)
        btn.pack(pady=5, padx=5, fill="x")

    def setup_main_frame(self):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        self.label_score = ctk.CTkLabel(frame, text=f"{self.score} ", font=("Arial", 36, "bold"))
        self.label_score.pack(pady=(40, 20))

        
        self.click_btn = ctk.CTkButton(frame, text="", width=160, height=160, 
                                        corner_radius=80, command=self.on_click)
        self.click_btn.pack(pady=20)

        self.info_label = ctk.CTkLabel(frame, text=f"Клик: +{self.click_power} | Авто: {self.auto_click_speed}/с", font=("Arial", 13))
        self.info_label.pack(pady=10)
        return frame

    def setup_shop_frame(self):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(frame, text="Магазин", font=("Arial", 20, "bold")).pack(pady=20)
        
        self.btn_buy_p = ctk.CTkButton(frame, text=f"Сила (+1) — {self.power_cost} ", command=self.buy_power, width=220)
        self.btn_buy_p.pack(pady=10)
        
        self.btn_buy_a = ctk.CTkButton(frame, text=f"Авто (+1) — {self.auto_cost} ", command=self.buy_auto, width=220)
        self.btn_buy_a.pack(pady=10)
        return frame

    def setup_settings_frame(self):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(frame, text="Настройки", font=("Arial", 20, "bold")).pack(pady=20)
        
        
        self.mode_menu = ctk.CTkOptionMenu(frame, values=["Темная", "Светлая"], command=self.change_theme)
        self.mode_menu.pack(pady=10)
        self.mode_menu.set("Темная")
        return frame

    def change_theme(self, new_theme):
        ctk.set_appearance_mode(new_theme)

    
    def show_main(self): self.switch(self.main_frame)
    def show_shop(self): self.switch(self.shop_frame)
    def show_settings(self): self.switch(self.settings_frame)

    def switch(self, target_frame):
        for f in [self.main_frame, self.shop_frame, self.settings_frame]:
            f.grid_forget()
        target_frame.grid(row=0, column=1, sticky="nsew")

    
    def on_click(self):
        self.score += self.click_power
        self.update_ui()

    def buy_power(self):
        if self.score >= self.power_cost:
            self.score -= self.power_cost
            self.click_power += 1
            self.power_cost = int(self.power_cost * 1.5)
            self.update_ui()

    def buy_auto(self):
        if self.score >= self.auto_cost:
            self.score -= self.auto_cost
            self.auto_click_speed += 1
            self.auto_cost = int(self.auto_cost * 1.7)
            self.update_ui()

    def update_ui(self):
        self.label_score.configure(text=f"{self.score} ")
        self.info_label.configure(text=f"Клик: +{self.click_power} | Авто: {self.auto_click_speed}/с")
        self.btn_buy_p.configure(text=f"Сила (+1) — {self.power_cost} ")
        self.btn_buy_a.configure(text=f"Авто (+1) — {self.auto_cost} ")

    def update_auto_click(self):
        if self.auto_click_speed > 0:
            self.score += self.auto_click_speed
            self.update_ui()
        self.after(1000, self.update_auto_click)

if __name__ == "__main__":
    app = ClickerApp()
    app.mainloop()
