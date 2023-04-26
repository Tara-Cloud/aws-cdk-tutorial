# Deploy a Serverless Web Application using the Amazon Cloud Development Kit (AWS CDK)

>***Author's Note:*** 
>The intended audience for this tutorial is developers, cloud architects, and DevOps professionals with a basic understanding of cloud computing and an existing AWS account.  This tutorial also assumes a basic knowledge of object-oriented programming.

>This tutorial could be part one of a more extensive series where learners could eventually build out a full-scale web application following the example architecture presented in this tutorial's *Constructs, Stacks, and Apps* section.  

![img](readme-assets/tutorial_title.png)

The [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) is a framework used to define cloud infrastructure as code.  With the AWS CDK, we can use our favorite object-oriented programming languages to build reliable, scalable, and secure applications in the AWS cloud without manually deploying infrastructure.

***In this tutorial we will learn:***
- The value proposition of the AWS CDK
- The building blocks of AWS CDK applications (Constructs, Apps, and Stacks)
- The basic structure of AWS CDK projects
- The lifecycle of a CDK application

Once we understand what the AWS CDK is all about, we will use our new skills to deploy a website to the cloud!

**Estimated Time to Complete**: 10-20 min (not including prerequisites)

**Cost**: All AWS resources deployed in this tutorial fall within the [AWS Free Tier](https://aws.amazon.com/free/free-tier-faqs/).  Make sure to follow clean-up instructions in *Step 7* of this tutorial.  

## Tutorial Pre-Requisites
- [ ] [Node.js (>= 10.13.0, except for versions 13.0.0 - 13.6.0)](https://nodejs.org/en)
- [ ] An [IDE](https://www.codecademy.com/article/what-is-an-ide) of your choice.  We will be editing code throughout this tutorial.  One great option is [VS Code](https://code.visualstudio.com/download).
- [ ] An active AWS Account and a basic understanding of [AWS Regions](https://cloudacademy.com/blog/aws-regions-and-availability-zones-the-simplest-explanation-you-will-ever-find-around/).
- [ ] [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
- [ ] The AWS CLI configured with credentials for an IAM user with the `AdministratorAccess` permission policy attached.  [Instructions for configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).  

## The Power of CDK

A CDK application defines a cloud application or cloud infrastructure configuration.  We can deploy the same CDK application once or hundreds of times.  This functionality is powerful for several reasons:

- :shield: **Security**: Define reusable components modeled to meet security best practices and your organization's security and compliance requirements.  Minimize human error by modeling and sharing vetted configurations via the CDK.
- :moneybag: **Cost Savings**: Use the AWS CDK to provision and destroy entire cloud architectures quickly.  Destroy cloud infrastructure when it's not needed, and avoid paying for unnecessary resources.  Use the AWS CDK to redeploy the same infrastructure in seconds as needed.
- :detective: **Best Practices Built-in**: Create and reuse patterns built using cloud best practices.  Use 1000+ high-quality [existing, open-source CDK libraries](https://constructs.dev/) to deploy common cloud infrastructure patterns.

## Constructs, Stacks, and Apps

CDK applications are created with three essential parts: constructs, stacks, and apps.
- **Constructs**: Constructs are the building blocks of your CDK application.  A construct represents a *cloud component* to be deployed in your cloud environment.  

A cloud component could be one resource - such as one [Amazon S3 bucket](https://aws.amazon.com/s3/) - or a cloud component could represent a higher-level abstraction such as an [application load balancer fronting containers running in the Amazon Elastic Container Service](https://docs.aws.amazon.com/solutions/latest/constructs/aws-alb-fargate.html).  

CDK Constructs are powerful because they can be used to define common infrastructure patterns using best practices - once defined, CDK Constructs make best practice patterns easily sharable and repeatable.
- **Stacks**: Stacks are the unit of deployment in the AWS CDK.  Every AWS resource defined using a CDK construct must be defined within the scope of a stack.  When you deploy your CDK application, you will choose whether to deploy every stack in the application, only specific stacks or even multiple copies of the same stack.
- **Apps**: A CDK application or app is a container for one or more stacks. 

![img](readme-assets/cdk_application_diagram.png)

> :bulb:*Summary:* A CDK application (or app) is a container for multiple stacks.  A CDK stack is a container for multiple CDK constructs.  CDK constructs represent a cloud component deployed to your cloud environment.

Perhaps we want to host a [serverless web application](https://catalog.us-east-1.prod.workshops.aws/workshops/b0c6ad36-0a4b-45d8-856b-8a64f0ac76bb/en-US) in the cloud.  Here is an example of a typical serverless architecture:

![img](readme-assets/example_serverless_architecture.png)

> :bulb:*Tip:* This application is serverless because it can be built and maintained without provisioning and maintaining servers.  AWS abstracts away all server management.

We like this serverless architecture a lot, and we know our team will want to deploy many similar architectures in the future.  Or we may need to deploy our serverless application separately in several countries.  Or maybe both.  This sounds like a perfect use case for the AWS CDK!  Below is an example of organizing our serverless web application into a CDK application using constructs, stacks, and apps.

![img](readme-assets/cdk_application_serverless_web_app_diagram.png)
> :bulb:*Tip:* Apps, stacks, and constructs promote modularity and reuse.  We could reuse the entire CDK application if we wanted to deploy a different website with the same architecture.   We could reuse only the Front End stack if we just needed a static website with no data store or compute.  If an individual construct is perfectly configured to meet our security requirements, we can plug that construct into countless other stacks and applications.

## CDK Application Lifecycle

We are about to build our first CDK application!  We will work with CDK using the command line interface.  Familiarizing yourself with common CDK commands is a great way to familiarize yourself with the overall lifecycle of a CDK application.  Take a moment to review the graphic below.  These commands are the same for Windows, Linux, and MacOS users.
![img](readme-assets/cdk_app_lifecycle.png)

*\*note that CloudFormation is out of scope for this tutorial but an important tool to familiarize yourself with to build infrastructure as code expertise.  Check out the [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to learn more.*

## Let's Build a CDK App!

Now that we know what the AWS CDK is all about, let's get hands-on and deploy our first CDK application!  We will use the AWS CDK to configure and deploy a simple static S3 website hosted in the AWS cloud. 
> :bulb:*Tip:* Remember to review the list of pre-requisites at the beginning of the tutorial.  Every pre-requisite is mandatory.

> :bulb:*Tip:* If you get stuck or lost you can refer to the code for the completed solution located in the `cdk_static_website_COMPLETED` directory within this repository. 

## Step 1: Configure Your Dev Environment
### Install the AWS CDK Toolkit
The AWS CDK Toolkit is a command-line utility that you will use to orchestrate your CDK applications.  Windows, Mac, and Linux users can install the CDK Toolkit by running the following command:

*Note: Windows users should run this command as an Administrator and Mac/Linux users should run this command using `sudo`*

`npm install -g aws-cdk`

Verify your AWS CDK Toolkit installation by running

`cdk --version`

*Example Output:*

![img](readme-assets/cdk_version_EO.png)

### Select Your Programming Language
AWS CDK allows you to model and deploy cloud infrastructure using your object-oriented programming language of choice.  No need to learn new syntax!  CDK is currently available for TypeScript, JavaScript, Python, Java, C#, and Go.  

Depending on your choice of programming language, you may encounter additional prerequisites.  For this tutorial, we will be using Python, and we need the following tools installed on our system:
- [ ] [Python version 3.6 or greater](https://www.python.org/downloads/)
- [ ] [Python package installer (pip)](https://pip.pypa.io/en/stable/installation/)

Verify your Python installation by running 
`python --version` or `python3 --version`

*Example Output:*

![img](readme-assets/python3_version_EO.png)

## Step 2: Create Your First CDK Application
### Initialize a CDK Project
Create an empty directory where your CDK application will live:

`mkdir cdk_static_website && cd cdk_static_website`

The `cdk init` command creates a new, empty CDK project.  You can run `cdk init --help` to see the options available.

We will create a new CDK project using a sample-app template and build our CDK application using Python.  Run the `cdk init` command using the following options:

`cdk init sample-app --language python`

*Example Output:*

![img](readme-assets/cdk_init_EO.png)

![img](readme-assets/cdk_init_EO_2.png)

### Activate our virtual environment and install the required modules
A virtual environment allows us to install packages and run our Python application without impacting the Python installation on our system.  [Learn more about virtual environments here](https://docs.python.org/3/tutorial/venv.html).

Let's activate our virtual environment by running the following command.  Make sure you are in your `cdk_static_website/` directory.

Linux/MacOS:

`source .venv/bin/activate`

Windows:

`.venv\Scripts\activate.bat`

> Your Python installation should have virtual environment functionality built in.  If your virtual environment activation fails you may need to manually create a virtual environment by running `python3 -m venv .venv`

Once we have activated our virtual environment, we can install the required Python modules for our project by running

`pip install -r requirements.txt`

Now we are ready to work with CDK!

> :bulb:*Tip:* If you haven't already, now is an excellent time to open your IDE.  If you are using VS Code you can open the project directory in VS Code by running `code .` 

![image](readme-assets/cdk_python_project_structure.png)

In initializing our project, the CDK Toolkit has created several pre-configured files and directories for us.  We will focus on the most critical files.  [Read more about CDK project structure and components here](https://cdkworkshop.com/30-python/20-create-project/300-structure.html).
- ***app.py***: the entry point for our CDK application, similar to a "main" file.
- ***cdk_static_website/cdk_static_website.py***: a Python file that creates a custom CDK stack for use in your CDK application.  We will learn more about stacks when we model and deploy our application.  A production CDK application will likely grow to have several different files defining several different stacks. 
- ***cdk.json*** A configuration file for CDK that defines several aspects of our application and how it should operate.  
- ***README.md***: A README describing our CDK application and basic deployment steps.  Notice we can find several useful tips and CDK commands prepopulated in the README by the CDK toolkit.   Eventually, we should customize this README file to be specific to the CDK application we build.
- The CDK toolkit also initialized a [git repository](https://www.gitkraken.com/learn/git/tutorials/what-is-a-git-repository) for us in the project directory and populated a [.gitignore file](https://git-scm.com/docs/gitignore) that we can modify as needed.

## Step 3: Bootstrap Your AWS Account

An AWS environment is a combination of the AWS account and AWS region where we are provisioning our cloud resources.  We prepare our AWS environment using a process called CDK Bootstrap.  The CDK Bootstrap script will provision several resources in our AWS environment. CDK will rely on these resources behind the scenes when our applications are being deployed.

Bootstrapping an AWS environment is a one-time process.  You will only need to rerun CDK Bootstrap if you start deploying CDK applications in different AWS regions or a different AWS account.  [Read more about CDK Bootstrap here.](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)

Bootstrap your AWS environment by running: 

`cdk bootstrap`

*Example Output:*

![img](readme-assets/bootstrap_existed_output.png)

## Step 4: Design our Application

Remember that the unit of deployment in the AWS CDK is called a ***stack***.  Within our CDK stacks we will use Python to define the resources we want to provision in the AWS cloud.  Let's get started by opening `cdk_static_website/cdk_static_website_stack.py`.  The file in its current state looks like this:

![img](readme-assets/cdk_static_website_stack%20_init_view.png)

> :bulb:*Tip:* If your IDE gives you warnings like `Import "aws_cdk" could not be resolved` the most likely cause is an IDE misconfiguration related to your Python interpreter.  Fixing this is out of the scope of this tutorial.  If you have followed all the previous instructions correctly, you can safely ignore these warnings. 

This example code will deploy two AWS resources: a [Amazon SQS Queue](https://aws.amazon.com/sqs/) and a [Amazon SNS Topic](https://aws.amazon.com/sns/).  

Let's delete the existing code in `cdk_static_website_stack.py` and replace it with the following code block:

```
from constructs import Construct
from aws_cdk import ( 
    Stack,
    aws_s3 as s3, 
    aws_s3_deployment as s3_deploy,
    RemovalPolicy,
)

class CdkStaticWebsiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        #create a s3 bucket to host our static website
        static_website_bucket = s3.Bucket(self, "StaticS3Bucket",
            public_read_access=True,
            block_public_access=s3.BlockPublicAccess(restrict_public_buckets = False),
            website_index_document='index.html',
            website_error_document='error.html',
            removal_policy= RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        #upload the html documents from s3-assets/ directory to the s3 bucket
        deployment = s3_deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3_deploy.Source.asset("../s3-assets")],
            destination_bucket=static_website_bucket
        )
```

This block of code imports several CDK modules and then uses those modules to model cloud infrastructure.  Specifically, we are defining the CdkStaticWebsiteStack.  The CdkStaticWebsiteStack will include two constructs:
- a [S3bucket construct](https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_s3/Bucket.html) configured with the necessary settings to support static website hosting.  This construct will create a new s3 Bucket in our AWS cloud environment.
> :rotating_light: *SECURITY ALERT* :rotating_light: Almost all S3 bucket deployments will be configured to set the block_public_access property to true.  This project uses a special S3 bucket configuration designed for website hosting.  It is critically important that we do not store ANY files or objects in this S3 bucket other than files you want publicly available on a public website.
- a [BucketDeployment construct](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3_deployment/BucketDeployment.html) which is used to upload assets to our newly created bucket.  In this case, we use the BucketDeployment construct to upload the html files we want to serve from our bucket.

> :bulb:*Tip:* As we learn, we copy and paste existing code to get the feel of working with the CDK.  When designing and coding your CDK applications, you will use the [CDK API documentation](https://docs.aws.amazon.com/cdk/api/v2/python/modules.html) to make decisions about what code to write.  You can see examples of the CDK API documentation by clicking the S3Bucket and BucketDeployment construct links above.  

Open the `app.py` file located in the root of our project directory.  

We do not need to make any changes to `app.py`, but let's look at what is happening here.  `app.py` is the application entry point, meaning when we deploy our CDK application, the deployment process will begin by running the code in `app.py`.

![img](readme-assets/app_py_from_template.png)

- On line 5, we are importing the CdkStaticWebsite stack we just defined.  
- On line 8 we instantiate our application and on line 9 we add the CdkStaticWebsite stack to our application.
- When `app.synth()` runs on line 11, CDK will synthesize our application and deploy our resources.

In our static website app we are only deploying one stack, but here is an example of what `app.py` might look like for a production-scale CDK application with multiple stacks:

![img](readme-assets/production_app_py.png)

## Step 5: Synthesize and Deploy our Application
We have successfully designed our CDK application using constructs and stacks.  Let's get this website in the cloud!

### CDK Synth 

Start by running the `cdk synth` command.  

Run:

`cdk synth`

*Example Output:*

![gif](readme-assets/synth_EO.gif)

The output of `cdk synth` will be lengthy.  The `cdk synth` command synthesizes our CDK code into a CloudFormation template.  We don't need to know about CloudFormation templates for this tutorial, but note that a new directory `cdk.out` has appeared in our project.  This directory is where synthesized CloudFormation templates are stored.

`cdk synth` will fail if we have syntax errors in our code - this is useful because we can correct errors before we try to deploy our resources rather than having a deployment fail. 

### CDK Deploy

So far, we have done a lot of designing and planning, but we have not yet provisioned any cloud infrastructure.  The `cdk deploy` command will trigger the actual deployment of resources in our account based on the code in our CDK app.  

Run: 

`cdk deploy`

*Example Output:*

![gif](readme-assets/deploy_EO.gif)
> :rotating_light: *Security Alert:* :rotating_light: We will be asked to review any Identity and Access Management (IAM Changes) that will be made when our CDK application is deployed.  This step adds awareness of security implications for our cloud environment resulting from this deployment.  In production, we should review these changes very closely. Here we can select **y** to approve the changes and deploy the stack.   

Upon successful deployment, we are given a *Stack ARN*.  ARN stands for Amazon Resource Number and is a unique identifier within AWS.  If our application had deployed more than one stack, we would see multiple *Stack ARNs* displayed.  

We can open the AWS console and navigate to the CloudFormation console.  The CloudFormation console allows us to view our newly deployed stack.

![gif](readme-assets/cloudformation_console_example.gif)

> :bulb:*Tip:* Did you notice another stack in your CloudFormation console called *CDK Toolkit*?  This stack was deployed by us earlier when we ran `cdk bootstrap`.

## Step 6: Update Your Application

Our CDK application deployment succeeded, and our S3 Website is live and running.  Of course, we want to see the website in action!  We can manually find the URL for our new website using the S3 console within AWS, but that's a pain.  Wouldn't getting the website URL as an output once our stack is deployed be better?  

This is a great opportunity to practice iterative development and improve our application by making an update to our CDK code.  

Open `cdk_static_website\cdk_static_website_stack.py` and make a few edits.

We will import the Cfn output CDK module and use it to output information about the resources we deploy.
- update the imports at the top of your file to include CfnOutput as an imported Python class: 
```
from constructs import Construct
from aws_cdk import ( 
    Stack,
    aws_s3 as s3, 
    aws_s3_deployment as s3_deploy,
    RemovalPolicy,
    CfnOutput
)
```
- at the bottom of the file (after the S3 deployment construct) add:
```
#output s3 bucket URL when stack is deployed
CfnOutput(self, "S3 Website Url", value=static_website_bucket.bucket_website_url)
```
Let's also increase the security posture of our web app by enforcing access logging on our s3 bucket.  Add a line of code to our s3 bucket construct.  Replace our current bucket construct with a construct that enforces server access logging and deploys a second, private S3 Bucket for log storage.

```     
#create a s3 bucket to host our static website
static_website_bucket = s3.Bucket(self, "StaticS3Bucket",
    public_read_access=True,
    block_public_access=s3.BlockPublicAccess(restrict_public_buckets = False),
    website_index_document='index.html',
    website_error_document='error.html',
    removal_policy= RemovalPolicy.DESTROY,
    auto_delete_objects=True,
    server_access_logs_bucket= s3.Bucket(self, 'static_website_logging_bucket')
)
```

After making these changes, `cdk_static_website\cdk_static_website_stack.py` should look like this: 

![img](readme-assets/updated_stack_py.png)

Implement our changes by running 

`cdk deploy`

Remember to select *y* when prompted to approve our new deployment.
![img](readme-assets/deploy_changes_approval.png)

*Example Output:*

![img](readme-assets/deploy_changes_success_EO.png)

Awesome!  Now we can click on the link output in our terminal and see our brand new *Hello World* website deployed using the AWS CDK.  
> :bulb:*Tip:* Curious about the error.html document we reference in our S3 bucket configuration?  Append error.html to the end of our S3 Website URL and see what happens.  Because we correctly configured our S3 Bucket construct, our bucket is already set up to route web traffic like a traditional web server.  If users enter an invalid URL, they will be redirected to either the index.html or error.html files we deployed to our bucket using CDK.  

![img](readme-assets/website_hello_world_EO.png) ![img](readme-assets/error_page_EO.png)

## Step 7: Destroy Your Application

It's time to practice the last step of the CDK application lifecycle and tear down our application.  We will delete every resource by destroying the entire CDK stack.

Run:

`cdk destroy`

*Example Output:*

![img](readme-assets/destroy_EO.png)

Select **Y** to approve the deletion of our CDK stack.  

> :bulb:*Tip:* Make sure to complete step 7 and destroy all resources to avoid incurring future AWS charges.

## Summary

Great job!  

In this tutorial you learned:

- the basic structure of an AWS CDK application
- why the AWS CDK is a powerful tool for deploying cloud infrastructure
- how to design and deploy a basic CDK application

Continue on your CDK learning path with more great labs and resources below:

### What to Build Next? 
Want to keep building your skills?  There are several different AWS architecture patterns you can practice implementing to make this web app more secure and performant
- [Deploy a Serverless Web App using S3 and API Gateway with Cognito Authentication](https://aws.amazon.com/getting-started/hands-on/build-serverless-web-app-lambda-apigateway-s3-dynamodb-cognito/)
- [Deploy a React App on Amazon S3](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront.html)

### Continuing Education Resources:
- [AWS CDK on GitHub](https://github.com/aws/aws-cdk)
- [AWS CDK User Guide](https://docs.aws.amazon.com/CDK/latest/userguide)
- [The CDK Workshop](https://cdkworkshop.com/)
- [AWS CDK FAQs](https://aws.amazon.com/cdk/faqs/)
- [Securing your AWS CDK Deployments](https://aws.amazon.com/blogs/devops/secure-cdk-deployments-with-iam-permission-boundaries/)