<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Lion City Soundscapes Visualisation</h3>
<h4 align="center">(README.md is still being updated)</h4>

  <p align="left">
    A Django web application that visualises characteristic soundscapes of Singapore on an interactive Leaflet map. This project was done as part of my Final Year Project (FYP) Bachelor of Honours requirement at NTU and is part of the project 'Lion City Soundscapes'. This repository comprises of the code used to develop the web application and includes instructions to install the project locally. The web application has been deployed on Amazon EC2 and can be viewed live <a href="">here</a>. 
    <br />
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

- Python (version 3.11.0)
- Pip (22.3.1)
- Django
- LeafletJS
- OneMap
- Javascript
- HTML/CSS

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

To ensure that the project runs smoothly, please make sure you have the following dependencies installed on your system:

- **Python**: This project is built with Python version 3.11.0. You can download the latest version of Python from the <a href="python.org">official website</a>. To check if you have the correct version of Python installed, open a terminal or command prompt and run the following command:

  ```sh
  python --version
  ```

  This will display the installed version of Python. To ensure the project runs smoothly, please ensure your version of Python is 3.11.0 or newer.

- **Pip**: Pip is the package installer for Python. To check if you have pip installed, you may run the following command line in your terminal:

  ```sh
  pip --version
  ```

  This will display the installed version of Pip. To ensure the project runs smoothly, please ensure your version of Pip is 22.3.1 or newer.

- **Python Virtual Environment**: To install and set up the virtual environment, run the following command line in the termianal or command prompt:

  ```sh
  python -m pip install venv
  ```

- Django

  ```sh
  pip install django
  ```

- Django Virtual Enviornment
  ```sh
  pip install virtualenv
  ```
  <br>
  <br>

### Installation

This README.md is still being updated. **Please note that the installation instructions are written for Windows machines only.** Installation instructions for other OS will be updated in the future.

<br>
#### Step 1: Setting up and activating the Virtual Environment

Python virtual environments help to create an isolated environment for development, where you can install dependencies, and other required third-party packages. Once the Python virtual environment `venv` has been installed (refer to <a href="#prerequisites">project prerequisites</a>), create a new virtual environment called `env` with the following command line in your terminal:

```sh
python -m venv env
```

Next, activate the virtual environment with the following command:

```sh
env\Scripts\activate
```

We can now install Django within the virtual environment with the following line:

```sh
pip install django
```

<br>
#### Step 2: Installing the Project

Clone the repository by downloading it from https://github.com/nemopotatoes/Lion-City-Soundscapes-Visualisation, or enter the following command on a terminal (with git installed):

```sh
git clone https://github.com/ntudsp/Lion-City-Soundscapes-Visualisation.git
```

You may navigate to the project folder in the terminal, where `path/to/` is the directory of the folder:

```sh
cd path/to/Lion-City-Soundscapes-Visualisation
```

Install project dependencies in the project's directory with the following command (make sure you have pip installed for this step):

```sh
pip install -r requirements.txt
```

<br>
#### Step 3: Running the Project on a Local Server

You may run the project on a local server by entering the following line in the project directory `/path/to/Lion-City-Soundscapes-Visualisation`. Please make sure you have python installed for this step.

```sh
python manage.py runserver
```

The project can be viewed on your local server at http://127.0.0.1:8000/

<br>
#### Step 4: Stopping the Server

To stop the server, press `Ctrl`+`C` in your keyboard in the same terminal.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Define user requirements
- [x] Web Application Design
  - [x] User interface template
  - [x] Wireframes and storyboards
- [x] Set up Django project
- [x] Set up Leaflet interactive map
- [x] Finalise soundscape recordings (locations.csv)
- [x] AWS Deployment (EC2 Free Tier)
- [x] Other Pages (About, Resources, Recordings, Contact)
- [x] Testing

<p align="right">(<a href="#readme-top">back to top</a>)</p>
