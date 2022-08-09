# Flask Introduction
___

## Table Of Contents
* What You Will Learn
* Useful Resources
  * Flask
    * What is a Framework?
    * What is a Web Application?
  * How to Install Flask?
    * To get Started.
  * Flask Application Structure
    * How does Flask display a page?

---

## What You will Learn
* Flask Basics

---

## Useful Resources
* [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing)
* `if __name__ == "__main__"`

---

## Flask
Flask is a Python web micro-framework designed to be a base for web applications.

### What is a Framework?
A framework is a set of modules that help programmers develop faster and easier.
These modules contain standard functionalities that handle low-layer tasks such as HTTP requests.

### What is a Web Application?
A web application is a standard website.
Well-known websites such as, Linkedin, Pinterest, Twilio, and Instagram were all built using the Flask framework.

---

## How To Install Flask?
`pip` is the essential way to install packages for python.

### To Get Started
1. Setup a virtual environment
2. From within the environment, use pip:
```bash
pip install flask
```
---

## Flask Application Structure
Flask is based on the MVC model.
MVC stands for Models-Views-Controller.
In this scenario, a user sends a request to enter a webpage by entering a URL.

* The Controller is the constructor; it receives the requests, assembles them, and sends an update to the Models.
* The Controller’s update: retrieves the necessary data from the Models, organizes it, and notifies the Controller of the packaged data.
* Once the Controller gets the Ok from the Models, it builds The View.
* The View uses the Model data and renders the final web page by responding to the user’s request.

The response is presented as a website in the user’s browser.

### How does Flask Display a Page?
1. A user sends a request (by entering a URL).
2. The request is routed to a function of the controller.
3. The controller uses the models to retrieve necessary data.
4. The controller builds the view with the data from the models.
5. The controller renders the view and sends it back to the user.


