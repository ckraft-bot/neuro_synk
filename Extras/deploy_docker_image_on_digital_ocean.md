# Steps to Deploy Docker Image on DigitalOcean App Platform

Follow these steps to deploy a Docker image from Docker Hub on DigitalOcean App Platform:

## 1. Login to DigitalOcean
- Go to the [DigitalOcean dashboard](https://cloud.digitalocean.com) and log in to your account.

## 2. Create a New App
- On the **App Platform** dashboard, click the **Create App** button.

## 3. Choose Your Source
- **Select "Deploy from Docker Hub"**:
  - In the source selection screen, you’ll be asked where your app is hosted. Choose **Docker Hub**.

## 4. Specify the Docker Image
- **Enter your Docker Hub details**:
  - You’ll need to provide the **Docker Hub image name** (e.g., `your-dockerhub-username/your-image-name:tag`).
  - If your image is public, you can enter it directly. If it's private, you'll need to authenticate with your Docker Hub credentials (username and password).

## 5. Configure Service
- **Set up your service**:
  - After specifying the image, DigitalOcean will display a configuration screen for your app.
  - Set **ports**: Ensure that the ports used in your container (e.g., port 80 or 443) are mapped correctly to the public-facing ports on App Platform.
  - **Environment Variables**: You can define any environment variables your application requires. For example, API keys, database URLs, etc.

    Example:
    - Environment variable: `MY_APP_ENV=production`

## 6. Set Up Scaling and Resources
- **Choose the size of your instance**: Select the resources you want to allocate for your app, such as CPU, memory, and disk size.
- **Scaling**: Set the number of instances (replicas) for high availability if needed.

## 7. Review and Deploy
- After reviewing all your settings (e.g., ports, environment variables, scaling), click **Deploy**.

## 8. Wait for Deployment
- DigitalOcean will now pull the image from Docker Hub and deploy it on the App Platform.
- It will also configure DNS for your domain and make the app publicly accessible if needed.

## 9. Monitor the Deployment
- Once the app is deployed, you can monitor logs, request traffic, and manage your app from the **App Platform dashboard**.

## Additional Considerations
- **Automatic Updates**: If you push a new version of the image to Docker Hub, DigitalOcean App Platform can automatically rebuild and redeploy your app, or you can manually trigger a rebuild.
- **Custom Domain**: If you want to use a custom domain, you can link your domain to your app through the App Platform UI.
- **Scaling**: You can scale your app by increasing the number of replicas or adjusting the allocated resources.
