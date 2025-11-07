# 🚀 Deployment Guide

This guide covers multiple deployment options for the Euro Trends BMW x ISM Dashboard.

## 📋 Table of Contents
1. [Docker Deployment](#docker-deployment)
2. [Manual Production Deployment](#manual-production-deployment)
3. [Cloud Deployment Options](#cloud-deployment-options)
4. [Environment Variables](#environment-variables)
5. [Performance Optimization](#performance-optimization)

---

## 🐳 Docker Deployment (Recommended)

### Prerequisites
- Docker 20.10+
- Docker Compose 2.0+

### Quick Start
```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Access Points
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- API Docs: http://localhost:5000/api/status

### Configuration
Edit `docker-compose.yml` to customize:
```yaml
services:
  backend:
    environment:
      - FLASK_ENV=production
      - MAX_CONTENT_LENGTH=50MB
  frontend:
    environment:
      - VITE_API_URL=http://localhost:5000
```

---

## 🔧 Manual Production Deployment

### Backend (Flask)

#### Option 1: Gunicorn (Linux/Mac)
```bash
cd backend
pip install gunicorn

# Development
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app

# Production with auto-reload
gunicorn --bind 0.0.0.0:5000 \
  --workers 4 \
  --timeout 120 \
  --access-logfile - \
  --error-logfile - \
  app:app
```

#### Option 2: Waitress (Windows)
```bash
cd backend
pip install waitress

# Run
waitress-serve --port=5000 --threads=4 app:app
```

#### Option 3: uWSGI
```bash
pip install uwsgi
uwsgi --http :5000 --wsgi-file app.py --callable app --processes 4
```

### Frontend (React)

#### Build for Production
```bash
cd frontend
npm run build
# Output in dist/ folder
```

#### Serve with Nginx
```nginx
# /etc/nginx/sites-available/euro-trends

server {
    listen 80;
    server_name your-domain.com;
    root /var/www/euro-trends/frontend/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/euro-trends /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

#### Serve with Apache
```apache
# /etc/apache2/sites-available/euro-trends.conf

<VirtualHost *:80>
    ServerName your-domain.com
    DocumentRoot /var/www/euro-trends/frontend/dist

    <Directory /var/www/euro-trends/frontend/dist>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
        RewriteEngine On
        RewriteBase /
        RewriteRule ^index\.html$ - [L]
        RewriteCond %{REQUEST_FILENAME} !-f
        RewriteCond %{REQUEST_FILENAME} !-d
        RewriteRule . /index.html [L]
    </Directory>

    ProxyPass /api http://localhost:5000/api
    ProxyPassReverse /api http://localhost:5000/api
</VirtualHost>
```

---

## ☁️ Cloud Deployment Options

### 1. Heroku

#### Backend
```bash
# Create Heroku app
heroku create euro-trends-backend

# Add buildpack
heroku buildpacks:add heroku/python

# Deploy
git subtree push --prefix backend heroku main

# Configure
heroku config:set FLASK_ENV=production
```

**Procfile** (create in backend/):
```
web: gunicorn app:app
```

#### Frontend
```bash
# Deploy to Heroku
cd frontend
npm run build

# Use heroku-static buildpack
heroku create euro-trends-frontend
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-static
git push heroku main
```

**static.json** (create in frontend/):
```json
{
  "root": "dist/",
  "routes": {
    "/**": "index.html"
  }
}
```

### 2. AWS Deployment

#### Backend (AWS Lambda + API Gateway)
```bash
# Install Zappa
pip install zappa

# Initialize
zappa init

# Deploy
zappa deploy production
```

**zappa_settings.json**:
```json
{
  "production": {
    "app_function": "app.app",
    "aws_region": "us-east-1",
    "runtime": "python3.13",
    "s3_bucket": "euro-trends-backend"
  }
}
```

#### Frontend (AWS S3 + CloudFront)
```bash
# Build
npm run build

# Upload to S3
aws s3 sync dist/ s3://euro-trends-frontend --delete

# Create CloudFront distribution
aws cloudfront create-distribution \
  --origin-domain-name euro-trends-frontend.s3.amazonaws.com
```

### 3. Google Cloud Platform

#### Backend (Cloud Run)
```bash
# Build container
gcloud builds submit --tag gcr.io/PROJECT_ID/euro-trends-backend

# Deploy
gcloud run deploy euro-trends-backend \
  --image gcr.io/PROJECT_ID/euro-trends-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

#### Frontend (Firebase Hosting)
```bash
# Install Firebase CLI
npm install -g firebase-tools

# Initialize
firebase init hosting

# Build and deploy
npm run build
firebase deploy
```

### 4. Azure Deployment

#### Backend (Azure App Service)
```bash
# Create app
az webapp create \
  --resource-group euro-trends-rg \
  --plan euro-trends-plan \
  --name euro-trends-backend \
  --runtime "PYTHON:3.13"

# Deploy
az webapp up \
  --name euro-trends-backend \
  --location eastus
```

#### Frontend (Azure Static Web Apps)
```bash
# Deploy via GitHub Actions (automatic)
az staticwebapp create \
  --name euro-trends-frontend \
  --resource-group euro-trends-rg \
  --source https://github.com/user/repo \
  --location eastus
```

### 5. Vercel (Frontend Only)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd frontend
vercel --prod
```

**vercel.json**:
```json
{
  "rewrites": [
    { "source": "/api/(.*)", "destination": "https://your-backend.herokuapp.com/api/$1" },
    { "source": "/(.*)", "destination": "/" }
  ]
}
```

### 6. Netlify (Frontend Only)
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
cd frontend
npm run build
netlify deploy --prod --dir=dist
```

**netlify.toml**:
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/api/*"
  to = "https://your-backend.herokuapp.com/api/:splat"
  status = 200

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

---

## 🔐 Environment Variables

### Backend (.env)
```bash
# Flask configuration
FLASK_ENV=production
FLASK_APP=app.py
SECRET_KEY=your-secret-key-here

# CORS
CORS_ORIGINS=https://your-frontend-domain.com

# File upload
MAX_CONTENT_LENGTH=52428800  # 50MB
UPLOAD_FOLDER=./uploads

# Data
DATA_FILE=BMW Data Set for WebApp.xlsx

# Logging
LOG_LEVEL=INFO
```

### Frontend (.env.production)
```bash
# API endpoint
VITE_API_URL=https://your-backend-domain.com/api

# Feature flags
VITE_ENABLE_ANALYTICS=true
VITE_ENABLE_DEBUG=false
```

---

## ⚡ Performance Optimization

### Backend
```python
# Enable caching
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/api/data/summary')
@cache.cached(timeout=300)  # 5 minutes
def get_summary():
    # ...
```

### Frontend
```typescript
// Lazy load routes
const Overview = lazy(() => import('./components/Overview'))
const Explorer = lazy(() => import('./components/Explorer'))

// Use React.memo for expensive components
const ExpensiveChart = React.memo(ChartComponent)
```

### Database (Optional)
```bash
# Use PostgreSQL for better performance
pip install psycopg2-binary

# Connection pooling
from sqlalchemy import create_engine
engine = create_engine('postgresql://...', pool_size=10)
```

### CDN
```html
<!-- Use CDN for static assets -->
<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
```

---

## 🔒 Security Best Practices

1. **Environment Variables**: Never commit `.env` files
2. **HTTPS**: Always use SSL in production
3. **CORS**: Restrict to specific origins
4. **Rate Limiting**: Implement API rate limits
5. **Input Validation**: Sanitize all user inputs
6. **Dependencies**: Keep packages updated
7. **Secrets**: Use secret management (AWS Secrets Manager, Azure Key Vault)

```python
# Rate limiting
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/upload')
@limiter.limit("10 per hour")
def upload_file():
    # ...
```

---

## 📊 Monitoring

### Application Monitoring
- **Sentry**: Error tracking
- **New Relic**: Performance monitoring
- **Datadog**: Full-stack observability

### Setup Sentry
```bash
pip install sentry-sdk[flask]
```

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)
```

---

## 🆘 Troubleshooting

### Common Issues

**CORS Errors**
```python
# backend/app.py
from flask_cors import CORS
CORS(app, origins=['https://your-frontend.com'])
```

**Port Already in Use**
```bash
# Find process
lsof -i :5000  # Mac/Linux
netstat -ano | findstr :5000  # Windows

# Kill process
kill -9 <PID>  # Mac/Linux
taskkill /PID <PID> /F  # Windows
```

**Memory Issues**
```python
# Limit data processing
df = pd.read_excel('data.xlsx', nrows=10000)
```

---

## 📚 Additional Resources

- [Flask Deployment Options](https://flask.palletsprojects.com/en/latest/deploying/)
- [Vite Production Build](https://vitejs.dev/guide/build.html)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Nginx Configuration](https://nginx.org/en/docs/)

---

**Need help? Open an issue on GitHub!**
