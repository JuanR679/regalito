import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import random
import math

# ==========================
#  PERSONALIZA AQUÍ
# ==========================
TU_NOMBRE = "Juan"
NOMBRE_NOVIA = "victoria"

# Formato: "YYYY-MM-DD"
FECHA_ESPECIAL = "2026-03-09"  # Ej: aniversario/cumpleaños

TITULO_APP = f"Para {NOMBRE_NOVIA} 💖"

CARTA = f"""
Mi amor {NOMBRE_NOVIA},

Solo quería recordarte lo importante que eres para mí.
Gracias por tu sonrisa, por tu compañía y por hacer mi vida mejor.

Eres mi lugar favorito.
Te amo hoy, mañana y siempre.

Con amor,
{TU_NOMBRE} 💘
""".strip()

RAZONES = [
    "Porque tu sonrisa me desarma.",
    "Porque contigo todo se siente más ligero.",
    "Porque me inspiras a ser mejor.",
    "Porque me haces sentir en casa.",
    "Porque tu forma de ver la vida es hermosa.",
    "Porque tus abrazos arreglan el mundo.",
    "Porque amo tus detalles y tu esencia.",
    "Porque amo tus mensajitos",
    "Porque amo tus celos.",
    "Porque amo tu boquita.",
    "Porque amo tus hermosos y brillantes ojitos.",
    "Porque amo tu todo tu cuerpo.",

]

CUMPLIDOS_RANDOM = [
    "Eres arte en forma de persona.",
    "Tu mirada tiene magia.",
    "Contigo, todo tiene sentido.",
    "Eres mi casualidad favorita.",
    "Tu risa es mi canción favorita.",
    "Eres increíble, nunca lo dudes.",
    "Eres arte para mis ojos.",
    "tu pintas mis dias de colores.",
]

# ==========================
#  APP
# ==========================

