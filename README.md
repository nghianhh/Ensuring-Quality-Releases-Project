## Introduction
This is the project for the Udacity Cloud DevOps using Microsoft Azure Nanodegree Program, in this project we create disposable test environments and run a variety of automated tests with the click of a button. Additionally, we monitor and provide insight into an application's behavior, and determine root causes by querying the application’s custom log files.

For this project we use the following tools:

- Azure DevOps: For creating a CI/CD pipeline to run Terraform scripts and execute tests with Selenium, Postman and Jmeter
- Terraform: For creating Azure infrastructure as code (IaS)
- Postman: For creating a regression test suite and publish the results to Azure Pipelines.
- Selenium: For creating a UI test suite for a website.
- JMeter: For creating a Stress Test Suite and an Endurance Test Suite.
- Azure Monitor: For configuring alerts to trigger given a condition from an App Service.

## Getting Started
For this project we will follow the next steps:
1. Install our dependencies
2. Configure storage account and state backend for Terraform
3. Create a Service Principal for Terraform
4. Configure Pipeline Environment
5. Configure an Azure Log Analytics Workspace
6. Create Postman Test Suites
7. Create a Selenium test for a website
8. Create a Test Suite with JMeter
9. Enable Monitoring & Observability

## Install our dependencies
| Dependency | Link |
| ------ | ------ |
| Terraform | https://www.terraform.io/downloads.html |
| JMeter |  https://jmeter.apache.org/download_jmeter.cgi|
| Postman | https://www.postman.com/downloads/ |
| Python | https://www.python.org/downloads/ |
| Selenium | https://sites.google.com/a/chromium.org/chromedriver/getting-started |
| Azure DevOps | https://azure.microsoft.com/en-us/services/devops/ |

## Terraform
1.  Clone source code from Github repo
2.  Open a Terminal and connect to your Azure account to get the Subscription ID
3. Create a storage account to Store Terraform state.
4. Copy the storage_account_name, container_name, and access_key, and update the corresponding values in terraform/environments/test/main.tf accordingly.

## Azure DevOps Pipeline
1. Go to https://dev.azure.com/ using Udacity provide account to create new AzureDevops project or use your email to create.
2. Install below extensions :

|Extensions|Link|
|--|--|
|JMeter|https://marketplace.visualstudio.com/items?itemName=AlexandreGattiker.jmeter-tasks&targetId=625be685-7d04-4b91-8e92-0a3f91f6c3ac&utm_source=vstsproduct&utm_medium=ExtHubManageList|
|PublishHTMLReports|https://marketplace.visualstudio.com/items?itemName=LakshayKaushik.PublishHTMLReports&targetId=625be685-7d04-4b91-8e92-0a3f91f6c3ac&utm_source=vstsproduct&utm_medium=ExtHubManageList|
|Terraform|https://marketplace.visualstudio.com/items?itemName=ms-devlabs.custom-terraform-tasks&targetId=625be685-7d04-4b91-8e92-0a3f91f6c3ac&utm_source=vstsproduct&utm_medium=ExtHubManageList|

3. Go to Project Settings > Pipelines > Service Connection > Azure Resource Manager > Service principal(manual), Create the new Service Connection

4. Go to portal to create a VM to use as an Agent or request a default agent from Microsoft

![Agent](https://github.com/nghianhh/Ensuring-Quality-Releases-Project/blob/3893206003eb0cce4abbaf3878e0748a1621ebb9/Screenshots/ADO_Agent_Pool.png?raw=true)

5. Create a New Pipeline > select GitHub > Existing Azure Pipelines YAML file > Choose  **azure-pipelines.yaml**  file

6. When running pipeline to stage "UITest" you might facing error : "No resource found ..." because you not yet setup VM for running this step in Environment.

7. Go to Azure Pipeline > Environments > test > Add resource > Virtual machines

8. Copy command, SSH to the VM then run copied command
![vm_resources](https://github.com/nghianhh/Ensuring-Quality-Releases-Project/blob/main/Screenshots/ADO_Test_Environment_Resource_VM.png?raw=true) 

9. After finished #8 go back to pipeline and re-run

10. Now wait for pipeline to execute on the following Stages: Provision > Deployment > PerfTest > UITest > FunctionalTest
![pipeline_overview](https://github.com/nghianhh/Ensuring-Quality-Releases-Project/blob/main/Screenshots/ADO_Pipeline_Overall.png?raw=true)

11. After the pipeline run complete successfully then check the Test result and deployed Azure app service is up

![Report_1](https://github.com/nghianhh/Ensuring-Quality-Releases-Project/blob/main/Screenshots/ADO_TestPlan_Report_1.png?raw=true)

![Report_2](https://github.com/nghianhh/Ensuring-Quality-Releases-Project/blob/main/Screenshots/ADO_TestPlan_Report_2.png?raw=true)

![Report_3](https://github.com/nghianhh/Ensuring-Quality-Releases-Project/blob/main/Screenshots/ADO_TestPlan_Report_3.png?raw=true)

![Deployed_AppService](https://github.com/nghianhh/Ensuring-Quality-Releases-Project/blob/main/Screenshots/Fake_Rest_API_Portal.png?raw=true)

## Configure Logging and Monitoring

1. Create a Log Analytics workspace

### Set up email alerts in the App Service:

1. Log into Azure portal and go to the AppService that you have created.
2. On the left-hand side, under **Monitoring**, click **Alerts**, then **New Alert Rule**.
3. Verify the resource is correct, then, click **Add a Condition** and choose **Http 404**.
4. Set the Threshold value of `1`. Then click **Done**.
5. Create an action group and name.
6. Add “Send Email” for the Action Name, and choose **Email/SMS/Push/Voice** for the action type, and enter your email. Click **OK**.
7. Name the alert rule `Http 404`, and leave the severity at `3`, then click **Create**.
9. Go to the App Service web page, navigate the links, and generate 404 not found errors (e.g., by visiting non-existent pages).
10. After a few minutes , check your mailbox.

###  Set up log analytics workspace to get custom logs:

1. Log into Azure portal and go to the Log workspace that you have created.
2. Under **Setting**, click **Table**, then create new table **New custom log (DCR-based)**.
3. Then go to **Monitor** resource, under **Setting**, select **Data Collection Rules**, open the rule you just created in #2.
4. In the DCR rule, under **Configuration**, open **Data Source**, add a new data source with type **Custom Text Log**, continue to complete the creation.
5. under **Configuration**, open **Resources** and add your VM that using to run Selenium test.
6. Check this article https://learn.microsoft.com/en-us/azure/azure-monitor/agents/data-collection-log-text?tabs=portal for more detail.

