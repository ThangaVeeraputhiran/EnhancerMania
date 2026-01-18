# 🚀 Deployment Guide - GitHub & Vercel

## Step 1: Push to GitHub

### 1.1 Create a New Repository on GitHub

1. Go to [GitHub](https://github.com) and log in
2. Click the "+" icon in the top right → "New repository"
3. Fill in the details:
   - **Repository name**: `noise-removal-project` (or your preferred name)
   - **Description**: "AI-powered noise removal and speech enhancement web application"
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have them)
4. Click "Create repository"

### 1.2 Push Your Code

Copy the commands from GitHub's "push an existing repository" section, or use these:

```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values!**

Example:
```bash
git remote add origin https://github.com/sharukhhere/noise-removal-project.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy to Vercel

### Option A: Deploy via Vercel Dashboard (Easiest)

1. **Go to [Vercel](https://vercel.com)**
2. Click "Sign Up" or "Log In" (use GitHub account for easy integration)
3. After logging in, click "Add New..." → "Project"
4. Click "Import Git Repository"
5. Authorize Vercel to access your GitHub account if prompted
6. Select your `noise-removal-project` repository
7. Configure your project:
   - **Framework Preset**: Other
   - **Root Directory**: ./
   - **Build Command**: Leave empty
   - **Output Directory**: Leave empty
   - **Install Command**: pip install -r requirements.txt
8. Click "Deploy"
9. Wait for deployment (usually 2-5 minutes)
10. Your app will be live at: `https://your-project-name.vercel.app`

### Option B: Deploy via Vercel CLI

1. **Install Vercel CLI**:
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy**:
```bash
vercel
```

4. **Follow the prompts**:
   - Set up and deploy? **Y**
   - Which scope? Choose your account
   - Link to existing project? **N**
   - What's your project's name? **noise-removal-project**
   - In which directory is your code located? **.**
   - Want to override settings? **N**

5. **Production Deployment**:
```bash
vercel --prod
```

---

## Step 3: Verify Deployment

### Check Your Live App

1. Visit the URL provided by Vercel (e.g., `https://noise-removal-project.vercel.app`)
2. Test the upload functionality
3. Try processing an audio file
4. Verify the download works

### Common Issues & Solutions

#### Issue: "Module not found" errors
**Solution**: Ensure `requirements.txt` includes all dependencies:
```bash
Flask==2.3.0
librosa==0.10.0
soundfile==0.12.1
scipy==1.11.0
numpy==1.24.0
matplotlib==3.7.0
```

#### Issue: File upload fails
**Solution**: Vercel has file size limits. For larger files:
1. Use Vercel Pro (500MB limit)
2. Or implement external storage (AWS S3, Cloudinary)

#### Issue: Processing timeout
**Solution**: Vercel serverless functions timeout at 10 seconds (free tier). For longer processing:
1. Upgrade to Pro (60 seconds)
2. Or use background jobs with external processing

#### Issue: Static files not loading
**Solution**: Check vercel.json routes configuration and ensure static folder is properly configured

---

## Step 4: Custom Domain (Optional)

### Add a Custom Domain

1. In Vercel Dashboard, go to your project
2. Click "Settings" → "Domains"
3. Add your custom domain (e.g., `noiseremoval.yourdomain.com`)
4. Follow DNS configuration instructions
5. Wait for DNS propagation (can take up to 48 hours)

---

## 📊 Monitor Your Deployment

### Vercel Dashboard Features:

- **Analytics**: View visitor statistics
- **Logs**: Check runtime logs for debugging
- **Deployments**: View deployment history
- **Settings**: Configure environment variables

### Access Logs:
```bash
vercel logs YOUR_DEPLOYMENT_URL
```

---

## 🔄 Update Your Deployment

Every time you push to GitHub, Vercel automatically redeploys:

```bash
# Make changes to your code
git add .
git commit -m "Update: description of changes"
git push origin main
```

Vercel will automatically detect the push and redeploy!

---

## 🎉 You're Done!

Your noise removal application is now:
- ✅ Stored on GitHub
- ✅ Live on the internet via Vercel
- ✅ Automatically deploying on every push
- ✅ Ready to share with the world!

### Share Your Project:

- GitHub: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`
- Live App: `https://your-project-name.vercel.app`

---

## 📝 Next Steps

1. **Add a README badge**: Update DEPLOYMENT_README.md with your Vercel URL
2. **Enable analytics**: Set up Vercel Analytics for visitor tracking
3. **Add environment variables**: For any API keys or secrets
4. **Set up monitoring**: Use Vercel's built-in monitoring tools
5. **Share**: Add the link to your portfolio, LinkedIn, or resume!

---

## 🆘 Need Help?

- Vercel Documentation: https://vercel.com/docs
- GitHub Help: https://docs.github.com
- Project Issues: Open an issue on your GitHub repository

Good luck with your deployment! 🚀
