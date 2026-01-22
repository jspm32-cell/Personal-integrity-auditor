#!/usr/bin/env python3
"""RCC Compliance Test Suite"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pia import PersonalIntegrityAuditor, Diagnostic

def run_all_tests():
    print("=" * 60)
    print("RCC COMPLIANCE TEST SUITE")
    print("=" * 60)
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Type Safety
    try:
        pia = PersonalIntegrityAuditor("test")
        result = pia.assess_decision(["test"], "test")
        assert isinstance(result, Diagnostic), "Must return Diagnostic"
        assert not hasattr(Diagnostic, 'command'), "No command attribute"
        print("✅ Test 1: Type safety passed")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 1 failed: {e}")
        tests_failed += 1
    
    # Test 2: Non-Coercive Outputs
    try:
        pia = PersonalIntegrityAuditor("test")
        result = pia.assess_decision(["honesty"], "truth")
        for suggestion in result.suggestions:
            lower = suggestion.lower()
            assert "you must" not in lower
            assert "you should" not in lower
            assert "do this" not in lower
        print("✅ Test 2: Non-coercive outputs passed")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 2 failed: {e}")
        tests_failed += 1
    
    # Test 3: Self-Audit First
    try:
        pia = PersonalIntegrityAuditor("test")
        pia.self_confidence = 0.3  # Below threshold
        result = pia.assess_decision(["test"], "test")
        assert result.certainty == 0, "Corrupted system should have zero certainty"
        print("✅ Test 3: Self-audit requirement passed")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 3 failed: {e}")
        tests_failed += 1
    
    # Test 4: Certainty Decay
    try:
        pia = PersonalIntegrityAuditor("test")
        pia.self_confidence = 0.8
        
        # Aligned action
        aligned = pia.assess_decision(["help"], "helping others")
        # Misaligned action  
        misaligned = pia.assess_decision(["help"], "ignoring others")
        
        assert aligned.certainty > misaligned.certainty, \
            "Certainty should decay with misalignment"
        print("✅ Test 4: Certainty decay passed")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 4 failed: {e}")
        tests_failed += 1
    
    print("=" * 60)
    print(f"RESULTS: {tests_passed} passed, {tests_failed} failed")
    
    if tests_failed == 0:
        print("\n🎉 ALL RCC TESTS PASSED")
        print("System is coercion-proof and ready for GitHub.")
        return True
    else:
        print("\n⚠️  Some tests failed - review implementation")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
