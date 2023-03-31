<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Lion City Soundscapes</h3>

  <p align="center">
    An interactive map web application for characteristic soundscapes in Singapore
    <br />
    <a href="https://github.com/nemopotatoes/Lion-City-Soundscapes-Visualisation"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

### Built With

- Python
- Django
- LeafletJS
- OneMap
- Javascript
- HTML/CSS

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

Before setting up the project, make sure the following has been installed:

- Python

- Django

  ```sh
  pip install django
  ```

- Django Virtual Enviornment
  ```sh
  pip install virtualenv
  ```

### Installation

- Clone the repo:

  ```sh
  git clone https://github.com/nemopotatoes/Lion-City-Soundscapes-Visualisation.git
  ```

- Install project dependencies in your project directory:

  ```sh
  pip install -r requirements.txt
  ```

- Navigate to the cloned project directory 'lioncitysoundscapes' and create a new project by running the following: 
  ```sh
  django-admin startproject newproject
  ```

- Go to to `settings.py` in the new project and copy the `SECRET_KEY`

- Navigate to `settings.py` of the cloned project and paste your `SECRET_KEY`:

  ```py
  SECRET_KEY = 'ENTER YOUR SECRET_KEY'
  ```
  
- Run the Server:
  ```sh
  python manage.py runserver
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Set up Django project
- [x] Set up Leaflet interactive map
- [ ] Finalise soundscape recordings (locations.csv)
- [ ] AWS Integration 
- [ ] Other Pages: About, Resources, Recordings, Contact
- [ ] Admin Panel

<p align="right">(<a href="#readme-top">back to top</a>)</p>
