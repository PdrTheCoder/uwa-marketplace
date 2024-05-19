/* text button for toggle password visibility by switching between "Hide" and "Show" */
    function togglePasswordVisibility(id) {
        var passwordInput = document.getElementById(id);
        var toggleButton = document.getElementById(id + "-toggle");
        if (passwordInput.type === "password") {
            passwordInput.type = "text";
            toggleButton.textContent = "Hide";
        } else {
            passwordInput.type = "password";
            toggleButton.textContent = "Show";
        }
    }
