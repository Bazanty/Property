# Property Management System
The **Property Management System** is a comprehensive command-line application designed to help real estate agents efficiently manage properties, clients, rooms, and payments. Built using Python and SQLAlchemy, the system provides an easy-to-use interface for managing agents, properties, clients, and transactions.


# By Nyakundi Brian



## Table of Content
   * Project Overview

   * Features

   * structure

   * File Description

   * Installation

   * Tech stack

   * Usage

   * CLI Commands
  
   * Contributing

   * License




### **Overview**
  The **Property Management System** is a Python-based application designed to streamline property management for agents. 
  It provides an easy-to-navigate command-line interface (CLI) that allows agents to manage their properties, clients, rooms, and payments efficiently.
  The system uses **SQLite** for database storage and **SQLAlchemy** as an ORM to interact with the database.



### **Features**
   * **Agent Management**: Create and manage agents, including authentication and profile details.


   * **Property Management**: Add, update, delete, and list properties.

 
   * **Room Management**: Add rooms to properties, list rooms, and remove rooms as needed.


   * **Client Management**: Manage client information, link clients to properties, and handle client data.


   * **Payment Management**: Record and track payments made by clients for their rented properties.


   * **Search Functionality**: Easily search properties and clients by different criteria like name, address, etc.




### Project Structure


  ```python
   Property-Management-System/

   ├── property/

   │   ├── cli.py            # CLI commands and logic

   │   ├── database.py       # Database configuration and session management 
   
   │   ├── models.py         # SQLAlchemy models (Agent, Property, Client, etc.)

   │   ├── main.py           # Entry point for the application

   │   ├── requirements.txt  # Project dependencies

├── venv/                 # Virtual environment directory (usually excluded from version control)

├── property.db           # SQLite database file storing all the data

├── LICENSE               # Project license (e.g., MIT, Apache, GPL)

├── Pipfile               # Pipenv dependency management file

├── Pipfile.lock          # Lock file for Pipenv to ensure reproducible installs

└── README.md             # Project documentation
```

<<<<<<< HEAD
###### **File Descriptions**:
*cli.py: Contains the logic for handling command-line interface commands that interact with the user.

*database.py: Configures the connection to the **SQLite** database and handles session management using **SQLAlchemy**.

*models.py: Defines SQLAlchemy models representing agents, clients, properties, rooms, and payments.

*main.py: The main entry point for the application, where the execution of commands takes place.

*requirements.txt: Lists the necessary dependencies for running the project.

*property.db: SQLite database file where all data related to agents, properties, rooms, clients, and payments is stored.
=======


##### File Descriptions:
* cli.py: Contains the logic for handling command-line interface commands that interact with the user.

* database.py: Configures the connection to the **SQLite** database and handles session management using **SQLAlchemy**.

* models.py: Defines SQLAlchemy models representing agents, clients, properties, rooms, and payments.

* main.py: The main entry point for the application, where the execution of commands takes place.
>>>>>>> 66253998be1da9efbb700ba0f00f6f04466513ac

* requirements.txt: Lists the necessary dependencies for running the project.

* property.db: SQLite database file where all data related to agents, properties, rooms, clients, and payments is stored.
  
* LICENSE: The open-source license for the project, specifying how others can use and distribute the code.

* property.db: The SQLite database file storing all agent, client, property, room, and payment data.

* Pipfile: Manages the project’s dependencies using Pipenv.

* Pipfile.lock: Locks the dependencies to ensure that everyone is using the same versions.


### Technology Stack
This project is built using the following technologies:

**Backend**:
* [Python](https://www.python.org)(Programming language)
* [SQLAlchemy](https://www.python.org)(ORM for database interaction)
* [Click](https://www.python.org)(for creating CLI commands)

**Database**:
SQLite (used for local development, can be switched to PostgreSQL or MySQL for production)

**Authentication**:
bcrypt (for password hashing)

**Environment Management**:
Pipenv (for managing Python dependencies)


 #### Installation and Setup
 To get the **Property Management System** up and running, follow these steps:

 **Using Pip**

1.Create a Virtual Environmnet:

```python
python -m venv venv


2.Activate the virtual Env
* On Linux/macOS:

`source venv/bin/activate`

* On Windows:

`venv\Scripts\activate`


3.**Install Dependancies**: 

`pip install -r property/requirements.txt`


4. **Intialize the Database**:
5. 
`python property/database.py`


6. **Run the Application**

`python -m property.main`

```

   **Using Pipenv**
```python
1.**Install Pipenv**

`pip install pipenv`

2.**Install Dependancies:**
Pipfile:

`pipenv install`

3.**Activate the Virtual Environment**

`pipenv shell`

4.**Create the Database**:

`python property/database.py`

5.**Run the Application**:

`python -m property.main` 

```



  ### **Contribution**
We welcome contributions from anyone who wants to help improve the Property Management System. If you have ideas to solve real-world problems faced by property managers, agents, and clients, your input is highly valued.
Feel free to fork the repository, open issues, and submit pull requests. By contributing, you'll be making the system more powerful and helping property managers work more efficiently.



   **How to Contribute**
 ```python
1.Fork the repository.

2.Create a new branch 

`(git checkout -b feature-branch)`.

3.Make your changes.

4.Commit your changes `(git commit -am 'Add new feature')`.

5.Push to your branch `(git push origin feature-branch)`.

6.Open a pull request.
```



Thank you for your interest and contributions!





#### License
This project is licensed under the MIT License - see the [LICENSE] file for details.





#### Project URL
You can access the project repository and related resources at the following URL:

<<<<<<< HEAD
Project URL: https://github.com/Bazanty/Property
=======

Project URL:https://github.com/Bazanty/Property
>>>>>>> 66253998be1da9efbb700ba0f00f6f04466513ac













