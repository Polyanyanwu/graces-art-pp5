
# Cloning and Deployment for Graces Art Print

- [Cloning and Deployment for Graces Art Print](#cloning-and-deployment-for-graces-art-print)
  - [Prerequisites](#prerequisites)
    - [Fork the Repository](#fork-the-repository)
    - [Clone the Repository](#clone-the-repository)
      - [Through the HTTPS](#through-the-https)
    - [Application Dependencies](#application-dependencies)
  - [Deployment to Heroku](#deployment-to-heroku)
    - [**Create Heroku App**](#create-heroku-app)
    - [**Create Database in Heroku**](#create-database-in-heroku)
    - [**Create the Config Variables**](#create-the-config-variables)
  - [Deploy through the CLI](#deploy-through-the-cli)
  - [Deploy through the Heroku Deploy Tab and Github](#deploy-through-the-heroku-deploy-tab-and-github)

The project was developed using [GitPod IDE](https://www.gitpod.io/) (Integrated Development Environment)and pushed to [GitHub](https://github.com). The project repository is at [Graces Art Print](https://github.com/Polyanyanwu/graces-art-pp5). Commits to the repository were done via the Git version control available in the Gitpod.

[Return to README](/README.md)

## Prerequisites

1. You need to create an account in [GitHub](https://github.com) if you don’t have any yet.
   Login to your GitHub account.

After logging into Github, you could decide on any of the following options:

1. Create a repository: [Here](https://docs.github.com/en/github/getting-started-with-github/create-a-repo), create same directory structure as I have, copy and paste the codes.
2. You can **fork** the Graces Art Print repository, or
3. You can **clone** the repository.

### Fork the Repository

Fork of a repository will create a copy of the repository in your own repositories in GitHub.

You can make changes to the copy as you desire. You can also pull the latest version from the original repository through a pull request in the upstream repository.

To Fork a repository you need to proceed as follows:

1. Navigate to the repository [Graces Art Print Repository](https://github.com/Polyanyanwu/graces-art-pp5).
2. Locate the fork button on the top right of the page and click on it. This will create a copy of the repository in your own Github repositories.

### Clone the Repository

Cloning enables you to create a copy of the repository locally on your computer. This is making a local copy of the repository at that point in time.

To clone a repository, proceed as follows:

1. Open the [Graces Art Print Repository](https://github.com/Polyanyanwu/graces-art-pp5).
2. Click on the **Code** button.

![Code button](/docs/deploy/images/repository_code_btn.png)

1. Three options are presented to clone the repository (HTTPS, SSH, Gihub CLI). This manual will discuss the most popular method (HTTPS) and offer a link for further information on others.

![Clone options](/docs/deploy/images/cloning_options.png)

#### Through the HTTPS

- Click HTTPS option and copy the link given
- You may click on the Download Zip button and get a compressed zip file of the repository downloaded to your machine.
- You can also click Open with GitHub desktop if you have it installed
- Navigate to the directory on your machine where you want to store the cloned repository.
- Open your Terminal and type: ```git clone``` and paste the link copied above.
- Press **Enter** and the local clone will be created.

For further information visit [Cloning Repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-using-the-command-line).

[<< Back to README](/README.md) [>> Bact to TOC](#cloning-and-deployment-for-graces-art-print)

### Application Dependencies

The project was developed mainly with Django and relevant packages. In Django/Python projects a requirements.txt file is created in the main application folder. This file indicates which packages and dependencies are required to run the application. After successfully creating/clone/fork the project, you have to run this command in the CLI:

- ``pip3 install -r requirements.txt``. The command will install all the application requirements needed for the project.
- Secondly you need to create the database to run the application and other environment variables. More information on the creation of the database and other variables will be discussed under Deployment to Heroku given below.
- You need to run migration in order to create the database from the models. Run the following commands in the CLI:
  - ``python3 manage.py makemigrations`` and then,
  - ``python3 manage.py migrate``

- After the successful migrations which created the database, run the project locally by typing:
  - ``python3 manage.py runserver``

## Deployment to Heroku

The application was deployed to [Heroku](https://heroku.com) where all the code and database is hosted. The static files were hosted on [Amazon AWS](https://aws.amazon.com/s3/)

 The live site is accessible at [Graces Art Print](https://graces-art.herokuapp.com/).

Find below steps that were used to effectively deploy the application to the Heroku platform.

### **Create Heroku App**

1. Sign up / Log in to [Heroku](https://heroku.com) and create an account.

2. From the Heroku Dashboard page select 'New' and then 'Create New App'

![Heroku New App](/docs/deploy/images/create_application.png)

3. From the Create New App form that opens, input an App Name and chose a Region (Europe or United States). When you enter an App Name if it is available, Heroku will indicate that it is available. If its not available you chose another name. Application names in Heroku are unique. I created the app (graces-buffet).

![Heroku New Application Form](/docs/deploy/images/heroku_create_app.png)

### **Create Database in Heroku**

4. Its time to create the Database Resource. Postgres DB was used for the project. From the Heroku Dashboard, select your application name by clicking on it, then click on the Resources tab. From the search bar that opens in the Resources tab, input postgres and heroku will automatically display a suggested list of resources matching the name you inputted.

![Postgres DB Search](/docs/deploy/images/postgres_search.png)

Click on the Heroku Postgres and Heroku will display the Order form for you to select the Plan you need. If it is for app development like we are doing, select the Free plan.

![Postgres DB Plan](/docs/deploy/images/postgres_heroku.png)

Click on Submit Order Form to complete the process.
Heroku provision's the database and automatically creates a record in the Config Vars (see below) for the Database URL. This URL is very essential for you to access the database from your application.

[<< Back to README](/README.md) [>> Bact to TOC](#cloning-and-deployment-for-graces-art-print)

### **Create the Config Variables**

5. The next thing to do is to create the necessary Config environment variables needed for the application to run.
- From the Settings tab, click on the Reveal Config Vars button to open the Config Vars which shows empty KEY and VALUE settings. In my own application I am using Postgres DB, Amazon AWS, Stripe for Payment, email forwarding and the required keys are listed below:

![Config Vars](/docs/deploy/images/config_vars.png)

- If you have not done so, proceed to [Amazon AWS](https://aws.amazon.com/s3/), create an account. You will need to create Bucket, AWS Groups, Policies and User. Grant the user permission to the Bucket and grant programmatic access to the user. Put the user in the group which has your policy attached. Download the CSV file which will contain this users access key and secret access key which you will put in the Config Var of Heroku. The process is a bit long, you can get tips on how to successfully create your AWS S3 bucket, user, group and connect to Django from online resources like this from [Michael Herman](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/).
- Create media and static folders at your AWS bucket created in the first step.
- If you have initial media files, copy them across to the Bucket's media folder, be sure to grant Public read access to the media files.
- The static files will be created at the S3 bucket when you deploy the application during the collectstatic phase of the deployment.

6. You also need to create a Developer's test account with [Strip](https://dashboard.stripe.com).

- Create an account with Stripe
- Click on Developers
- Click on API keys and copy the Published Public key and the Secret key which you will put in the Config Vars at Heroku.

![Stripe API Keys](/docs/deploy/images/strip_api.png)

- Create Strip Webhook endpoint which is also required for processing card payments.

![Stripe Webhook](/docs/deploy/images/webhook_endpoint.png)
For further information on creating the Stripe Webhook please [see this documentation](https://stripe.com/docs/api/webhook_endpoints/create)

- Click on the Webhook endpoint you created and copy the Signing Secret which is part of what you need to put in the Config var as shown above (STRIPE_WH_SECRET).

## Deploy through the CLI

- You need to enable two-factor authentication in your Heroku account.
- Click on Account Settings in Heroku
- Copy your API which you will use in logging into the Heroku from the Terminal in your development environment.
- Return to your Gitpod or development IDE
- Add Heroku as a remote repository to your workspace using ```git remote add heroku <url address of your app on heroku>```
- type ```heroku login -i```
- You will be prompted for your Heroku email and password
- For the password, enter the API key you copied from step 2 above.
- Finally, type ```git push heroku main``` where main is the branch you want to deploy.

OR

## Deploy through the Heroku Deploy Tab and Github

- Open your application in Heroku
- Click on the Deploy tab.
- Click on a Deployment method, in this case it is Github. Click on Connect to Github.
- At the Connect to GitHub section, select your Github account; enter the name of the repository and click on the Search button.
- If the account and repository are located by Heroku, click on Connect button. This action will connect the Github repository to the application created in Heroku.
- Next is to choose either Automatic deploy or Manual deploy. The Automatic deploy will execute each time you push a commit to your Github repository connected to the application. You can also choose manual deployment, select the branch to deploy and click on Deploy Branch.

![Deployment Method](/docs/deploy/images/deployment_method.png)

- Heroku will then build the application and after completion of the build process you will see Your App Was Successfully Deployed message and a link to the application's live site is displayed.

[<< Back to README](/README.md)   [>> Bact to TOC](#cloning-and-deployment-for-graces-art-print)
