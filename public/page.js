// Function to change background color every 2 seconds
function changeColor() {
    var colors = ['#ff0000', '#00ff00', '#0000ff']; // Array of colors
    var index = 0; // Initial color index

    // Function to change background color
    function updateColor() {
        document.getElementById('landing-page').style.backgroundColor = colors[index]; // Change background color
        index = (index + 1) % colors.length; // Move to next color
    }

    setInterval(updateColor, 2000); // Call updateColor every 2 seconds
}

// Call the function when the page is loaded
window.onload = changeColor;

// JavaScript function for HERWARE landing page

document.addEventListener("DOMContentLoaded", function() {
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Function to handle form submission
    function handleFormSubmit(event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Fetch form input values
        var name = document.getElementById("name").value;
        var email = document.getElementById("email").value;
        var message = document.getElementById("message").value;

        // Perform validation (for demonstration purposes only)
        if (name === "" || email === "" || message === "") {
            alert("Please fill in all fields.");
            return;
        }

        // Display a confirmation message (for demonstration purposes only)
        alert("Form submitted successfully!\nName: " + name + "\nEmail: " + email + "\nMessage: " + message);

        // You can perform further actions here, such as sending the form data to a server using AJAX
    }

    // Add event listener to the form submission
    document.getElementById("contact-form").addEventListener("submit", handleFormSubmit);
});
