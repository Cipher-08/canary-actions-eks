
<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 23.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>
<a href="#gdcalert13">alert13</a>
<a href="#gdcalert14">alert14</a>
<a href="#gdcalert15">alert15</a>
<a href="#gdcalert16">alert16</a>
<a href="#gdcalert17">alert17</a>
<a href="#gdcalert18">alert18</a>
<a href="#gdcalert19">alert19</a>
<a href="#gdcalert20">alert20</a>
<a href="#gdcalert21">alert21</a>
<a href="#gdcalert22">alert22</a>
<a href="#gdcalert23">alert23</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# 

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.jpg "image_tooltip")



## **Choosing the Best Way to Update Your App: Canary vs. Rolling Out in Kubernetes**

In Kubernetes, several techniques for deploying applications are available, each suited to different needs and scenarios.  These techniques include _blue-green deployments, canary deployments, rolling updates, A/B testing, and recreate deployments._ Each method offers its approach to managing updates and minimizing downtime.

This blog will focus on two popular methods: _canary deployments and rolling updates. _

This blog will focus on canary and rollout deployment strategies, explaining how they work locally and with Amazon EKS. However, these strategies can be used in any version of Kubernetes. We'll also discuss how to automate these processes using GitHub Actions, providing a detailed guide on implementing canary and rollout deployments from local testing to production environments.


## **Use a Canary deployment strategy for Kubernetes deployments.**

Canary deployment involves deploying two versions of an application, where the new version (the "canary") is rolled out to a small set of users to test its performance in a real-world environment.


### **Why choose a canary deployment strategy?**

Canary deployments let you introduce a new app version to just a few users first. This way, you can make sure everything works well before rolling it out to everyone. It's useful for catching issues early, reducing the risk of affecting all your users if something goes wrong. Now, let's explore how the canary deployment strategy is implemented:

First, deploy the new version of your software to a section of your environment where it won't affect active users. 



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


After testing—be it functional, unit, or integration tests—and once your users have tested the feature and are confident in the new version, begin directing a small group of users to it. This group could consist of internal team members.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


As confidence grows, gradually increase the scope of the rollout by deploying more pods and broadening the user base that accesses the new version. Once the canary phase confirms stability, a new deployment is scaled up to serve all users, marking the successful completion of the rollout process.



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")



### **Setup for Canary Deployment**

Let's outline our starting point before we set up a canary deployment. We have developed a simple Flask application, which we've dockerized and uploaded to DockerHub.

To implement a canary deployment, you need two deployment configurations: one for the deployment that creates the stable version of your application and one for the deployment creates the canary version.

**deployment1.yaml - Stable Version**



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.jpg "image_tooltip")


**deployment2.yaml - Canary Version**

This deployment is the new version you are testing, initially receiving a small fraction of the traffic.



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.jpg "image_tooltip")



### **Initiate Canary Workflow**

Apply the Deployments: Start by deploying both versions using kubectl.



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")




<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.png "image_tooltip")



### **Promoting the Canary**

If the canary version performs well, you can gradually increase the number of replicas of the canary deployment and decrease the replicas of the stable version. 

_Kubectl scale deployment/python-app-v1 —replicas=5_



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.png "image_tooltip")


_Kubectl scale deployment/python-app-v2 —replicas=5_



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image10.png "image_tooltip")



### **Rejecting the Canary**

If the canary version encounters issues, roll it back to minimize impact. This can be done by scaling the canary deployment down to zero:

_kubectl scale deployment/python-app-v2 --replicas=0  _



<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image11.png "image_tooltip")



## **Integrating Canary Deployment with GitHub actions.**

So far, we have successfully implemented canary deployment locally using Minikube. Now, let's move on to updating our CI/CD pipeline to automate this process with GitHub Actions.

**Step 1: Set Up Amazon EKS**

Before integrating with GitHub Actions, you need an EKS cluster:

Create an EKS Cluster: You can use AWS Management Console, AWS CLI, or eksctl to create a cluster. For simplicity, eksctl is a good choice:

_eksctl create cluster --name rollingback --region us-east-1 --nodegroup-name eks-nodes --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 4 --managed_



<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image12.png "image_tooltip")


This command creates an EKS cluster named "rollingback" with a managed node group.

**Step 2: Create a GitHub Workflow**

Create a .github/workflows/deploy.yml file in your repository to define the CI/CD workflow:



<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image13.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image13.jpg "image_tooltip")


