let userID = localStorage.getItem('userID');
if (userID != null) {
    document.querySelector(".login-form").style.display = 'none';
    document.querySelector("#logout").style.display = 'flex';
} else {
    document.querySelector("#logout").style.display = 'none';
}

//------------------------------------------------------------------------------------------------------------

document.getElementById("error-popup-close").addEventListener('click', ()=> {
    document.getElementById("error-popup").style.display = 'none';
})

function errorPopup(strongText, errorText) {
    document.getElementById("error-popup-strong").innerText = strongText;
    document.getElementById("error-popup-text").innerText = errorText;
    document.getElementById("error-popup").style.display = 'block';
}

//------------------------------------------------------------------------------------------------------------

document.getElementById('login-to-register').addEventListener('click', (event) => {
    event.preventDefault();
    
    document.getElementById('register-username').style.border = "1px solid #ced4da";
    document.getElementById('register-username').placeholder = "";
    document.getElementById('register-username').value = null;
    
    document.getElementById('register-password').style.border = "1px solid #ced4da";
    document.getElementById('register-password').placeholder = "";
    document.getElementById('register-password').value = null;

    document.querySelector('.register-form').style.display = "block";
    document.querySelector('.login-form').style.display = "none";
    
    document.getElementById('error-popup').style.display = 'none';
})

document.getElementById('register-to-login').addEventListener('click', (event) => {
    event.preventDefault();
    document.getElementById('login-password').style.border = "1px solid #ced4da";
    document.getElementById('login-password').placeholder = "";
    document.getElementById('login-password').value = null
    
    document.getElementById('login-username').style.border = "1px solid #ced4da";
    document.getElementById('login-username').placeholder = "";
    document.getElementById('login-username').value = null
    
    document.querySelector('.register-form').style.display = "none";
    document.querySelector('.login-form').style.display = "block";
    
    document.getElementById('error-popup').style.display = 'none';
})

//------------------------------------------------------------------------------------------------------------
document.getElementById('login-username').addEventListener('click', () => {
    document.getElementById('login-username').style.border = "1px solid #ced4da";
})

document.getElementById('login-password').addEventListener('click', () => {
    document.getElementById('login-password').style.border = "1px solid #ced4da";
})

document.getElementById('login-submit').addEventListener('click', (event) => {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById("login-password").value;
    
    const jsonString = JSON.stringify({
        username: username,
        password: password,
    });
    
    console.log(jsonString)
    
    const requestOptions = {
        // mode: "no-cors",
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        body: jsonString
    };
    
    var passFlag = true;
    
    // login form input text check
    if (username.length === 0) {
        passFlag = false;
        let usernameInput = document.getElementById('login-username');
        usernameInput.placeholder = "Username cannot be empty"
        usernameInput.style.borderColor = "red";
        errorPopup("Login failed: ", "Username cannot be empty")
    }
    if (password.length === 0) {
        passFlag = false;
        let passwordInput = document.getElementById('login-password');
        passwordInput.placeholder = "Password cannot be empty"
        passwordInput.style.borderColor = "red";
        errorPopup("Login failed: ", "Password cannot be empty")
    }
    
    // Make a promise
    if (passFlag === true) {
        fetch('http://127.0.0.1:5000/v1/user/login', requestOptions).then((response) => {
            if (response.status === 404) {
                response.json().then((data) => {
                    errorPopup("Login failed: ", data['status']);
                });
            } else {
                response.json().then((data) => {
                    document.querySelector(".register-form").style.display = 'none';
                    document.querySelector(".login-form").style.display = 'none';
                    localStorage.setItem('username', data['username']);
                    localStorage.setItem('userID', data['userID']);
                    document.querySelector("#logout").style.display = 'block';
                });
            }
        })
    }
})

//------------------------------------------------------------------------------------------------------------

document.getElementById('register-username').addEventListener('click', () => {
    document.getElementById('register-username').style.border = "1px solid #ced4da";
})

document.getElementById('register-password').addEventListener('click', () => {
    document.getElementById('register-password').style.border = "1px solid #ced4da";
})

// register form submit
document.getElementById('register-submit').addEventListener('click', (event) => {
    document.getElementById("error-popup").style.display = "none";
    event.preventDefault();
    
    const username = document.getElementById("register-username").value;
    const password = document.getElementById('register-password').value;
    
    const jsonString = JSON.stringify({
        username: username,
        password: password,
    });
    
    const requestOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: jsonString
    };
    
    var passFlag = true;
    
    // register form input text check
    if (username.length === 0) {
        passFlag = false;
        let nameInput = document.getElementById('register-username');
        nameInput.placeholder = "username cannot be empty"
        nameInput.style.borderColor = "red";
        errorPopup("Register failed: ", "Please fill all fields.")
    }
    if (password.length === 0) {
        passFlag = false;
        let passwordInput = document.getElementById('register-password');
        passwordInput.placeholder = "Password cannot be empty"
        passwordInput.style.borderColor = "red";
        errorPopup("Register failed: ", "Please fill all fields.")
    } 
    
    if (passFlag === true) {
        fetch('http://127.0.0.1:5000/v1/user/register', requestOptions).then((response) => {
            if (response.status === 403) {
                response.json().then((data) => {
                    errorPopup("Register failed: ", data['status']);
                });
            } else if (response.status === 201) {
                response.json().then((data) => {
                    // display a login page for re-login with just registed account
                    document.querySelector(".register-form").style.display = 'none';
                    document.querySelector(".login-form").style.display = 'none';
                    localStorage.setItem('username', data['username']);
                    localStorage.setItem('userID', data['userID']);
                    document.querySelector("#logout").style.display = 'block';
                });
            }
        });
    }
})

//------------------------------------------------------------------------------------------------------------

document.getElementById('logout').addEventListener('click', () => {
    localStorage.clear();
    document.querySelector(".login-form").style.display = 'block';
    document.querySelector("#logout").style.display = 'none';
    
    document.getElementById('login-password').style.border = "1px solid #ced4da";
    document.getElementById('login-password').placeholder = "";
    document.getElementById('login-password').value = null
    
    document.getElementById('login-username').style.border = "1px solid #ced4da";
    document.getElementById('login-username').placeholder = "";
    document.getElementById('login-username').value = null
});