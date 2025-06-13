# GitHub Actions Workflows Documentation

This directory contains GitHub Actions workflows for continuous integration, testing, and deployment.

## Workflow Files

### `ci.yml` - Main CI Workflow
The primary continuous integration workflow that runs on all pushes and pull requests.

**Key Features:**
- Multi-platform testing (Ubuntu, Windows, macOS)
- Node.js version matrix testing
- Security scanning with CodeQL
- Dependency vulnerability checks
- Code quality analysis
- Debug mode with tmate for troubleshooting

**When to use:** This is your main workflow that should run on every code change.

### `node.yml` - Node.js Specific Workflow
Specialized workflow for Node.js projects with npm package publishing capabilities.

**Key Features:**
- Comprehensive Node.js version testing
- Coverage reporting to Codecov
- Automated npm publishing on version changes
- E2E test support

**When to use:** For Node.js projects that need npm publishing or more detailed Node.js-specific testing.

### `python.yml` - Python Specific Workflow
Specialized workflow for Python projects with PyPI publishing capabilities.

**Key Features:**
- Python version matrix (3.8-3.12)
- Code formatting with Black
- Type checking with mypy
- Linting with flake8
- PyPI package publishing

**When to use:** For Python projects that need PyPI publishing or Python-specific tooling.

### `release.yml` - Release Automation
Handles version releases and changelog generation.

**Key Features:**
- Automated GitHub Release creation
- Changelog generation from commit history
- Source and binary archive creation
- CHANGELOG.md file updates
- Support for pre-releases (alpha/beta)

**When to use:** When creating new version releases of your project.

## Common Workflow Patterns

### 1. Adding a New Check to CI
Edit `ci.yml` and add a new step to the appropriate job:
```yaml
- name: My New Check
  run: |
    echo "Running my custom check"
    npm run my-check
```

### 2. Adding Secrets
1. Go to repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add the secret name and value
4. Reference in workflow: `${{ secrets.YOUR_SECRET_NAME }}`

### 3. Conditional Execution
Run steps only under certain conditions:
```yaml
- name: Deploy
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  run: npm run deploy
```

### 4. Manual Workflow Triggers
Add workflow_dispatch to enable manual runs:
```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deployment environment'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production
```

## Debugging Workflows

### Using tmate for Interactive Debugging
1. Go to Actions tab in GitHub
2. Select the CI workflow
3. Click "Run workflow"
4. Check "Run the build with tmate debugging enabled"
5. The workflow will pause and provide SSH access

### Viewing Workflow Logs
- Click on any workflow run in the Actions tab
- Expand job steps to see detailed logs
- Use the search function to find specific errors

### Common Issues and Solutions

**Issue:** Workflow not triggering
- Check branch protection rules
- Verify workflow file syntax
- Ensure correct event triggers

**Issue:** Permission denied errors
- Add necessary permissions to workflow:
```yaml
permissions:
  contents: write
  pull-requests: write
```

**Issue:** Secrets not working
- Verify secret names match exactly (case-sensitive)
- Check secret is available for the branch/environment
- Secrets are not available in pull requests from forks

## Best Practices

1. **Use Action Versions**: Always specify action versions
   ```yaml
   uses: actions/checkout@v4  # Good
   uses: actions/checkout@main  # Avoid
   ```

2. **Cache Dependencies**: Speed up workflows
   ```yaml
   - uses: actions/cache@v3
     with:
       path: ~/.npm
       key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
   ```

3. **Fail Fast Strategy**: Stop all matrix jobs if one fails
   ```yaml
   strategy:
     fail-fast: true
     matrix:
       node: [14, 16, 18]
   ```

4. **Timeout Settings**: Prevent hanging workflows
   ```yaml
   jobs:
     test:
       timeout-minutes: 10
   ```

5. **Artifact Management**: Clean up old artifacts
   ```yaml
   - uses: actions/upload-artifact@v3
     with:
       retention-days: 7  # Delete after 7 days
   ```

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [Action Security Best Practices](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)