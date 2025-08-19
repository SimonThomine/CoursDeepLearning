# Language Switching Implementation

This document explains how the multilingual language switching works in the Jupyter Book.

## 🔧 How It Works

### 1. **Smart URL Detection**
The JavaScript automatically detects the deployment environment:
- **Local development**: `file://` or `localhost`
- **GitHub Pages**: `username.github.io/repository-name`
- **Custom domain**: Any other domain

### 2. **Path Transformation**
When switching languages, the system:
1. Detects current language from URL path (`/fr/` or `/en/`)
2. Replaces language segment with target language
3. Preserves the rest of the path structure

### 3. **Fallback Handling**
If no language is detected in the current path:
- Navigates to the target language root page
- Maintains proper base URL for different deployments

## 📍 URL Structure

### Local Development
```
file:///path/to/project/
├── index.html                    # Language selector
├── _build_fr/_build/html/        # French site
│   ├── index.html
│   └── 01_Fondations/...
└── _build_en/_build/html/        # English site
    ├── index.html
    └── 01_Fondations/...
```

### GitHub Pages
```
https://username.github.io/repository-name/
├── index.html                    # Language selector
├── fr/                          # French site
│   ├── index.html
│   └── 01_Fondations/...
└── en/                          # English site
    ├── index.html
    └── 01_Fondations/...
```

## 🎯 Implementation Details

### Footer Language Switcher
Each page includes a footer with language switching buttons:

```html
<div id="language-switcher">
  <span>🌐 Language / Langue:</span>
  <a href="#" onclick="switchToEnglish()">🇺🇸 English</a>
  <a href="#" onclick="switchToFrench()">🇫🇷 Français</a>
</div>
```

### JavaScript Functions
```javascript
function getBaseUrl() {
  // Detects GitHub Pages vs other deployments
  if (window.location.hostname.includes('github.io')) {
    const pathParts = window.location.pathname.split('/');
    if (pathParts.length >= 2) return '/' + pathParts[1];
  }
  return '';
}

function switchToLanguage(targetLang) {
  // Transforms current URL to target language
  const baseUrl = getBaseUrl();
  let currentPath = window.location.pathname;
  let newPath;
  
  if (currentPath.includes('/fr/')) {
    newPath = currentPath.replace('/fr/', '/' + targetLang + '/');
  } else if (currentPath.includes('/en/')) {
    newPath = currentPath.replace('/en/', '/' + targetLang + '/');
  } else {
    newPath = baseUrl + '/' + targetLang + '/';
  }
  
  window.location.href = newPath;
}
```

## 🚀 Deployment Scenarios

### 1. **Local Testing**
```bash
cd CoursDeepLearningBook
python build_multilingual.py
open index.html
```

### 2. **GitHub Pages**
```bash
./deploy.sh
# Push docs/ folder to GitHub Pages
```

### 3. **Custom Domain**
The language switching automatically adapts to any domain structure.

## 🔍 Testing

Use the test page to verify language switching:
```bash
open test_language_switching.html
```

This shows:
- Current URL and detected base URL
- Language detection results
- Preview of URL transformations

## 🎨 Visual Indicators

- **Current language** is highlighted in green
- **Other language** appears in gray
- **Hover effects** provide visual feedback
- **Smooth transitions** enhance user experience

## 🛠️ Troubleshooting

### Common Issues

1. **Language switching doesn't work**
   - Check browser console for JavaScript errors
   - Verify the target language files exist
   - Test with the debugging page

2. **Wrong URLs generated**
   - Check if deployment matches expected structure
   - Verify base URL detection logic
   - Test in different environments

3. **Missing pages in target language**
   - Some English pages may not exist yet
   - Falls back to language root page
   - Use translation helper script to create templates

### Debug Mode
Add this to browser console to see URL transformations:
```javascript
console.log('Current:', window.location.href);
console.log('Base URL:', getBaseUrl());
console.log('Language:', getCurrentLanguage());
```

## 📝 Future Enhancements

Potential improvements:
- **Page equivalence mapping** for better cross-language navigation
- **Language preference storage** in localStorage
- **Automatic language detection** based on browser settings
- **Translation progress indicators**

---

*The language switching system is designed to be robust and work across different deployment scenarios while providing a smooth user experience.*