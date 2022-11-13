# Image Hosting

![deployment status](https://github.com/MauroMontan/image-hosting/actions/workflows/deploy.yml/badge.svg)

## Try it

Use the Deta button to deploy the application in your deta environment.

> See Endpoint section to try it.

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/MauroMontan/image-hosting)

### Endpoints

For now there are two endpoints, one for upload an image, and other to download

| Name           | Type | Endpoint                                                |
| -------------- | ---- | ------------------------------------------------------- |
| Upload Image   | POST | https://{YOUR_DOMAIN}.deta.dev/images/{FILENAME}        |
| Download Image | GET  | https://{YOUR_DOMAIN}.deta.dev/images/upload/{FILENAME} |

### CI/CD

- This project is using the [deta deploy action](https://github.com/BogDAAAMN/deta-deploy-action) for a better deployment. Check the deploy workflow file to see how is implemented for this project.
