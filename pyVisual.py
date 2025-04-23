#Trabalho de Python (Aprendizado de Máquina)- Professor: Marcelo Paiva
#Alunos: 
##  Julya Alfaiate - 2314290064
##  Yan Nogueira - 2314290122
##  Eduardo Castro - 


import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        valor = float(entrada_valor.get())
        dias = int(entrada_dias.get())

        taxa_anual = 0.1415
        taxa_diaria = (1 + taxa_anual) ** (1 / 365) - 1
        valor_bruto = valor * ((1 + taxa_diaria) ** dias)
        rendimento_bruto = valor_bruto - valor

        # IOF
        if dias < 30:
            tabela_iof = {
                1: 0.96, 2: 0.93, 3: 0.90, 4: 0.86, 5: 0.83,
                6: 0.80, 7: 0.76, 8: 0.73, 9: 0.70, 10: 0.66,
                11: 0.63, 12: 0.60, 13: 0.56, 14: 0.53, 15: 0.50,
                16: 0.46, 17: 0.43, 18: 0.40, 19: 0.36, 20: 0.33,
                21: 0.30, 22: 0.26, 23: 0.23, 24: 0.20, 25: 0.16,
                26: 0.13, 27: 0.10, 28: 0.06, 29: 0.03
            }
            iof = rendimento_bruto * tabela_iof.get(dias, 0.0)
        else:
            iof = 0.0

        rendimento_apos_iof = rendimento_bruto - iof

        # IR
        if dias <= 180:
            ir = rendimento_apos_iof * 0.225
        elif dias <= 360:
            ir = rendimento_apos_iof * 0.20
        elif dias <= 720:
            ir = rendimento_apos_iof * 0.175
        else:
            ir = rendimento_apos_iof * 0.15

        rendimento_liquido = rendimento_apos_iof - ir
        valor_total = valor + rendimento_liquido

        resultado = f"""
        Valor Investido: R$ {valor:.2f}
        Rendimento Bruto: R$ {rendimento_bruto:.2f}
        IOF: R$ {iof:.2f}
        IR: R$ {ir:.2f}
        Valor Final: R$ {valor_total:.2f}
        """
        messagebox.showinfo("Resultado da Simulação", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos.")

# Janela
janela = tk.Tk()
janela.title("Caixinha Super Cofrinho")

# Layout
tk.Label(janela, text="Valor a Investir (R$):").grid(row=0, column=0)
entrada_valor = tk.Entry(janela)
entrada_valor.grid(row=0, column=1)

tk.Label(janela, text="Tempo de aplicação (dias):").grid(row=1, column=0)
entrada_dias = tk.Entry(janela)
entrada_dias.grid(row=1, column=1)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=2, columnspan=2, pady=10)

janela.mainloop()
