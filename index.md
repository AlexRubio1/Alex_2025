---
layout: base
title: Rubio's Home 
description: Home
hide: true
---
{% include nav/home.html %}


<!--- Concatenation of site URL to frontmatter image  --->
{% assign sprite_file = site.baseurl | append: page.image %}
<!--- Has is a list variable containing mario metadata for sprite --->
{% assign hash = site.data.mario_metadata %}  
<!--- Size width/height of Sprit images --->
{% assign pixels = 256 %}

<!--- HTML for page contains <p> tag named "Mario" and class properties for a "sprite"  -->

<p id="mario" class="sprite"></p>
  
<!--- Embedded Cascading Style Sheet (CSS) rules, 
        define how HTML elements look 
--->

<!-- Hero Section -->
<header style="padding: 2rem; text-align: center; background: #222; color: white;">
  <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">Alex Rubio</h1>
  <p style="font-size: 1.2rem; max-width: 600px; margin: auto;">
    Full Stack Developer & CS Principles Enthusiast — focused on real-world impact, collaboration, and clean code.
  </p>
  <a href="/resume.pdf" target="_blank" style="display: inline-block; margin-top: 1rem; padding: 0.6rem 1.2rem; background: #4CAF50; color: white; border-radius: 10px; text-decoration: none;">📄 View My Resume</a>
</header>

<!-- About Section -->
<section style="padding: 2rem; max-width: 850px; margin: auto; line-height: 1.6; color: white;">
  <h2 style="color: white;">About Me</h2>

  <p>
    I'm a full-stack developer and student at Del Norte High School passionate about building real-world software. I’ve led backend development and deployment for projects with model integration, API configuration, and AWS readiness. My journey started in game dev with sprite animation on Roblox, and I now focus on scalable systems and collaborative coding.
  </p>

  <h3 style="color: white; margin-top: 1.5rem;">💻 Technical Skill Kit (TKS)</h3>
  <ul>
    <li><strong>Frontend Dev:</strong> HTML, CSS, JavaScript, Java; I design responsive interfaces and build interactive user experiences.</li>
    <li><strong>Backend Dev:</strong> Flask, SQLite, REST APIs; I structure server logic and connect data flow between front and backend cleanly.</li>
    <li><strong>Deployment Ops:</strong> Nginx, AWS, Git, CI/CD; I manage code shipping, server config, and cloud hosting pipelines.</li>
    <li><strong>Data Handling:</strong> DataTables, Model Integration, Server Config; I structure data pipelines and connect predictive models to APIs.</li>
    <li><strong>Projects:</strong> StudyBuddy, PowayData, DataScience, Draw.io Clone; all collaborative or open-source tools built to solve real problems.</li>
  </ul>
  <p><em>TKS: Code, Deploy, Scale</em></p>

  <h3 style="color: white; margin-top: 1.5rem;">🤝 Soft Skill Kit (SSK)</h3>
  <ul>
    <li><strong>Team Collaboration:</strong> Co-scrum of an Open Coding Society project, Co-founder of RobloxCoding; I work with peers to lead group projects and mentor younger coders.</li>
    <li><strong>Problem Solving:</strong> Debugging APIs, backend-to-model issues; I enjoy breaking down bugs and turning roadblocks into working features.</li>
    <li><strong>Initiative & Drive:</strong> Self-starter projects and GitHub repos; everything I build is open-source and designed to help students learn and collaborate.</li>
    <li><strong>Open Source Ethos:</strong> All code public to help student devs grow; I believe sharing work fuels innovation, especially in student communities.</li>
  </ul>
  <p><em>SSK: Lead, Solve, Share</em></p>
</section>

<style>

  /*CSS style rules for the id and class of the sprite...
  */
  .sprite {
    height: {{pixels}}px;
    width: {{pixels}}px;
    background-image: url('{{sprite_file}}');
    background-repeat: no-repeat;
  }

  /*background position of sprite element
  */
  #mario {
    background-position: calc({{animations[0].col}} * {{pixels}} * -1px) calc({{animations[0].row}} * {{pixels}}* -1px);
  }
