# Getting Started with the Amazon Cloud Development Kit (AWS CDK)
- The CDK ...
- In this tutorial we will...

## The Power of CDK
- security
- cost savings
- best practices built in

## What We Are Building

## Pre-Requisites
- [ ] An [IDE](https://www.codecademy.com/article/what-is-an-ide) of your choice.  We will be editing code throughout this tutorial.  One great option is [VS Code](https://code.visualstudio.com/download).
- [ ] AWS Account
-- :lightbulb: Security tip: root credentials to deploy resources is not a good practice
- [ ] Credentials for a Role/User with at least the following priviledges...
- [ ] [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
- [ ] [Node.js (>= 10.13.0, except for versions 13.0.0 - 13.6.0)](https://nodejs.org/en)

## Step 1: Configure Your Dev Environment
### Install the AWS CDK Toolkit
The AWS CDK Toolkit is a command-line utility that you will use to orchestrate your CDK applications.  Windows, Mac, and Linux users can install the CDK Toolkit by running the following command:

*(Note: Windows users should run this command as an Aministrator and Mac/Linux users should run this command using `sudo`)*

`npm install -g aws-cdk`

Verify your AWS CDK Toolkit installation by running 
`cdk --version`

### Select Your Programming Language
AWS CDK offers you the opportunity to model and deploy cloud infrastructure using your object-oriented programming language of choice - no need to learn new syntax!  CDK is currently available for TypeScript, JavaScript, Python, Java, C#, and Go with more languages to come.  

Depending on your choice of programming language, you may encounter additional prequisites.  For this tutorial we will be using Python and we need the following tools installed on our system:
- [ ] [Python version 3.6 or greater](https://www.python.org/downloads/)
- [ ] [Python package installer (pip)](https://pip.pypa.io/en/stable/installation/)

Verify your Python installation by running 
`python --version` or `python3 --version`

Verify your pip installation by running #TO-DO

## Step 2: Create Your First CDK Application
Create an empty directory where your CDK application will live:
`mkdir cdk_static_website && cd cdk_static_website`

The `cdk init` command creates a new, empty CDK project for us.  Run `cdk init --help` to see the options available to us when we create a new project.  For this tutorial we will create a new CDK project using a sample-app template and we will build our CDK application using Python.  Therefore, our `cdk init` command looks like this:
`cdk init sample-app --language python`

#TO-DO Example Output

Let's explore our new CDK Python application!
> If you havent already, it's a good idea to open your project directory in your IDE of choice to explore the contents. >
![image](readme-assets/cdk_python_project_structure.png)
As you can see, in the processes of initializing our project the CDK Toolkit has created several nice components for us.  For now we will focus on the most critical files.  [Read more about CDK project structure and components here](https://cdkworkshop.com/30-python/20-create-project/300-structure.html).
- **app.py**: the entry point for our CDK application, similar to a "main" file.
- **cdk_static_website/cdk_static_website.py**: a Python file that creates a custom CDK stack for use in your CDK application.  We will learn more about stacks when we model and deploy our application in step 4 of this tutorial.  A production CDK application will likely grow to have several different files defining several different stacks. 
- **cdk.json** A configuration file for CDK that defines several aspects of our application and how it should operate.  
- **README.md**: A README describing our CDK application and basic deployment steps.  Notice we can find several useful tips and CDK commands prepopulated in the README by the CDK toolkit.  Eventually we should customize this README file to be specific to the CDK application we build.
- Notice that the CDK toolkit also initialized a git repository for us in the project directory and populated a .gitignore file that we can modify as needed.

Now that we are familiar with our project structure, let's start building!

## Step 3: Bootstrap Your Account

## Step 4: Deploy Your Application to the Cloud 

## Step 5: Update Your Application

## Step 6: Destroy Your Application

## What to Build Next? 
- React App hosted in s3
- s3 behind API gateway with a lambda authenticator
- level 3 s3 website construct

## Become a Pro
- [CDK on GitHub](https://github.com/aws/aws-cdk)
- [The CDK Workshop](https://cdkworkshop.com/)
- [AWS CDK User Guide](https://docs.aws.amazon.com/CDK/latest/userguide)

#TO-DO:
- Example complete app code
- Example skeleton app code (with comments)
- Siren note around public access step 