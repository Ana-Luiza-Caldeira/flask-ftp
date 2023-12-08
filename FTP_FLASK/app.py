from flask import Flask, render_template, request, send_file
import os
 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/buscar', methods=['POST'])
def buscar_arquivos():
    termo_busca = request.form.get('termo_busca', '')
 
    # Listar todos os arquivos PDF no diretório 'media'
    arquivos_encontrados = [f for f in os.listdir('media') if f.endswith('.pdf') and termo_busca.lower() in f.lower()]
 
    return render_template('index.html', arquivos_encontrados=arquivos_encontrados, termo_busca=termo_busca)
 
@app.route('/visualizar/<nome_arquivo>')
def visualizar_pdf(nome_arquivo):
    caminho_arquivo = os.path.join('media', nome_arquivo)
    return send_file(caminho_arquivo, mimetype='application/pdf')
 
if __name__ == '__main__':
    app.run(debug=True)



































# @app.route('/')
# def exibir_arquivo(caminho_arquivo_pdf = 'C:/Users/Usuário 14/Desktop/imagens/p3.pdf'):
#     # busca no servidor: caminho_arquivo_pdf

#     # Verifique se os arquivos existem
#     if os.path.exists(caminho_arquivo_pdf):
#         return render_template('index.html', caminho_pdf=caminho_arquivo_pdf)
#     else:
#         return 'Arquivos não encontrados!'
 
# @app.route('/pdf')
# def exibir_pdf():
#     return send_file('C:/Users/Usuário 14/Desktop/imagens/p3.pdf', mimetype='application/pdf')
 
# if __name__ == '__main__':
#     app.run(debug=True)