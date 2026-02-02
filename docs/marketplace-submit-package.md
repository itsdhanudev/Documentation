# Publishing Packages to the ITsMagic Marketplace (GitHub)

This guide explains, step by step, how to publish your package to the ITsMagic Marketplace. The marketplace is hosted on GitHub, so you will send a Pull Request (PR) with your package information.

Repository:
```
https://github.com/ITsMagic-Software/Packages-Manifest
```

## Overview (what you will do)

1. Create a public GitHub repository with your package content.
2. Add your package entry to `database.json` in the Marketplace repo.
3. Upload your media (thumbnail + images) in the correct folder.
4. Open a Pull Request with your changes.

## Step 1: Create a public repository for your package

Your package files must be in a public GitHub repository (on your own account).

- Create a new public repo on GitHub.
- Upload the package files (scenes, scripts, assets, etc.).
- Copy the repository URL. You will use it in `repositoryURL`.

## Step 2: Fork the Marketplace repository

1. Open the Marketplace repo:
```
https://github.com/ITsMagic-Software/Packages-Manifest
```
2. Click **Fork** to create a copy in your GitHub account.
3. Open your fork and clone it to your computer.

## Step 3: Add your package to database.json

Open `database.json` and add a new product entry using this structure:

```json
{
  "id": "6cb01fa1-a3dc-4cf8-a7c6-e115a36d8806",
  "userName": "ITsMagic",
  "titleB64": "Q2F2ZSBjaHVyY2ggKEhJR0ggR1JBUEhJQ1Mp",
  "descriptionB64": "VW5kZXJncm91bmQgY2h1cmNoIHByb2plY3Qgd2l0aCBhbWF6aW5nIGdyYXBoY2lzLg==",
  "tags": "graphics,afpp",
  "version": 1,
  "repositoryURL": "https://github.com/ITsMagic-Software/Package-CaveChurch",
  "isTemplate": false,
  "mediaFolder": "itsmagic/cavechurch",
  "thumbnail": "thumb.jpg",
  "images": [
    "img1.jpg",
    "img2.jpg",
    "img3.jpg",
    "img4.jpg"
  ]
}
```

### Field explanations (simple)

- `id`: A unique ID for the package (use a UUID).
- `userName`: Your GitHub username.
- `titleB64`: The package title in Base64.
- `descriptionB64`: The package description in Base64.
- `tags`: Comma-separated tags to help search.
- `version`: Start at `1` and increase when you update.
- `repositoryURL`: Your public GitHub repo with the package files.
- `isTemplate`: `true` if the package is a template, otherwise `false`.
- `mediaFolder`: The folder where your images will be stored (see next step).
- `thumbnail`: The main image for the package.
- `images`: Extra images (screenshots) for the package.

### How to create Base64 for title/description

You can use any Base64 encoder. For example:

- Title: `Cave church (HIGH GRAPHICS)`
- Description: `Underground church project with amazing graphics.`

Then convert each one to Base64 and place the result in `titleB64` and `descriptionB64`.

## Step 4: Add your images to the media folder

**Image requirements**
- Max size: 1 MB per image
- Accepted formats: JPG or PNG
- Maximum: 8 images per product

Inside the Marketplace repository, there is a `media` folder. Create this path:

```
media/yourusername/yourpackage/
```

Example:

```
media/itsmagic/cavechurch/
```

Put your `thumbnail` image and all `images` inside this folder.

## Step 5: Open a Pull Request

1. Commit your changes (database.json + media files).
2. Push to your fork.
3. Open a Pull Request to:
   - Base repository: `ITsMagic-Software/Packages-Manifest`
   - Compare repository: your fork
4. Describe your package and submit.

After review, your package will be published in the Marketplace.

## Moderation and approval

Your Pull Request can be approved or rejected by Marketplace moderators. If it is rejected, the moderators will leave feedback explaining what you need to change to get approval.
