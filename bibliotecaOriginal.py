import customtkinter
import requests
import customtkinter as tk
from tkinter import ttk


def pesquisar_livro():
    query = entry.get()
    url = "https://openlibrary.org/search.json?q=" + query
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        livros = data.get('docs', [])

        if livros:
            resultados.delete(*resultados.get_children())
            for livro in livros:
                titulo = livro.get('title', 'N/A')
                autores = ', '.join(livro.get('author_name', ['N/A']))
                ano_publicacao = livro.get('publish_date', 'N/A')
                isbn = livro.get('isbn', 'N/A')
                resultados.insert('', 'end', values=(titulo, autores, ano_publicacao, isbn[0]))
        else:
            resultados.delete(*resultados.get_children())
            resultados.insert('', 'end', values=("Nenhum resultado encontrado", "", "", ""))
    else:
        resultados.delete(*resultados.get_children())
        resultados.insert('', 'end', values=("Erro ao acessar a API", "", "", ""))


root = customtkinter.CTk()
root.title("Biblioteca")
root.geometry("1280x720")

entry = ttk.Entry(root, width=50)
entry.grid(row=0, column=0, padx=5, pady=5)

search_button = ttk.Button(root, text="Pesquisar", command=pesquisar_livro)
search_button.grid(row=0, column=1, padx=5, pady=5)

resultados = ttk.Treeview(root, columns=("Título", "Autores", "Ano de Publicação", "Número de Páginas"))
resultados.heading('#0', text='', anchor='center')
resultados.heading('#1', text='Título', anchor='center')
resultados.heading('#2', text='Autores', anchor='center')
resultados.heading('#3', text='Ano de Publicação', anchor='center')
resultados.heading('#4', text='ISBN', anchor='center')
resultados.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

resultados.column("#0", width=0, stretch=tk.NO)
resultados.column("#1", width=300, stretch=tk.NO)
resultados.column("#2", width=300, stretch=tk.NO)
resultados.column("#3", width=250, stretch=tk.NO)
resultados.column("#4", width=250, stretch=tk.NO)

root.mainloop()
