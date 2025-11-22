# Firebase Deployment Guide

## Overview

Your salary tracker application has been configured for Firebase deployment using:
- **Firebase Cloud Functions** for the Flask backend
- **Firebase Firestore** for data persistence
- **Firebase Hosting** for static assets
- **Firebase Analytics** for usage tracking

## What's Been Configured

### Configuration Files

✅ [firebase.json](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/firebase.json) - Firebase project configuration  
✅ [.firebaserc](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/.firebaserc) - Links to your Firebase project  
✅ [main.py](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/main.py) - Cloud Function wrapper for Flask  
✅ [requirements.txt](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/requirements.txt) - Updated with Firebase dependencies  
✅ [.gitignore](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/.gitignore) - Excludes Firebase cache files

### Code Changes

✅ [database.py](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/database.py) - Migrated from SQLite to Firestore  
✅ [static/firebase-config.js](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/static/firebase-config.js) - Client-side Firebase initialization  
✅ [templates/base.html](file:///Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions/templates/base.html) - Added Firebase SDK script

## Deployment Steps

### 1. Install Firebase CLI

```bash
npm install -g firebase-tools
```

### 2. Login to Firebase

```bash
firebase login
```

This will open a browser window for authentication.

### 3. Deploy to Firebase

```bash
cd /Users/pravin/.gemini/antigravity/scratch/track_your_salary_and_deductions
firebase deploy
```

The deployment process will:
- Upload your Flask app as a Cloud Function
- Deploy static files to Firebase Hosting
- Set up routing to connect hosting to the function

### 4. Access Your App

After deployment completes, Firebase will provide URLs:
- **Hosting URL**: `https://track-your-income-deduction.web.app`
- **Function URL**: `https://us-central1-track-your-income-deduction.cloudfunctions.net/app`

Visit the Hosting URL to use your application.

## Important Notes

> [!IMPORTANT]
> **Firestore Security Rules**: Your Firestore database is currently open. You should set up security rules in the Firebase Console:
> 1. Go to [Firebase Console](https://console.firebase.google.com)
> 2. Select your project: `track-your-income-deduction`
> 3. Navigate to Firestore Database → Rules
> 4. Add authentication or restrict access as needed

> [!NOTE]
> **Cold Starts**: Cloud Functions may have a delay (1-3 seconds) on first request after inactivity. Subsequent requests will be faster.

> [!WARNING]
> **Data Migration**: Your existing SQLite data (`salary_tracker.db`) will NOT be automatically migrated to Firestore. You'll start with an empty database. If you need to migrate existing data, let me know.

## Testing Checklist

After deployment, verify:
- [ ] Application loads at the hosting URL
- [ ] Can add a new salary entry
- [ ] Entry appears in the dashboard
- [ ] Can edit an existing entry
- [ ] Can delete an entry
- [ ] Chart displays correctly
- [ ] Data persists after page refresh

## Troubleshooting

**If deployment fails:**
1. Check that you're logged into Firebase: `firebase login`
2. Verify project exists: `firebase projects:list`
3. Check deployment logs: `firebase deploy --debug`

**If data doesn't persist:**
1. Check Firestore in Firebase Console
2. Verify security rules allow writes
3. Check browser console for errors

## Next Steps

1. Deploy using the commands above
2. Test the application thoroughly
3. Set up Firestore security rules
4. (Optional) Migrate existing SQLite data to Firestore
5. (Optional) Set up custom domain in Firebase Hosting
