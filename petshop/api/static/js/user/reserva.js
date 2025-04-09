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
  });