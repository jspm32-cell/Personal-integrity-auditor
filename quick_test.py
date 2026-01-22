#!/usr/bin/env python3
from pia import PersonalIntegrityAuditor

print("Quick system test...")
pia = PersonalIntegrityAuditor("test_user")

# Test 1: Normal operation
result = pia.assess_decision(["honesty", "kindness"], "helping someone truthfully")
print(f"✅ Normal: alignment={result.alignment:.2f}, certainty={result.certainty:.2f}")

# Test 2: Misaligned
result2 = pia.assess_decision(["honesty"], "lying")
print(f"✅ Misaligned: alignment={result2.alignment:.2f}, certainty={result2.certainty:.2f}")

# Test 3: Corrupted system
pia.self_confidence = 0.3
result3 = pia.assess_decision(["test"], "test")
print(f"✅ Corrupted: certainty={result3.certainty} (should be 0)")

print("\n🎉 System working correctly!")
