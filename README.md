# Personal Integrity Auditor

[![RCC-Compliant](https://img.shields.io/badge/RCC-Compliant-green)] 
[![Non-Coercive](https://img.shields.io/badge/Non--Coercive-Guaranteed-red)] 
[![Self-Auditing](https://img.shields.io/badge/Self--Auditing-Required-blue)]

A recursive self-auditing system that **collapses rather than harms**.

## ⚠️ What This Is NOT
- NOT for judging/evaluating others
- NOT for compliance or enforcement
- NOT a surveillance or scoring system
- NOT a medical or diagnostic tool

## ✅ What This Is
A personal reflection tool that helps notice gaps between stated values and actions.

## 🔒 Safety Guarantees (Provable)
1. **Cannot issue commands** - only returns reflective questions
2. **Cannot judge others** - only analyzes your own stated values  
3. **Cannot be weaponized** - misuse causes system collapse
4. **All corruption is visible** - no silent failures

## 🚀 Quick Start
```python
from pia import PersonalIntegrityAuditor

pia = PersonalIntegrityAuditor("your_id")
result = pia.assess_decision(
    stated_values=["honesty", "compassion"],
    chosen_action="Told a difficult truth gently"
)

print(f"Alignment: {result.alignment:.2f}")
print(f"Certainty: {result.certainty:.2f}")
print("Suggestions:", result.suggestions)


# Finish the README.md (it got cut off)
cat >> README.md << 'EOF'
# Create LICENSE file
cat > LICENSE << 'EOF'
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2024 Personal Integrity Auditor Project

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as published
 by the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
