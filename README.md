# Github Action Test

[![CI](https://github.com/goodlookingprokim/Github_Action_Test/actions/workflows/ci.yml/badge.svg)](https://github.com/goodlookingprokim/Github_Action_Test/actions/workflows/ci.yml)
[![Node.js CI](https://github.com/goodlookingprokim/Github_Action_Test/actions/workflows/node.yml/badge.svg)](https://github.com/goodlookingprokim/Github_Action_Test/actions/workflows/node.yml)
[![Python CI](https://github.com/goodlookingprokim/Github_Action_Test/actions/workflows/python.yml/badge.svg)](https://github.com/goodlookingprokim/Github_Action_Test/actions/workflows/python.yml)
[![Release](https://github.com/goodlookingprokim/Github_Action_Test/actions/workflows/release.yml/badge.svg)](https://github.com/goodlookingprokim/Github_Action_Test/actions/workflows/release.yml)

A repository for testing and demonstrating GitHub Actions workflows.

## 🚀 Available Workflows

### 1. CI Workflow (`ci.yml`)
- **Triggers**: Push to main/develop branches, Pull Requests, Manual dispatch
- **Features**:
  - Multi-OS testing (Ubuntu, Windows, macOS)
  - Node.js version matrix (18.x, 20.x)
  - Dependency caching
  - Security scanning with CodeQL
  - Code quality checks
  - Debug mode with tmate

### 2. Node.js Workflow (`node.yml`)
- **Purpose**: Specialized workflow for Node.js projects
- **Features**:
  - Multiple Node.js versions (16.x, 18.x, 20.x)
  - Test coverage with Codecov
  - NPM package publishing (requires NPM_TOKEN secret)
  - E2E testing support

### 3. Python Workflow (`python.yml`)
- **Purpose**: Specialized workflow for Python projects
- **Features**:
  - Multiple Python versions (3.8 - 3.12)
  - Code formatting with Black
  - Type checking with mypy
  - Linting with flake8
  - PyPI publishing (requires PYPI_API_TOKEN secret)

### 4. Release Workflow (`release.yml`)
- **Triggers**: Git tags (v*.*.* pattern) or manual dispatch
- **Features**:
  - Automated changelog generation
  - GitHub Release creation
  - Source and binary archives
  - CHANGELOG.md updates

## 🛠️ Setup Instructions

### 1. Basic Setup
No additional setup required for basic CI workflows.

### 2. For NPM Publishing
Add `NPM_TOKEN` secret to your repository:
1. Go to Settings → Secrets and variables → Actions
2. Add new repository secret named `NPM_TOKEN`
3. Add your NPM authentication token

### 3. For PyPI Publishing
Add `PYPI_API_TOKEN` secret to your repository:
1. Go to Settings → Secrets and variables → Actions
2. Add new repository secret named `PYPI_API_TOKEN`
3. Add your PyPI API token

### 4. For Security Scanning
CodeQL is automatically enabled. No additional setup required.

## 📝 Usage Examples

### Running CI on Push
Simply push your code to main or create a pull request:
```bash
git add .
git commit -m "feat: add new feature"
git push origin main
```

### Creating a Release
Create and push a version tag:
```bash
git tag v1.0.0
git push origin v1.0.0
```

Or use the manual workflow dispatch from the Actions tab.

### Debugging Failed Workflows
Enable debug mode when manually triggering the CI workflow:
1. Go to Actions tab
2. Select "CI" workflow
3. Click "Run workflow"
4. Check "Run the build with tmate debugging enabled"
5. Click "Run workflow"

## 🧪 Testing Locally

You can test GitHub Actions locally using [act](https://github.com/nektos/act):
```bash
# Install act
brew install act  # macOS
# or follow instructions at https://github.com/nektos/act

# Run CI workflow
act push

# Run specific job
act -j test
```

## 📚 Best Practices

1. **Always use caching** for dependencies to speed up workflows
2. **Use matrix builds** to test across multiple versions/platforms
3. **Set appropriate timeouts** to prevent hanging workflows
4. **Use secrets** for sensitive data (tokens, passwords)
5. **Enable branch protection** to require CI passes before merging

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).