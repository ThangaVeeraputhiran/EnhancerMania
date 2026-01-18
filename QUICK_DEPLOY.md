# 🚀 QUICK DEPLOYMENT COMMANDS

## Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. Create a repository (name it whatever you want, e.g., "noise-removal-project")
3. **DO NOT** add README, .gitignore, or license (we already have them)
4. Click "Create repository"

---

## Step 2: Push to GitHub

Copy and paste these commands ONE BY ONE (replace YOUR_USERNAME and YOUR_REPO):

```powershell
# Check current status
git status

# Add remote repository (REPLACE WITH YOUR GITHUB URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Example:
# git remote add origin https://github.com/sharukhhere/noise-removal-project.git

# Verify remote was added
git remote -v

# Push to GitHub
git push -u origin main
```

---

## Step 3: Deploy to Vercel

### Option A: Via Web Interface (EASIEST - RECOMMENDED)

1. Go to: https://vercel.com/signup
2. Sign up/Login with GitHub
3. Click "Add New..." → "Project"
4. Import your repository
5. Click "Deploy"
6. Done! Your app will be live in 2-3 minutes

### Option B: Via Command Line

```powershell
# Install Vercel CLI (if you have Node.js)
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Deploy to production
vercel --prod
```

---

## 🎉 After Deployment

Your app will be live at:
- `https://YOUR-PROJECT-NAME.vercel.app`

Every time you push to GitHub, Vercel automatically redeploys!

---

## 📝 To Update Your Code Later

```powershell
# Make your changes, then:
git add .
git commit -m "Your update message"
git push origin main
```

Vercel will auto-deploy the changes!

---

## ✅ Checklist

- [ ] Created GitHub repository
- [ ] Pushed code to GitHub
- [ ] Created Vercel account
- [ ] Deployed to Vercel
- [ ] Tested live app
- [ ] Shared the link!

---

## 🆘 If You Get Stuck

### Error: "remote origin already exists"
```powershell
git remote remove origin
# Then add it again
git remote add origin YOUR_GITHUB_URL
```

### Error: "failed to push"
```powershell
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Can't find git command
Install Git from: https://git-scm.com/download/win

---

## 📞 Your Project URLs

Fill these in after deployment:

- GitHub: ___________________________________
- Vercel: ___________________________________
- Custom Domain (optional): ________________

---

Good luck! 🚀
