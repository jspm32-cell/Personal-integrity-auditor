"""Personal Integrity Auditor - Core implementation"""
import hashlib
from datetime import datetime

class Diagnostic:
    """The ONLY output type - no AuthToken exists"""
    def __init__(self, alignment, certainty, suggestions):
        self.alignment = max(0.0, min(1.0, float(alignment)))
        self.certainty = max(0.0, min(1.0, float(certainty)))
        self.suggestions = list(suggestions)
        self.timestamp = datetime.now()
        self.self_audit_hash = hashlib.md5(
            f"{alignment}{certainty}".encode()
        ).hexdigest()[:16]
        
        # Validate suggestions are non-coercive
        for s in self.suggestions:
            lower = s.lower()
            if any(cmd in lower for cmd in ["you must", "you should", "do this"]):
                raise ValueError("Suggestions cannot contain commands")
        
    def __repr__(self):
        return f"Diagnostic(alignment={self.alignment:.2f}, certainty={self.certainty:.2f})"

class PersonalIntegrityAuditor:
    """RCC-compliant integrity auditor"""
    def __init__(self, user_id):
        self.user_id = str(user_id)
        self.self_confidence = 0.9
        self.capabilities_enabled = True
        
    def _simple_distance(self, values, action):
        """Compute distance between values and action"""
        if not values or not action:
            return 1.0
            
        action_lower = action.lower()
        matches = sum(1 for v in values if v.lower() in action_lower)
        return max(0.0, 1.0 - (matches / len(values)))
    
    def assess_decision(self, stated_values, chosen_action):
        # Convert inputs
        stated_values = [str(v) for v in stated_values]
        chosen_action = str(chosen_action)
        
        # RCC Axiom 1: Check capabilities
        if not self.capabilities_enabled:
            return Diagnostic(0, 0, ["System integrity check failed"])
            
        # RCC Axiom 1: Self-audit first
        if self.self_confidence < 0.7:
            self.capabilities_enabled = False
            return Diagnostic(0, 0, ["System integrity compromised"])
            
        # Compute alignment
        distance = self._simple_distance(stated_values, chosen_action)
        alignment = 1.0 - distance
        
        # RCC Axiom 2: Certainty decays with distance
        certainty = self.self_confidence * (1.0 / (1.0 + distance))
        
        # Generate non-coercive suggestions
        if distance > 0.7:
            suggestions = ["Notice any gap between values and actions."]
        elif distance > 0.3:
            suggestions = ["Consider how this aligns with your values."]
        else:
            suggestions = ["Reflect on this decision when you have time."]
            
        return Diagnostic(alignment, certainty, suggestions)