class RegaloApp:
    def __init__(self, root):
        self.root = root
        self.root.title(TITULO_APP)
        self.root.geometry("720x520")
        self.root.configure(bg="#12051a")
        self.root.resizable(False, False)

        # Canvas para fondo y corazones
        self.canvas = tk.Canvas(root, width=720, height=520, bg="#12051a", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.hearts = []
        self.animating = False

        self._draw_header()
        self._draw_buttons()
        self._draw_footer()

        # Animación suave de “brillitos” (puntitos)
        self.stars = []
        self._init_stars()
        self._animate_stars()

    def _draw_header(self):
        self.canvas.create_text(
            360, 55,
            text=f"💖 {NOMBRE_NOVIA}, esto es para ti 💖",
            fill="#ffb3ff",
            font=("Helvetica", 22, "bold")
        )
        self.canvas.create_text(
            360, 95,
            text="Un regalito digital hecho con amor en Python 🐍✨",
            fill="#f2d7ff",
            font=("Helvetica", 13)
        )

    def _draw_buttons(self):
        # Marco invisible para ubicar botones
        self.btn_frame = tk.Frame(self.root, bg="#12051a")
        self.btn_window = self.canvas.create_window(360, 260, window=self.btn_frame)

        style = dict(
            font=("Helvetica", 14, "bold"),
            width=22,
            pady=8,
            bg="#ff4da6",
            fg="white",
            activebackground="#ff80c1",
            activeforeground="white",
            relief="flat",
            cursor="hand2"
        )

        tk.Button(self.btn_frame, text="📜 Abrir la carta", command=self.mostrar_carta, **style).grid(row=0, column=0, pady=10)
        tk.Button(self.btn_frame, text="💗 Razones por las que te amo", command=self.mostrar_razones, **style).grid(row=1, column=0, pady=10)
        tk.Button(self.btn_frame, text="🎁 Sorpresa", command=self.sorpresa, **style).grid(row=2, column=0, pady=10)
        tk.Button(self.btn_frame, text="⏳ Cuenta regresiva", command=self.cuenta_regresiva, **style).grid(row=3, column=0, pady=10)

        # Botón extra: cumplido random
        tk.Button(
            self.btn_frame,
            text="✨ Dime algo bonito",
            command=self.cumplido_random,
            font=("Helvetica", 12, "bold"),
            width=22,
            pady=6,
            bg="#7c4dff",
            fg="white",
            activebackground="#9a7dff",
            relief="flat",
            cursor="hand2"
        ).grid(row=4, column=0, pady=14)

    def _draw_footer(self):
        self.footer_text = self.canvas.create_text(
            360, 485,
            text=f"Hecho con amor por {TU_NOMBRE} 💘",
            fill="#d4b3ff",
            font=("Helvetica", 12, "italic")
        )

    # ====== Funciones de botones ======

    def mostrar_carta(self):
        messagebox.showinfo("📜 Carta", CARTA)

    def mostrar_razones(self):
        razones_txt = "💗 Razones por las que te amo:\n\n"
        for i, r in enumerate(RAZONES, 1):
            razones_txt += f"{i}. {r}\n"
        messagebox.showinfo("💗 Razones", razones_txt)

    def cumplido_random(self):
        messagebox.showinfo("✨ Para ti", random.choice(CUMPLIDOS_RANDOM))

    def cuenta_regresiva(self):
        try:
            target = datetime.strptime(FECHA_ESPECIAL, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "FECHA_ESPECIAL debe tener formato YYYY-MM-DD (por ejemplo 2026-05-20).")
            return

        ahora = datetime.now()
        if target < ahora:
            messagebox.showinfo("⏳ Cuenta regresiva", "¡La fecha ya pasó! 💖\nPero el amor sigue.")
            return

        diff = target - ahora
        dias = diff.days
        horas = diff.seconds // 3600
        minutos = (diff.seconds % 3600) // 60

        msg = (
            f"Faltan:\n\n"
            f"🗓️ {dias} días\n"
            f"🕒 {horas} horas\n"
            f"⏱️ {minutos} minutos\n\n"
            f"para nuestra fecha especial 💞"
        )
        messagebox.showinfo("⏳ Cuenta regresiva", msg)

    def sorpresa(self):
        if not self.animating:
            self.animating = True
            self._spawn_hearts()
            self._animate_hearts()
            self.root.bell()  # sonido básico
            messagebox.showinfo("🎁 Sorpresa", f"{NOMBRE_NOVIA}, te elijo a ti. Siempre. 💘")
        else:
            messagebox.showinfo("🎁 Sorpresa", "¡La sorpresa ya está en marcha! Mira los corazones 💖")

    # ====== Estrellitas (fondo) ======

    def _init_stars(self):
        for _ in range(40):
            x = random.randint(0, 720)
            y = random.randint(0, 520)
            r = random.randint(1, 2)
            star = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="#ffffff", outline="")
            self.stars.append((star, random.choice([-1, 1])))

    def _animate_stars(self):
        # Parpadeo suave
        for star, direction in self.stars:
            current = self.canvas.itemcget(star, "fill")
            # alterna entre dos colores
            new_color = "#ffe6ff" if current == "#ffffff" else "#ffffff"
            self.canvas.itemconfig(star, fill=new_color)

        self.root.after(900, self._animate_stars)

    # ====== Corazones animados ======

    def _spawn_hearts(self):
        # Genera un grupo inicial de corazones
        for _ in range(18):
            x = random.randint(40, 680)
            y = random.randint(300, 500)
            size = random.randint(14, 26)
            speed = random.uniform(1.2, 2.6)
            drift = random.uniform(-1.0, 1.0)
            color = random.choice(["#ff4da6", "#ff80c1", "#ffb3ff", "#ff66cc"])
            heart_id = self._create_heart(x, y, size, color)
            self.hearts.append({
                "id": heart_id,
                "x": x,
                "y": y,
                "size": size,
                "speed": speed,
                "drift": drift,
                "phase": random.uniform(0, math.pi * 2)
            })

    def _create_heart(self, x, y, s, color):
        # Corazón simple con 2 círculos + triángulo
        r = s * 0.35
        left = self.canvas.create_oval(x - s*0.5, y - s*0.25, x - s*0.1, y + s*0.15, fill=color, outline="")
        right = self.canvas.create_oval(x + s*0.1, y - s*0.25, x + s*0.5, y + s*0.15, fill=color, outline="")
        tri = self.canvas.create_polygon(
            x - s*0.52, y,
            x + s*0.52, y,
            x, y + s*0.75,
            fill=color, outline=""
        )
        # Agrupa con tag común
        tag = f"heart_{left}"
        self.canvas.itemconfig(left, tags=(tag,))
        self.canvas.itemconfig(right, tags=(tag,))
        self.canvas.itemconfig(tri, tags=(tag,))
        return tag

    def _animate_hearts(self):
        if not self.animating:
            return

        # Mueve corazones hacia arriba con oscilación lateral
        for h in self.hearts:
            h["y"] -= h["speed"]
            h["phase"] += 0.15
            sway = math.sin(h["phase"]) * 1.6 + h["drift"]
            h["x"] += sway

            self.canvas.move(h["id"], sway, -h["speed"])

        # Elimina los que se fueron arriba y crea nuevos
        remaining = []
        for h in self.hearts:
            if h["y"] > -50:
                remaining.append(h)
            else:
                self.canvas.delete(h["id"])

        self.hearts = remaining

        if len(self.hearts) < 10:
            self._spawn_hearts()

        # Continúa animación
        self.root.after(30, self._animate_hearts)


def main():
    root = tk.Tk()
    app = RegaloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()