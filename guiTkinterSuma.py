import tkinter as tk

# Función que se llama cuando el botón es presionado
def sumar():
    # Obtener los valores ingresados por el usuario
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    
    # Realizar la operación
    resultado = num1 + num2
    
    # Mostrar el resultado en la etiqueta
    result_label.config(text=f"Resultado: {resultado}")

# 1. Crear la ventana principal
root = tk.Tk()
# Establecer el tamaño inicial a 400x300 píxeles
#root.geometry("400x300")
root.geometry("400x300+200+100")
root.title("Sumadora")

# 2. Crear entradas de texto
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

# 3. Crear un botón que ejecutará la función `sumar`
sum_button = tk.Button(root, text="Sumar", command=sumar)
sum_button.pack()

# 4. Crear una etiqueta para mostrar el resultado
result_label = tk.Label(root, text="Resultado:")
result_label.pack()

# 5. Ejecutar el loop principal de Tkinter
root.mainloop()
