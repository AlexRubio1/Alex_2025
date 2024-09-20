---
layout: page
title: About Alex Rubio
permalink: /Rubios_about/
---

> **The beginning of my coding journey**

The start of my journey was a little intense has I didn't know what I was for a little bit until the teacher and my dad helped me. Going on I started to try and use python to code animation and make intertaining games. Also w

> **My Sports Journey**

- My Sports Journey started with basketball when I was young, more about myself is that I love playing football and that it's my passion currently.

![Picture](DSC02532.jpeg)   



<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
div.scroll-container {
  background-color: #333;
  overflow: auto;
  white-space: nowrap;
  padding: 10px;
}

div.scroll-container img {
  padding: 10px;
}
</style>

<h2>Image Gallery of my sports journey and my family</h2>
<p>Use the horizontal scrollbar to see the other images.</p>

<div class="scroll-container">
  <img src="../images/about/Rubio.jpg" alt="Sports Beginning" width="350" height="400">
  <img src="../images/about/Rubio1.jpg" alt="Sports Beginning" width="350" height="400">
  <img src="../images/about/Rubio2.jpg" alt="Basketball at age 9" width="350" height="400">
  <img src="../images/about/Rubio3.jpg" alt="The beginning of football" width="600" height="400">
  <img src="../images/about/Rubio6.jpg" alt="Inseason football" width="500" height="400">
  <img src="../images/about/Rubio8.jpg" alt="Inseason football" width="300" height="400">
</div>



> **Fun Facts about me**

- I Started sports at a young age starting with basketball then going to football 🏈🏀

- I Lived in California my whole life while my parents lived in mexico for half their life 🇲🇽

- My hobbys are hanging out with my friends and family, playing videogames, and watching the nfl 🏈

- I love going to the beach, im very outgoing 🏖️

- I have 4 pets, 2 cats and 2 dogs 🐈🐶








<style>
    /* Style looks pretty compact, trace grid-container and grid-item in the code */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
    }
    .grid-item {
        text-align: center;
    }
    .grid-item img {
        width: 100%;
        height: 100px; /* Fixed height for uniformity */
        object-fit: contain; /* Ensure the image fits within the fixed height */
    }
    .grid-item p {
        margin: 5px 0; /* Add some margin for spacing */
    }
</style>

<!-- This grid_container class is for the CSS styling, the id is for JavaScript connection -->
<div class="grid-container" id="grid_container">
    <!-- content will be added here by JavaScript -->
</div>

<script>
    // 1. Make a connection to the HTML container defined in the HTML div
    var container = document.getElementById("grid_container"); // This container connects to the HTML div

    // 2. Define a JavaScript object for our http source and our data rows for the Living in the World grid
    var http_source = "https://upload.wikimedia.org/wikipedia/commons/";
    var living_in_the_world = [
        {"flag": "0/01/Flag_of_California.svg", "greeting": "Hey", "description": "California - forever"},
        {"flag": "f/fc/Flag_of_Mexico.svg", "greeting": "Hola", "description": "Mexico - My Enthiticty"},
    ]; 
    
    // 3a. Consider how to update style count for size of container
    // The grid-template-columns has been defined as dynamic with auto-fill and minmax

    // 3b. Build grid items inside of our container for each row of data
    for (const location of living_in_the_world) {
        // Create a "div" with "class grid-item" for each row
        var gridItem = document.createElement("div");
        gridItem.className = "grid-item";  // This class name connects the gridItem to the CSS style elements
        // Add "img" HTML tag for the flag
        var img = document.createElement("img");
        img.src = http_source + location.flag; // concatenate the source and flag
        img.alt = location.flag + " Flag"; // add alt text for accessibility

        // Add "p" HTML tag for the description
        var description = document.createElement("p");
        description.textContent = location.description; // extract the description

        // Add "p" HTML tag for the greeting
        var greeting = document.createElement("p");
        greeting.textContent = location.greeting;  // extract the greeting

        // Append img and p HTML tags to the grid item DIV
        gridItem.appendChild(img);
        gridItem.appendChild(description);
        gridItem.appendChild(greeting);

        // Append the grid item DIV to the container DIV
        container.appendChild(gridItem);
    }
</script>

<script src="https://utteranc.es/client.js"
        repo="AlexRubio1/Student_2025"
        issue-term="pathname"
        theme="icy-dark"
        crossorigin="anonymous"
        async>
</script>