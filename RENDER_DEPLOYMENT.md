# Render.com Deployment Guide

## Overview

Your salary tracker application is now configured for deployment on **Render.com** - a free hosting platform that supports Flask applications with persistent storage.

## What's Been Configured

✅ [render.yaml](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/render.yaml) - Render service configuration  
✅ [requirements.txt](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/requirements.txt) - Updated with gunicorn for production  
✅ [app.py](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/app.py) - Configured for production environment  
✅ [database.py](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/database.py) - Using SQLite with persistent disk

## Deployment Steps

### 1. Push Your Code to GitHub

```bash
cd /Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions

# Add and commit all changes
git add -A
git commit -m "Configure for Render.com deployment"

# Push to GitHub (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/salary-tracker.git
git branch -M main
git push -u origin main
```

### 2. Create Render Account

1. Go to [render.com](https://render.com)
2. Click **Get Started for Free**
3. Sign up with your GitHub account (recommended for easy deployment)

### 3. Deploy on Render

1. After signing in, click **New +** → **Web Service**
2. Connect your GitHub repository: `salary-tracker`
3. Render will auto-detect the configuration from `render.yaml`
4. Click **Create Web Service**

Render will automatically:
- Install dependencies from `requirements.txt`
- Start your app with gunicorn
- Provide a free `.onrender.com` URL
- Set up persistent disk for your SQLite database

### 4. Access Your App

After deployment completes (2-3 minutes), Render will provide a URL like:
`https://salary-tracker-xxxx.onrender.com`

## Features on Render Free Tier

✅ **Completely Free** - No credit card required  
✅ **Persistent Storage** - 1GB disk for SQLite database  
✅ **Auto-Deploy** - Updates automatically when you push to GitHub  
✅ **HTTPS** - Free SSL certificate included  
✅ **Custom Domain** - Can add your own domain (optional)

## Important Notes

> [!NOTE]
> **Cold Starts**: Free tier services spin down after 15 minutes of inactivity. First request after inactivity may take 30-60 seconds to wake up.

> [!TIP]
> **Keep It Awake**: Use a service like [UptimeRobot](https://uptimerobot.com) to ping your app every 5 minutes to prevent cold starts.

> [!IMPORTANT]
> **Database Persistence**: Your SQLite database is stored on a persistent disk. Data will be preserved across deployments and restarts.

## Troubleshooting

**If deployment fails:**
1. Check the Render logs in the dashboard
2. Verify `requirements.txt` has all dependencies
3. Ensure `render.yaml` is in the root directory

**If the app doesn't load:**
1. Check Render logs for errors
2. Verify the service is running (not sleeping)
3. Check that PORT environment variable is being used

## Next Steps

1. ✅ Push code to GitHub
2. ✅ Create Render account
3. ✅ Deploy web service
4. ✅ Test your application
5. (Optional) Set up custom domain
6. (Optional) Configure UptimeRobot to prevent cold starts

Your app is ready to deploy! 🚀
