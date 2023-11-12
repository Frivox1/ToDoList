document.querySelectorAll('.edit-button').forEach(function(button) {
    button.addEventListener('click', function() {
        var form = button.parentElement;
        form.querySelector('.edit-input').style.display = 'inline';
        form.querySelector('.save-button').style.display = 'inline';
        button.style.display = 'none';
    });
});