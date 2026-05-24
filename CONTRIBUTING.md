# Contributing to Euro Trends BMW x ISM Project

Thank you for considering contributing to this project! 🎉

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)

## 🤝 Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code:
- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive criticism
- Respect differing viewpoints

## 💡 How Can I Contribute?

### Reporting Bugs
- Check if the bug has already been reported in [Issues](https://github.com/pratheekdk9919/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data/issues)
- Include:
  - Clear description of the issue
  - Steps to reproduce
  - Expected vs actual behavior
  - Screenshots if applicable
  - Environment details (OS, browser, Python/Node versions)

### Suggesting Features
- Open an issue with the `enhancement` label
- Describe the feature and its benefits
- Provide examples of how it would work

### Code Contributions
- Fork the repository
- Create a feature branch
- Make your changes
- Write/update tests
- Submit a pull request

## 🛠️ Development Setup

### Prerequisites
```bash
Python 3.13+
Node.js 16+
Git
```

### Local Development
```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data.git
cd Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data

# Backend setup
cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py

# Frontend setup (new terminal)
cd frontend
npm install
npm run dev
```

## 🔄 Pull Request Process

1. **Update Documentation**: Update README.md if you change functionality
2. **Add Tests**: Include tests for new features
3. **Follow Style Guide**: Match existing code style
4. **Update CHANGELOG**: Add entry for your changes
5. **Link Issues**: Reference related issues in PR description
6. **Request Review**: Tag maintainers for review

### PR Title Format
```
[Type] Brief description

Types: feat, fix, docs, style, refactor, test, chore
Examples:
- [feat] Add export to CSV functionality
- [fix] Correct salary aggregation logic
- [docs] Update API endpoint documentation
```

## 📝 Coding Standards

### Python (Backend)
```python
# Follow PEP 8
# Use type hints
def calculate_average(salaries: list[float]) -> float:
    """Calculate average salary with proper documentation."""
    return sum(salaries) / len(salaries)

# Use meaningful variable names
filtered_data = [x for x in data if x['Country'] == 'Germany']
```

### TypeScript/React (Frontend)
```typescript
// Use TypeScript interfaces
interface SalaryData {
  role: string
  salary: number
}

// Functional components with hooks
const Dashboard: React.FC = () => {
  const [data, setData] = useState<SalaryData[]>([])
  // ...
}

// Use descriptive names
const handleFileUpload = async (e: ChangeEvent<HTMLInputElement>) => {
  // ...
}
```

### Commit Messages
```
type(scope): description

Examples:
feat(forecast): add confidence interval calculation
fix(api): resolve CORS issue for upload endpoint
docs(readme): update installation instructions
style(frontend): improve button hover effects
refactor(backend): optimize data loading performance
test(forecast): add unit tests for prediction model
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v
pytest tests/test_forecasting.py  # specific test
```

### Frontend Tests
```bash
cd frontend
npm test
npm test -- --coverage  # with coverage
```

## 📚 Additional Resources

- [React Documentation](https://react.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Plotly Documentation](https://plotly.com/javascript/)

## ❓ Questions?

Feel free to open a discussion or reach out to maintainers:
- GitHub Issues: [Open an issue](https://github.com/pratheekdk9919/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data/issues)
- Project: BMW x ISM Field Project Team

---

**Thank you for contributing! 🙏**
