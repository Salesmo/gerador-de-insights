from flask import Blueprint, render_template, request, jsonify, session
import os
import pandas as pd
import google.generativeai as genai

# 1. Criar o Blueprint
# 'main' é o nome interno dele.
bp = Blueprint('main', __name__)

# 2. Usar @bp em vez de @app
@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/validar_api', methods=['POST'])
def validar_api():
    dados = request.json
    chave = dados.get('api_key')
    
    try:
        # Validação simples
        genai.configure(api_key=chave)
        genai.list_models()
        
        # --- AQUI ESTÁ A MUDANÇA ---
        # Salvamos na sessão. Como configuramos 'filesystem',
        # o Python cria um arquivo na pasta /flask_session com essa chave dentro.
        # O usuário NUNCA vê essa chave, só recebe um cookie ID.
        session['api_key'] = chave
        
        return jsonify({"status": "ok", "mensagem": "API Key válida e salva com segurança!"})
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Chave inválida."}), 401