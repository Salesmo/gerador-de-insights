import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env (onde está a tua SECRET_KEY)
load_dotenv()

class Config:
    # 1. Chave Secreta: Usada para assinar o 'crachá' (cookie) do usuário.
    # O 'os.environ.get' tenta pegar do .env; se não achar, usa a string padrão (apenas para dev).
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CHAVE_SECRETA_PARA_DEV_1016'

    # 2. Tipo de Sessão: 'filesystem' diz para guardar os dados em ARQUIVOS no servidor,
    # em vez de guardar dentro do cookie do navegador.
    SESSION_TYPE = 'filesystem'
    
    # 3. Permanente?: False significa que se ele fechar o navegador, a sessão morre (segurança).
    SESSION_PERMANENT = False
    
    # 4. Use Signer: Adiciona uma camada extra de criptografia no ID da sessão.
    SESSION_USE_SIGNER = True
    
    # 5. Pasta da Sessão: Onde os arquivos temporários vão ficar.
    # O padrão é criar uma pasta 'flask_session' na raiz do projeto.
    SESSION_FILE_DIR = os.path.join(os.getcwd(), 'flask_session')
    
    # --- Configurações de Cookie (Segurança Extra) ---
    # Só envia cookie se tiver HTTPS? (True em produção, False no teu PC local)
    SESSION_COOKIE_SECURE = False 
    # Impede que JavaScript leia o cookie (protege contra hackers XSS)
    SESSION_COOKIE_HTTPONLY = True
    # Protege contra uso do site em iframes de terceiros
    SESSION_COOKIE_SAMESITE = 'Lax'

    # Define o caminho absoluto para a pasta uploads, na raiz do projeto (.../projeto/uploads)
    basedir = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(os.path.dirname(basedir), 'uploads')