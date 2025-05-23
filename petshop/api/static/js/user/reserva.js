document.addEventListener('DOMContentLoaded', () => {
    const telefoneInput = document.getElementById('telefone');

    telefoneInput.addEventListener('input', () => {
      let value = telefoneInput.value.replace(/\D/g, ''); // Remove tudo que não for dígito

      if (value.length > 11) value = value.slice(0, 11); // Limita a 11 dígitos

      if (value.length >= 2) {
        value = `(${value.slice(0, 2)}) ${value.slice(2)}`;
      }
      if (value.length >= 10) {
        value = value.replace(/(\(\d{2}\)\s\d{5})(\d{4})/, '$1-$2');
      }

      telefoneInput.value = value;
    });
  

    const dataInput = document.getElementById('data');
    const hoje = new Date();
    const yyyy = hoje.getFullYear();
    const mm = String(hoje.getMonth() + 1).padStart(2, '0');
    const dd = String(hoje.getDate()).padStart(2, '0');
    const dataMinima = `${yyyy}-${mm}-${dd}`;
    dataInput.setAttribute('min', dataMinima);

  const horariosContainer = document.getElementById('horariosContainer');
  const horariosDiv = document.getElementById('horarios');
  const horarioSelecionadoInput = document.getElementById('horarioSelecionado');

  
  
  dataInput.addEventListener('change', () => {
    const data = dataInput.value;
  
    // Faz uma requisição GET para a view do Django com a data
    fetch(`/reserva/?data=${data}`)
      .then(response => {
        if (!response.ok) {
          throw new Error("Erro ao buscar horários.");
        }
        return response.json();
      })
      .then(result => {
        const horarios = result.horarios;
  
        // Limpa os horários anteriores
        horariosDiv.innerHTML = "";
  
        if (horarios.length === 0) {
          horariosDiv.innerHTML = "<p class='text-danger'>Nenhum horário disponível para esta data.</p>";
          horariosContainer.style.display = "block";
          return;
        }
  
        // Adiciona os botões de horário
        horarios.forEach(hora => {
          const btn = document.createElement("button");
          btn.type = "button";
          btn.className = "btn btn-outline-primary";
          btn.textContent = hora;
          btn.onclick = () => {
            horariosDiv.querySelectorAll("button").forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            horarioSelecionadoInput.value = hora;
          };
          horariosDiv.appendChild(btn);
        });
  
        horariosContainer.style.display = "block";
      })
      .catch(error => {
        console.error(error);
        horariosDiv.innerHTML = "<p class='text-danger'>Erro ao carregar os horários.</p>";
        horariosContainer.style.display = "block";
      });
  });
  
  document.getElementById('form').addEventListener('submit', function (e) {
    const nome = document.getElementById('nome').value.trim();
    const telefone = document.getElementById('telefone').value.trim();
    const nome_animal = document.getElementById('nome_animal').value.trim();
    const especie = document.getElementById('especie').value;
    const porte = document.getElementById('porte').value;
    const data = document.getElementById('data').value;
    const horario = document.getElementById('horarioSelecionado').value;
    const tipo_servico = document.getElementById('tipo_servico').value;
    const telefoneValido = /^\(\d{2}\)\s\d{5}-\d{4}$/.test(telefone);
 

    if (!telefoneValido) {
      e.preventDefault();
      alert("Telefone inválido. Use o formato (99) 99999-9999.");
      return;
    }
  
    if (!nome || !telefone || !nome_animal || !especie || !porte || !data || !horario || !tipo_servico) {
      e.preventDefault();
      alert("Por favor, preencha todos os campos obrigatórios corretamente antes de agendar.");
      return;
      
    }


  
    // Se quiser redirecionar só após o backend responder com sucesso, faça isso no Django
  });
  
  
  

});