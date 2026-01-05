from flask import Flask
from flask_session import Session
import os
from .config import Config # Importa a classe que criamos no passo anterior

# Inicializamos a extensão Session (mas ainda não a ligamos ao app)
sess = Session()

def create_app():
    # Cria a instância do Flask
    app = Flask(__name__)

    # Carrega as configurações da Classe Config
    app.config.from_object(Config)

    # Garante que a pasta de uploads exista
    caminho_uploads = app.config['UPLOAD_FOLDER']
    os.makedirs(caminho_uploads, exist_ok=True)

    # Agora sim, ligamos a Sessão ao App configurado
    sess.init_app(app)

    # Importar e Registrar o Blueprint
    from .routes import bp 
    app.register_blueprint(bp) 
    
    return app