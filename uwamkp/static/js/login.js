/* icon button for toggle password visibility by switching between fa-eye-slash and fa-eye */
function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var toggleIcon = document.getElementById("togglePasswordIcon");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleIcon.classList.remove("fa-eye-slash");
        toggleIcon.classList.add("fa-eye");
    } else {
        passwordInput.type = "password";
        toggleIcon.classList.remove("fa-eye");
        toggleIcon.classList.add("fa-eye-slash");
    }
}
