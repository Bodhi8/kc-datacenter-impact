# Contributing to Kansas City Data Center Impact Analysis

Thank you for your interest in contributing! This project benefits from community input, validation, and extension.

## 🎯 Ways to Contribute

### 1. Report Issues
Found a bug or error in the analysis?
- Check [existing issues](https://github.com/yourusername/kc-datacenter-impact/issues) first
- Open a new issue with clear description
- Include code to reproduce if applicable

### 2. Validate Models
Run the models with your own assumptions:
- Document your inputs and results
- Compare outputs with published findings
- Share discrepancies via pull request or issue

### 3. Extend Analysis
Add new features or perspectives:
- Additional data sources
- Alternative modeling approaches
- Regional comparisons
- Interactive visualizations

### 4. Improve Documentation
Help others understand the work:
- Clarify technical explanations
- Add examples or tutorials
- Fix typos or broken links
- Translate to other languages

### 5. Update Data
As new information becomes available:
- Evergy rate case decisions
- Data center announcements
- KCC/PSC regulatory changes
- Actual consumption data

## 🔧 Development Process

### Setting Up Development Environment

1. **Fork the repository**
```bash
# Click "Fork" button on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/kc-datacenter-impact.git
cd kc-datacenter-impact
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

4. **Run tests**
```bash
pytest tests/
```

### Making Changes

1. **Create a branch**
```bash
git checkout -b feature/your-feature-name
# Or: bugfix/issue-description
```

2. **Make your changes**
- Follow existing code style (Black formatting)
- Add tests for new functionality
- Update documentation

3. **Test your changes**
```bash
# Run tests
pytest tests/

# Format code
black src/

# Check linting
flake8 src/
```

4. **Commit changes**
```bash
git add .
git commit -m "Clear description of changes"
```

5. **Push and create pull request**
```bash
git push origin feature/your-feature-name
# Then create PR on GitHub
```

## 📝 Code Style Guidelines

### Python Code
- Follow [PEP 8](https://pep8.org/) style guide
- Use [Black](https://black.readthedocs.io/) for automatic formatting
- Maximum line length: 100 characters
- Use type hints where practical

**Example:**
```python
def calculate_bill_impact(
    current_rate: float,
    future_rate: float,
    monthly_kwh: int = 1000
) -> dict:
    """
    Calculate household bill impact from rate changes.
    
    Args:
        current_rate: Current electricity rate ($/kWh)
        future_rate: Projected future rate ($/kWh)
        monthly_kwh: Monthly consumption (default: 1000)
    
    Returns:
        Dictionary with current bill, future bill, and increase
    """
    current_bill = current_rate * monthly_kwh
    future_bill = future_rate * monthly_kwh
    
    return {
        'current_bill': current_bill,
        'future_bill': future_bill,
        'monthly_increase': future_bill - current_bill,
        'annual_increase': (future_bill - current_bill) * 12
    }
```

### Documentation
- Use docstrings for all functions/classes
- Follow [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for docstrings
- Update README.md if adding features
- Add examples for new functionality

### Commit Messages
Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: Add Monte Carlo uncertainty analysis
fix: Correct wholesale-to-retail conversion factor
docs: Update methodology with new data sources
test: Add validation tests for SVR model
refactor: Simplify demand forecasting code
```

## 🧪 Testing

### Writing Tests
Add tests for new functionality:

```python
# tests/test_models.py
import pytest
from src.kc_ml_models import calculate_bill_impact

def test_bill_impact_calculation():
    """Test bill impact calculation with known values."""
    result = calculate_bill_impact(
        current_rate=0.18,
        future_rate=0.41,
        monthly_kwh=1000
    )
    
    assert result['current_bill'] == 180
    assert result['future_bill'] == 410
    assert result['monthly_increase'] == 230
    assert result['annual_increase'] == 2760
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_models.py

# Run with coverage
pytest --cov=src tests/
```

## 📊 Data Contribution Guidelines

### Adding New Data Sources

1. **Document provenance**
   - Source organization
   - URL and access date
   - License/usage terms
   - Processing steps

2. **Update data_sources.md**
   ```markdown
   ### New Data Source Name
   - **Source:** Organization Name
   - **URL:** https://example.com/data
   - **Date Accessed:** YYYY-MM-DD
   - **License:** Public domain / CC-BY / etc.
   - **Description:** What the data contains
   - **Processing:** How it was cleaned/transformed
   ```

3. **Include raw and processed versions**
   - `data/raw/` - Original unmodified data
   - `data/processed/` - Cleaned/transformed data
   - `src/data_processing/` - Scripts showing transformations

### Data Quality Standards
- No personally identifiable information (PII)
- Validate against official sources when possible
- Document assumptions and limitations
- Include uncertainty estimates

## 🔍 Peer Review Process

### For Pull Request Authors
- Describe what changed and why
- Link related issues
- Include test results
- Update documentation
- Be responsive to feedback

### For Reviewers
- Check code quality and style
- Verify tests pass
- Assess documentation
- Run code locally
- Provide constructive feedback

## 🎓 Analysis Standards

### Scientific Rigor
- State assumptions explicitly
- Acknowledge limitations
- Provide uncertainty estimates
- Enable reproducibility
- Cite sources properly

### Validation Requirements
For major model changes:
1. Compare with historical data
2. Cross-validate against other markets
3. Sensitivity analysis on key parameters
4. Document validation approach

### Transparency Principles
- All code must be open
- Data sources must be documented
- Methodology must be explained
- Results must be reproducible

## 📢 Communication

### Discussions
Use [GitHub Discussions](https://github.com/yourusername/kc-datacenter-impact/discussions) for:
- Questions about methodology
- Ideas for new features
- General feedback
- Community coordination

### Issues
Use [GitHub Issues](https://github.com/yourusername/kc-datacenter-impact/issues) for:
- Bug reports
- Feature requests
- Documentation improvements
- Data updates

### Direct Contact
For sensitive matters:
- Email: [your-email@example.com]
- LinkedIn: [Your LinkedIn]

## 🏆 Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes
- Academic citations (for significant contributions)
- Community updates

## ❓ Questions?

Not sure where to start? 
- Check [open issues labeled "good first issue"](https://github.com/yourusername/kc-datacenter-impact/labels/good%20first%20issue)
- Read existing code and documentation
- Ask in [Discussions](https://github.com/yourusername/kc-datacenter-impact/discussions)

## 📜 Code of Conduct

### Our Pledge
We pledge to make participation in this project harassment-free for everyone, regardless of:
- Age, body size, disability, ethnicity
- Gender identity and expression
- Level of experience, education
- Nationality, personal appearance, race, religion
- Sexual identity and orientation

### Our Standards

**Positive behaviors:**
- Using welcoming and inclusive language
- Respecting differing viewpoints
- Accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy toward others

**Unacceptable behaviors:**
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Other conduct reasonably considered inappropriate

### Enforcement
Violations can be reported to [your-email@example.com]. All reports will be reviewed and investigated promptly and fairly.

## 🙏 Thank You!

Your contributions make this analysis better for:
- Kansas City residents seeking transparency
- Policymakers making informed decisions
- Journalists investigating impacts
- Researchers extending the work
- Communities facing similar challenges

Together, we can ensure data-driven policy decisions that protect residents while enabling sustainable growth.

---

*Last updated: November 15, 2025*
