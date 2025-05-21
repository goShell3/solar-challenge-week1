#!/usr/bin/env python3
"""
Generates markdown report from analysis results
"""

from jinja2 import Template
import yaml

REPORT_TEMPLATE = """
# MoonLight Energy Solutions - {{ country|title }} Analysis

## Key Metrics
- **Peak GHI**: {{ metrics.peak_ghi }} W/m²
- **Optimal Hours**: {{ metrics.optimal_hours|join(', ') }}

## Recommendations
{% for rec in recommendations %}
- {{ rec }}{% endfor %}
"""

def generate_report(country, metrics, recommendations):
    template = Template(REPORT_TEMPLATE)
    return template.render(
        country=country,
        metrics=metrics,
        recommendations=recommendations
    )

# Example usage
if __name__ == '__main__':
    metrics = {'peak_ghi': 950, 'optimal_hours': ['10AM', '11AM', '2PM']}
    recs = ["Prioritize northern regions due to consistent irradiance",
            "Avoid coastal areas during monsoon season"]
    
    report = generate_report('benin', metrics, recs)
    with open('../reports/benin_summary.md', 'w') as f:
        f.write(report)