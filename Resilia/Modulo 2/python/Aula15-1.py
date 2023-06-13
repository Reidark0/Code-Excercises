class Livros():
    def __init__(self, livro, isbn):
        self.livro = livro
        self.isbn = isbn

    def get_livro(self):
        return self.livro
    
    def get_isbn(self):
        return self.isbn

class Ebook(Livros):
    def __init__(self, linkDownload):
        self.linkDownload = linkDownload

    def get_link(self):
        return self.linkDownload

livro1 = Ebook('google.com')
livro1.livro = 'em busca de um teatro pobre'
livro1.isbn = 1234566123


print(livro1.get_isbn(), livro1.get_livro(), livro1.get_link())