**Step 3: Set Up GitHub Secrets**

Configure the required AWS credentials in your GitHub repository's secrets to secure your AWS access:



<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image14.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image14.png "image_tooltip")


**Step 4: Deploy and Verify**

You can see the progress and results of your deployment workflow by going to the "Actions" tab in your GitHub repository.



<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image15.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image15.png "image_tooltip")


The command _aws eks --region us-east-1 update-kubeconfig --name rollingback _configures kubectl to interact with your AWS EKS cluster, updating the kubeconfig file with the necessary access details.

The _kubectl apply -f deployment1.yaml_ command deploys your application updates to EKS. This step attempts to use your deployment configurations as specified in deployment1.yaml. 

If the deployment configurations have remained unchanged since the last update, you might see messages like deployment.apps/python-app-v1 unchanged, indicating that no changes were necessary.

By following these steps, you've automated your Kubernetes deployments to EKS using GitHub Actions, providing a secure way to deliver updates to your Kubernetes service application continuously.


## **Understanding Rollout Deployments**

Rollout deployments, or rolling updates, are a way to update applications gradually. This approach is essential in environments where running the application without downtime is required. 


### **What Are Rollout Deployments?**

Rollout deployments update applications, in which new versions are introduced incrementally across the entire environment instead of just a small subset of users. Unlike canary deployments, which test the latest version on a small percentage of the traffic before going full scale, rollout deployments gradually apply the updates to all instances. 

Kubernetes also supports managing multiple deployments concurrently, allowing for diverse configurations and testing environments to run in parallel.


### **How Rollout Deployments Work in Kubernetes**

Kubernetes does not update all pods at once. Instead, it replaces the old running pods with new ones in controlled phases. This is managed by setting the maxSurge and maxUnavailable parameters in the deployment configuration:



* _maxSurge_ specifies the maximum additional pods that can be created beyond the number you initially selected.
* _maxUnavailable_ sets the maximum number of pods unavailable during the update process.
* The deployment controller in Kubernetes orchestrates the rollout and management of new deployments, ensuring each step meets specified health checks before proceeding. 
* During the rollout, Kubernetes performs health checks on new pods as they come online. If a new pod fails these checks, Kubernetes stops the rollout and can automatically roll back to the previous version, depending on the deployment settings. This ensures that issues do not affect the entire application, as only a portion of the pods are replaced at any given time.
* Automatic Rollback: If a failed deployment occurs, Kubernetes' automatic rollback functionality is triggered to revert to the previous stable version, minimizing downtime.

A load balancer is utilized during the rollout to evenly distribute traffic between the old and new deployments, ensuring seamless user experience.


### **Steps to Set Up a Basic Rollout Deployment**

Before setting up a rollout deployment, let's establish our starting point. We have created a simple Flask application, dockerized it, and uploaded the image to DockerHub.

**Step 1: Create the Deployment Configuration**

**deployment.yaml**



<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image16.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image16.jpg "image_tooltip")


This deployment.yaml specifies the rolling update strategy, essential for implementing rollout deployments. Here's what each part of the strategy accomplishes:

**maxSurge**: This setting defines the maximum number of existing pods created above the desired number during the update. In this case, maxSurge: 1 allows one extra pod to be made during the rollout.

**maxUnavailable**: It is the maximum number of pods that can be unavailable during the update. Setting this to opt out of 2 means two original pods can be taken down before the new pods are ready.

**Step 2: Apply the Deployment Configuration**

To deploy your application (also supports multiple deployments) using this configuration, save the **deployment.yaml** file and run the following command:

_kubectl apply -f deployment.yaml_



<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image17.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image17.png "image_tooltip")


**Step 3: Monitor the Rollout Status**

After applying the deployment, you can monitor the status of the rollout to see how the update is progressing:

_kubectl rollout status deployment/python-app_



<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image18.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image18.png "image_tooltip")


This command will provide real-time feedback on the deployment status, showing whether the current rollout out is succeeding or if there are any issues.

**Step 4: Update the Application**

When you need to update your application, change the image in the deployment YAML file to the new version:



<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image19.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image19.jpg "image_tooltip")


Then reapply the deployment:

_kubectl apply -f deployment.yaml_

Kubernetes will start the rollout using the strategy defined in the YAML file.

**Step 5: Verify the Deployment**

Check the details of your deployed pods to ensure they are running the new version:

_kubectl get pods -l app=python-app -o wide_



