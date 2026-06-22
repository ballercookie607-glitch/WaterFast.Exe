import tkinter as tk
import random
import threading
import time

class WaterSplash:
    def __init__(self):
        self.splashes = []
        self.running = True
        
    def create_splash(self):
        """Create a random water splash window"""
        splash = tk.Tk()
        splash.attributes('-topmost', True)
        splash.attributes('-alpha', 0.8)
        
        # Random position
        x = random.randint(0, splash.winfo_screenwidth() - 100)
        y = random.randint(0, splash.winfo_screenheight() - 100)
        
        # Random size (100-300px)
        size = random.randint(100, 300)
        
        splash.geometry(f'{size}x{size}+{x}+{y}')
        splash.config(bg='#1E90FF')
        
        # Create canvas for water effect
        canvas = tk.Canvas(splash, bg='#1E90FF', highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Draw water circles
        center_x = size // 2
        center_y = size // 2
        for i in range(5, 0, -1):
            radius = (size // 2) * (i / 5)
            canvas.create_oval(
                center_x - radius, center_y - radius,
                center_x + radius, center_y + radius,
                outline='#00BFFF', width=2
            )
        
        # Add center circle
        canvas.create_oval(
            center_x - 10, center_y - 10,
            center_x + 10, center_y + 10,
            fill='#00BFFF'
        )
        
        # Auto-close after random duration
        duration = random.uniform(0.5, 2)
        splash.after(int(duration * 1000), splash.destroy)
        
        self.splashes.append(splash)

def main():
    # First warning
    root = tk.Tk()
    root.withdraw()
    
    from tkinter import messagebox
    
    result1 = messagebox.askyesno(
        "⚠️ Warning",
        "Are you sure you wanna run this app?"
    )
    
    if not result1:
        root.destroy()
        return
    
    # Second warning
    result2 = messagebox.askyesno(
        "⚠️ FINAL WARNING",
        "THIS IS YOUR LAST WARNING DO NOT OPEN IT"
    )
    
    if not result2:
        root.destroy()
        return
    
    root.destroy()
    
    # Start water splashes
    splash_app = WaterSplash()
    
    def splash_loop():
        while splash_app.running:
            splash_app.create_splash()
            time.sleep(random.uniform(0.2, 0.5))
    
    # Run splash loop in background thread
    splash_thread = threading.Thread(target=splash_loop, daemon=True)
    splash_thread.start()
    
    # Keep the app running
    main_window = tk.Tk()
    main_window.withdraw()
    main_window.title("WaterFast")
    
    main_window.mainloop()

if __name__ == "__main__":
    main()
