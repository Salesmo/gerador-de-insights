from app import create_app

# Cria a aplicação usando a fábrica que fizemos no __init__
app = create_app()

if __name__ == '__main__':
    # Roda o servidor
    app.run(debug=True)