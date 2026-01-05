// script.js


/* ======================== Função para mudar de tela no fluxo da aplicação ======================== */

function mudarTela(idTelaDestino) {
    // 1. Esconde TODAS as telas
    const telas = ['upload_screen', 'insights_screen', 'loading_screen', 'report_screen'];
    
    telas.forEach(id => {
        document.getElementById(id).classList.add('hidden');
    });

    // 2. Mostra SÓ a que queremos
    document.getElementById(idTelaDestino).classList.remove('hidden');
    
    // Opcional: Rolar para o topo
    window.scrollTo(0, 0);
}




/* ======================== Função para mostrar o nome do arquivo selecionado ======================== */
document.addEventListener('DOMContentLoaded', () => {
    // Selecionando os elementos
    const fileInput = document.getElementById('fileUpload');
    const fileNameContainer = document.getElementById('fileNameContainer');
    const fileNameDisplay = document.getElementById('fileNameDisplay');
    const removeFileBtn = document.getElementById('removeFileBtn');

    // Quando um arquivo é selecionado
    fileInput.addEventListener('change', function(event) {
        const file = event.target.files[0];

        if (file) {
            // Mostra o nome do arquivo
            fileNameDisplay.textContent = file.name;
            // Remove a classe 'hidden' para mostrar o container
            fileNameContainer.classList.remove('hidden');
        } else {
            resetFile();
        }
    });

    // Botãozinho "X" para remover o arquivo selecionado
    removeFileBtn.addEventListener('click', () => {
        resetFile();
    });

    // Função auxiliar para limpar o input
    function resetFile() {
        fileInput.value = ''; // Limpa o valor do input real
        fileNameContainer.classList.add('hidden'); // Esconde o container do nome
    }
});