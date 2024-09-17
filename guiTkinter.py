import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Mi aplicación de escritorio")

# Crear una etiqueta
label = tk.Label(root, text="Hola, mundo!")
label.pack()

# Crear un botón para cerrar la aplicación
button = tk.Button(root, text="Cerrar", command=root.quit)
button.pack()

# Ejecutar la aplicación
root.mainloop()
