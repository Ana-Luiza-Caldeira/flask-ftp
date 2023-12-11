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
    app.run(host='0.0.0.0',port=5000)