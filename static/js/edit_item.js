document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('editItemForm');
    const gameId = form.getAttribute('data-game-id');
    const discardButton = document.getElementById("discard-btn");

    form.addEventListener('submit', function(event) {
        event.preventDefault(); 

        const formData = new FormData(form);

        fetch(`/edit/${gameId}`, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                console.log(gameId);
                // Redirect to view the updated item
                window.location.href = `/view/${gameId}`;
            } else {
                alert('Error editing game data');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error editing game data');
        });
    });
    // Discard Changes Confirmation
    discardButton.addEventListener('click', function(event) {
        event.preventDefault(); 
        console.log("Lol");
    
        const userConfirmed = confirm("Are you sure you want to discard your changes?");
    
        if (userConfirmed) {
            window.location.href = `/view/${gameId}`;
        }
    });
});