</style>

<!--- Embedded executable code--->
<script>
  ////////// convert YML hash to javascript key:value objects /////////

  var mario_metadata = {}; //key, value object
  {% for key in hash %}  
  
  var key = "{{key | first}}"  //key
  var values = {} //values object
  values["row"] = {{key.row}}
  values["col"] = {{key.col}}
  values["frames"] = {{key.frames}}
  mario_metadata[key] = values; //key with values added

  {% endfor %}

  ////////// game object for player /////////

  class Mario {
    constructor(meta_data) {
      this.tID = null;  //capture setInterval() task ID
      this.positionX = 0;  // current position of sprite in X direction
      this.currentSpeed = 0;
      this.marioElement = document.getElementById("mario"); //HTML element of sprite
      this.pixels = {{pixels}}; //pixel offset of images in the sprite, set by liquid constant
      this.interval = 100; //animation time interval
      this.obj = meta_data;
      this.marioElement.style.position = "absolute";
    }

    animate(obj, speed) {
      let frame = 0;
      const row = obj.row * this.pixels;
      this.currentSpeed = speed;

      this.tID = setInterval(() => {
        const col = (frame + obj.col) * this.pixels;
        this.marioElement.style.backgroundPosition = `-${col}px -${row}px`;
        this.marioElement.style.left = `${this.positionX}px`;

        this.positionX += speed;
        frame = (frame + 1) % obj.frames;

        const viewportWidth = window.innerWidth;
        if (this.positionX > viewportWidth - this.pixels) {
          document.documentElement.scrollLeft = this.positionX - viewportWidth + this.pixels;
        }
      }, this.interval);
    }

    startWalking() {
      this.stopAnimate();
      this.animate(this.obj["Walk"], 3);
    }

    startRunning() {
      this.stopAnimate();
      this.animate(this.obj["Run1"], 6);
    }

    startPuffing() {
      this.stopAnimate();
      this.animate(this.obj["Puff"], 0);
    }

    startCheering() {
      this.stopAnimate();
      this.animate(this.obj["Cheer"], 0);
    }

    startFlipping() {
      this.stopAnimate();
      this.animate(this.obj["Flip"], 0);
    }

    startResting() {
      this.stopAnimate();
      this.animate(this.obj["Rest"], 0);
    }

    stopAnimate() {
      clearInterval(this.tID);
    }
  }

  const mario = new Mario(mario_metadata);

  ////////// event control /////////

  window.addEventListener("keydown", (event) => {
    if (event.key === "ArrowRight") {
      event.preventDefault();
      if (event.repeat) {
        mario.startCheering();
      } else {
        if (mario.currentSpeed === 0) {
          mario.startWalking();
        } else if (mario.currentSpeed === 3) {
          mario.startRunning();
        }
      }
    } else if (event.key === "ArrowLeft") {
      event.preventDefault();
      if (event.repeat) {
        mario.stopAnimate();
      } else {
        mario.startPuffing();
      }
    }
  });

  //touch events that enable animations
  window.addEventListener("touchstart", (event) => {
    event.preventDefault(); // prevent default browser action
    if (event.touches[0].clientX > window.innerWidth / 2) {
      // move right
      if (currentSpeed === 0) { // if at rest, go to walking
        mario.startWalking();
      } else if (currentSpeed === 3) { // if walking, go to running
        mario.startRunning();
      }
    } else {
      // move left
      mario.startPuffing();
    }
  });

  //stop animation on window blur
  window.addEventListener("blur", () => {
    mario.stopAnimate();
  });

  //start animation on window focus
  window.addEventListener("focus", () => {
     mario.startFlipping();
  });

  //start animation on page load or page refresh
  document.addEventListener("DOMContentLoaded", () => {
    // adjust sprite size for high pixel density devices
    const scale = window.devicePixelRatio;
    const sprite = document.querySelector(".sprite");
    sprite.style.transform = `scale(${0.2 * scale})`;
    mario.startResting();
  });

</script>