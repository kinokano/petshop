async function loginAdm(e){
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value

    console.log(username, password, csrf)

    const response = await apiRequest('/api/login/', 'POST', {username:username, password:password}, {'X-CSRFToken':csrf});

    console.log(response);

    if(response.status == 200)
    {
        console.log('logou');

        window.location.href = '/indexAdm/'
    }
    else{
        console.log('erro ao logar');
    }

}

document.getElementById('formLogin').addEventListener('submit', loginAdm);

