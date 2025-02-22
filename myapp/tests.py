{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Robothon 2.0</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Reset body and container margins and padding */
        body, .container-fluid {
            margin: 0;
            padding: 0;
            max-width: 100%;
            overflow-x: hidden;
        }

        /* Full-width header styling */
        .Header {
            background-color: black;
            padding: 10px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
        }
        .Header .logo-heading {
            display: flex;
            align-items: center;
        }
        .Header img {
            height: 50px;
            margin-right: 10px;
        }
        #heading {
            color: white;
            font-size: 2rem;
            margin: 0;
            text-shadow: 0 0 3px #000, 0 0 5px #000, 2px 2px 4px #000;
        }
        .Header_underline {
            background-color: red;
            height: 3px;
            width: 100%;
        }
        .button3 {
            background-color: black;
            border: 2px solid #000;
            color: white;
            padding: 10px 15px;
            font-size: 1rem;
            cursor: pointer;
            margin: 5px;
            border-radius: 2px;
        }
        .button3:hover, .active-button {
            background-color: red;
            color: white;
        }

        /* About Us Container Styling */
        .aboutus-container {
            border: 3px solid black;
            padding: 20px;
            border-radius: 10px;
            margin: 15px auto;
            background-color: #f9f9f9;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 100%;
        }
        .aboutusheading {
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(to bottom, #ff3300 0%, #663300 100%);
            -webkit-background-clip: text;
            color: transparent;
        }
        .aboutusparagraph {
            font-size: 1.25rem;
            line-height: 1.5;
            margin-bottom: 20px;
        }
        .join-button {
            background-color: red;
            color: white;
            padding: 10px 20px;
            font-size: 1rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .join-button:hover {
            transform: scale(1.1);
        }

        /* Overlay styling for the form popup */
        .overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            z-index: 1;
            align-items: center;
            justify-content: center;
        }

        /* Form container with smooth animation */
        .form-container {
            display: none;
            background-color: #fff;
            padding: 30px;
            border: 2px solid #333;
            border-radius: 10px;
            width: 90%;
            max-width: 500px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            transform: scale(0.9);
            opacity: 0;
            animation: zoomIn 0.5s forwards;
            text-align: center; /* Center content */
        }
        @keyframes zoomIn {
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        /* Close button styling */
        .close-btn {
            background: #ff3300;
            color: white;
            border: none;
            padding: 5px 10px;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
            position: absolute;
            top: 10px;
            right: 10px;
        }
        .close-btn:hover {
            background-color: #ff5733;
        }

        /* Additional styling for form fields */
        .form-group {
            margin-bottom: 15px; /* Space between fields */
            text-align: center; /* Align labels and inputs to center */
        }
        .form-control {
            width: 100%; /* Full-width inputs */
            padding: 10px; /* Inner padding */
            border: 1px solid #ccc; /* Border style */
            border-radius: 5px; /* Rounded corners */
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); /* Subtle shadow for inputs */
        }

        /* Aligning form elements */
        .form-group label {
            display: block; /* Make labels take the full width */
            margin-bottom: 5px; /* Space between label and input */
            font-weight: bold; /* Bold labels */
        }

        /* Confirmation message styling */
        .confirmation-message {
            display: none;
            margin-top: 20px;
            font-size: 1.25rem;
            color: green;
        }

        /* Responsive adjustments */
        @media (max-width: 576px) {
            #heading {
                font-size: 2rem;
            }
            .aboutusheading {
                font-size: 2rem;
            }
            .aboutusparagraph {
                font-size: 1rem;
            }
            .Header {
                flex-direction: column;
                align-items: center;
            }
            .Header nav {
                margin-top: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container-fluid p-0">
        <div class="Header">
            <!-- Logo and Heading -->
            <div class="logo-heading">
                <img src="{% static 'myapp/1727505199467.png' %}" alt="Robothon Logo" class="img-fluid">
                <h1 id="heading">ROBOTHON</h1>
            </div>
            <!-- Navigation Buttons -->
            <nav>
                <a href="{% url 'home' %}"><button class="button3 {% if request.path == '/' %}active-button{% endif %}">HOME</button></a>
                <a href="{% url 'competitions' %}"><button class="button3 {% if request.path == '/competitions/' %}active-button{% endif %}">COMPETITIONS</button></a>
                <a href="{% url 'aboutus' %}"><button class="button3 {% if request.path == '/aboutus/' %}active-button{% endif %}">ABOUT US</button></a>
            </nav>
        </div>
        <div class="Header_underline"></div>

        <!-- About Us Content -->
        <div class="aboutus-container">
            <h1 class="aboutusheading">Robothon 2.0</h1>
            <p class="aboutusparagraph">
                Robothon is an exciting annual robotics competition designed to inspire creativity, collaboration, and technical skills among students and enthusiasts.
                Join us for Robothon 2.0, where technology meets imagination, and creativity knows no bounds!
            </p>
            <button class="join-button" onclick="toggleForm()">Join Now</button>

            <!-- Overlay and form popup -->
            <div class="overlay" id="overlay">
                <div class="form-container" id="joinForm">
                    <button class="close-btn" onclick="toggleForm()">X</button>
                    <form id="submissionForm" method="POST">
                        {% csrf_token %}
                        
                        <div class="form-group">
                            {{ form.full_name.label_tag }} 
                            {{ form.full_name }} 
                        </div>

                        <div class="form-group">
                            {{ form.age.label_tag }} 
                            {{ form.age }} 
                        </div>

                        <div class="form-group">
                            {{ form.city.label_tag }} 
                            {{ form.city }} 
                        </div>

                        <div class="form-group">
                            {{ form.school_name.label_tag }} 
                            {{ form.school_name }} 
                        </div>

                        <div class="form-group">
                            {{ form.category.label_tag }} 
                            {{ form.category }} 
                        </div>

                        <button type="submit" class="join-button">Submit</button>
                    </form>
                    <!-- Confirmation Message -->
                    <div class="confirmation-message" id="confirmationMessage">Thank you for your submission!</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function toggleForm() {
            const overlay = document.getElementById("overlay");
            const form = document.getElementById("joinForm");
            overlay.style.display = overlay.style.display === "flex" ? "none" : "flex";
            form.style.display = form.style.display === "block" ? "none" : "block";
        }

        document.getElementById("submissionForm").addEventListener("submit", function(event) {
            event.preventDefault(); // Prevent default form submission
            
            // Hide the form
            const overlay = document.getElementById("overlay");
            const form = document.getElementById("joinForm");
            form.style.display = "none";

            // Show confirmation message
            const confirmationMessage = document.getElementById("confirmationMessage");
            confirmationMessage.style.display = "block";

            // Optional: You can add a timeout to hide the confirmation message after a few seconds
            setTimeout(() => {
                toggleForm(); // Hide the overlay after showing the message
            }, 3000); // Adjust the timeout duration as needed
        });
    </script>
</body>
</html>
