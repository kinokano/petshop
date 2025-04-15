document.querySelectorAll('.sidebar-button').forEach(button => {
    button.addEventListener('click', function() {
        document.querySelectorAll('.sidebar-button').forEach(btn => {
            btn.classList.remove('active');
        });
        this.classList.add('active');
    });
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