<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image20.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image20.png "image_tooltip")


This command lists all pods with the label app: python-app, showing their status and the node they are running on.

**Step 6: Rollback if Necessary**

If you detect issues with the new version, Kubernetes allows you to rollback to the previous version:

_kubectl rollout undo deployment/python-app_



<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image21.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image21.png "image_tooltip")


This command in the command line reverts the deployment to the previous stable version.


## **How to do Rollout Deployments using GitHub Action**

As discussed earlier, setting up your deployment to Amazon EKS with Github actions involves several preliminary steps, such as configuring AWS credentials and preparing your Kubernetes configurations. 

Assuming you've followed those steps, the GitHub Actions workflow file is the only difference. Below is the deploy.yml file that automates the deployment of your application to Amazon EKS every time changes are pushed to your main branch:



<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image22.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image22.jpg "image_tooltip")


You can see the progress and results of your deployment workflow by going to the "Actions" tab in your GitHub repository.



<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image23.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image23.png "image_tooltip")


The command _aws eks --region us-east-1 update-kubeconfig --name rollingback _configures kubectl to interact with your AWS EKS cluster, updating the kubeconfig file with the necessary access details.

By following these steps, you've automated your Kubernetes deployments to EKS using GitHub Actions for rolling back deployment, providing a secure way to continuously deliver updates to your application.


## **Canary vs. Rollout Deployments**

To help you understand the differences between canary and rollout deployments and when you might choose one.


<table>
  <tr>
   <td><strong>Aspects</strong>
   </td>
   <td><strong>Canary Deployment </strong>
   </td>
   <td><strong>Rollback Deployment </strong>
   </td>
  </tr>
  <tr>
   <td>Definition 
   </td>
   <td>Deploys a new version to a controlled group of users before a full release.
   </td>
   <td>Updates are distributed gradually across all instances to avoid downtime.
   </td>
  </tr>
  <tr>
   <td>Risk-Management 
   </td>
   <td>High control; typically involves up to 10% of user traffic initially.
   </td>
   <td>Less risky than instant rollout but more so than canary, as about 50% of traffic may be affected during the initial state of the update.
   </td>
  </tr>
  <tr>
   <td>Feedback
   </td>
   <td>Rapid feedback enabled by <em>kubectl logs</em> and <em>kubectl describe </em>for targeted pods.
   </td>
   <td>Slower feedback from broader user base; requires monitoring via<em> kubectl get events.</em>
   </td>
  </tr>
  <tr>
   <td>Rollback
   </td>
   <td>Quick rollback using <em>kubectl rollout</em> <em>undo </em>affects minimal traffic.
   </td>
   <td>Rolling back with <em>kubectl rollout undo </em>can affect more users if issues are detected.
   </td>
  </tr>
  <tr>
   <td>Resource Requirement 
   </td>
   <td>Requires resource allocation for both the old version and new versions using <em>kubectl scale deployment --replicas=X.</em>
   </td>
   <td>Efficient use of resources by managing replicas incrementally with <em>kubectl scale.</em>
   </td>
  </tr>
</table>



## **Conclusion**

We've covered the essentials of deploying applications using canary and rollout strategies in Kubernetes, focusing on their application both locally and on Amazon EKS. We also explored how to streamline these deployments with GitHub Actions. Whether opting for a gradual rollout to manage risks or a canary strategy for testing new features with minimal user impact, these methods ensure efficient and safe updates. This guide should help you implement these strategies effectively, enhancing your deployment processes in any Kubernetes environment.


## **Commonly asked questions.**

**Q 1. How does rollout deployment work?**

Rollout deployment gradually updates all users by replacing old versions with new ones in stages. This minimizes disruptions if problems arise since not all parts of the application are updated at once.

**Q 2. What are the benefits of canary vs. rollout deployment?**

Canary deployments are beneficial for testing new features on a small scale before a full rollout, reducing the risk of major issues. Rollout deployments, however, provide a systematic update to all users, which can be controlled and reversed if necessary, offering a balance between innovation and stability.

**Q 3. When should you use canary deployment?**

Use canary deployment when introducing significant changes that could potentially disrupt the user experience or when you need to test new features in a live environment without impacting all users.

**Q 4. What are the best practices for rollout deployment?**

Best practices for rollout deployment include setting up proper health checks, using phased updates to manage changes, and ensuring that there is a quick rollback plan in place to undo the current deployment, if things go wrong.
