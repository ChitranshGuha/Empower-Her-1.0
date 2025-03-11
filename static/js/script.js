document.addEventListener('DOMContentLoaded', () => {
    const slide = document.querySelector('.carousel-slide');
    const images = document.querySelectorAll('.carousel-slide img');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    let counter = 0;
    const size = images[0].clientWidth;

    // Move the carousel to show the next image
    function moveToNextSlide() {
        if (counter >= images.length - 1) counter = -1;
        counter++;
        slide.style.transform = 'translateX(' + (-size * counter) + 'px)';
    }

    // Move the carousel to show the previous image
    function moveToPrevSlide() {
        if (counter <= 0) counter = images.length;
        counter--;
        slide.style.transform = 'translateX(' + (-size * counter) + 'px)';
    }

    // Auto-slide every 5 seconds
    let interval = setInterval(moveToNextSlide, 5000);

    // Event listeners for buttons
    nextBtn.addEventListener('click', () => {
        clearInterval(interval); // Reset interval on manual slide
        moveToNextSlide();
        interval = setInterval(moveToNextSlide, 5000); // Resume auto-slide
    });

    prevBtn.addEventListener('click', () => {
        clearInterval(interval); // Reset interval on manual slide
        moveToPrevSlide();
        interval = setInterval(moveToNextSlide, 5000); // Resume auto-slide
    });

    // Query submission handling
    document.getElementById("userinfo").addEventListener("submit", function(event) {
        event.preventDefault();
        
        // Get the user details
        const name = document.getElementById("username").value;
        const phone = document.getElementById("phone").value;
        const email = document.getElementById("email").value;
        const query = document.getElementById("query").value;

        // Simulate sending the details to the server (replace with real server call)
        alert("Details submitted. Name: " + name + ", Phone: " + phone + ", Email: " + email + ", Query: " + query);

        // Show the chat box
        document.getElementById("chatBox").style.display = "block";
    });

    // Chat message sending
    function sendMessage() {
        const input = document.getElementById("chatInput").value;
        if (input.trim() !== "") {
            // Append the user's message to the chat window
            const chatMessages = document.getElementById("chatMessages");
            const messageElement = document.createElement("p");
            messageElement.innerText = "You: " + input;
            chatMessages.appendChild(messageElement);

            // Clear the chat input
            document.getElementById("chatInput").value = "";

            // Simulate a response from customer service
            setTimeout(() => {
                const responseElement = document.createElement("p");
                responseElement.innerText = "Customer Service: We're looking into it!";
                chatMessages.appendChild(responseElement);
            }, 1000);
        }
    }

    function closeChat() {
        document.getElementById("chatBox").style.display = "none";
    }

    // Add event listener for the chat input
    document.getElementById('chatInput').addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
});
