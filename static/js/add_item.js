document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("addItemForm");
    form.addEventListener('submit', function(e) {
        e.preventDefault(); 
        const formData = new FormData(form);

        fetch("/add", {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                // Show success message and update the link to view the new item
                const successMessage = document.getElementById("successMessage");
                successMessage.style.display = "block";
                console.log(successMessage.classList);
                console.log(successMessage.style.display);
                console.log(document.getElementById("viewNewItemLink"));
                const viewNewItemLink = document.getElementById("viewNewItemLink");
                viewNewItemLink.setAttribute("href", "/view/" + data.newItemId);
                viewNewItemLink.innerText = "See it here";
                form.querySelector("input").focus();
                form.reset();
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert("An error occurred while adding the item.");
        });
    });
});
