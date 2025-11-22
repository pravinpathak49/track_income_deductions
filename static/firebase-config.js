// Firebase Configuration
// Initialize Firebase for analytics and future features

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDS6wOy57QyzeWLNqveMYqTLJSuDRGFSVg",
    authDomain: "track-your-income-deduction.firebaseapp.com",
    projectId: "track-your-income-deduction",
    storageBucket: "track-your-income-deduction.firebasestorage.app",
    messagingSenderId: "308782879402",
    appId: "1:308782879402:web:0f01049951f3bf4cca76d3",
    measurementId: "G-1SB6CF4SG9"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

console.log("Firebase initialized successfully");
