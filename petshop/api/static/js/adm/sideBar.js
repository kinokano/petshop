// Função para determinar qual botão deve ficar ativo
function setActiveButton() {
    const currentPath = window.location.pathname;
    const buttonMap = {
        '/indexAdm/': 'inicio',
        '/agendamentos/': 'agendamentos',
        '/clientes/': 'clientes',
        '/relatorios/': 'relatorios'
    };

    // Remove a classe active de todos os botões
    document.querySelectorAll('.sidebar-button').forEach(btn => {
        btn.classList.remove('active');
    });

    // Encontra o botão correspondente à URL atual
    for (const [path, buttonId] of Object.entries(buttonMap)) {
        if (currentPath.startsWith(path)) {
            const button = document.getElementById(buttonId);
            if (button) {
                button.classList.add('active');
            }
            break;
        }
    }
}

// Configura os event listeners para os botões
function setupButtonListeners() {
    const buttons = {
        'inicio': '/indexAdm/',
        'agendamentos': '/agendamentos/',
        'clientes': '/clientes/',
        'relatorios': '/relatorios/'
    };

    for (const [id, path] of Object.entries(buttons)) {
        const button = document.getElementById(id);
        if (button) {
            button.addEventListener('click', function() {
                // Remove a classe active de todos os botões
                document.querySelectorAll('.sidebar-button').forEach(btn => {
                    btn.classList.remove('active');
                });
                // Adiciona a classe active ao botão clicado
                this.classList.add('active');
                // Navega para a página
                window.location.href = path;
            });
        }
    }
}

// Quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', () => {
    // Configura o botão ativo baseado na URL atual
    setActiveButton();
    
    // Configura os listeners de clique
    setupButtonListeners();
});

const inicio = document.getElementById('inicio');

inicio.addEventListener('click', function() {
    window.location.href = '/indexAdm/';
});

const agendamentos = document.getElementById('agendamentos');

agendamentos.addEventListener('click', function() {
    window.location.href = '/agendamentos/';
});

const clientes = document.getElementById('clientes');

clientes.addEventListener('click', function() {
    window.location.href = '/clientes/';
});

const relatorios = document.getElementById('relatorios');

relatorios.addEventListener('click', function() {
    window.location.href = '/relatorios/';    
});