"""
Token Counter - Accurate Measurement Tool
Uses real token counts from external test to calculate actual ratios
"""

import os
import json
from pathlib import Path

# Real token counts from DanDaDan external test (Claude Sonnet 4.5)
MEASURED_TOKENS = {
    # Instruction modules (Tier 1 loaded in test)
    "00_system_initialization.md": 2016,
    "01_cognitive_engine.md": 3588,
    "02_learning_engine.md": 2909,
    "04_npc_intelligence.md": 2562,
    "10_error_recovery.md": 2847,
    "11_dice_resolution.md": 2341,
    "12_player_agency.md": 3925,
    
    # Schemas (all loaded in test)
    "character_schema.json": 3706,
    "world_state_schema.json": 3675,
    "session_export_schema.json": 3147,
    "npc_schema.json": 6755,
    "memory_thread_schema.json": 4591,
    "power_system_schema.json": 5267,
    "anime_world_schema.json": 5883,
}

def count_words(filepath):
    """Count words in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Simple word count (split on whitespace)
            words = len(content.split())
            return words
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0

def calculate_actual_ratio(filename, filepath):
    """Calculate actual token-to-word ratio using measured data"""
    if filename in MEASURED_TOKENS:
        words = count_words(filepath)
        tokens = MEASURED_TOKENS[filename]
        ratio = tokens / words if words > 0 else 0
        return words, tokens, ratio
    return None, None, None

def analyze_workspace():
    """Analyze all AIDM files and calculate accurate token counts"""
    workspace = Path("c:/Users/admin/Downloads/workspace")
    
    results = {
        "instruction_modules": {},
        "schemas": {},
        "libraries": {},
        "core_files": {},
        "summary": {}
    }
    
    # Analyze instruction modules
    instructions_dir = workspace / "aidm" / "instructions"
    if instructions_dir.exists():
        for filepath in instructions_dir.glob("*.md"):
            words, tokens, ratio = calculate_actual_ratio(filepath.name, filepath)
            if words is not None:
                results["instruction_modules"][filepath.name] = {
                    "words": words,
                    "measured_tokens": tokens,
                    "ratio": round(ratio, 3)
                }
            else:
                # Estimate for unmeasured files using average ratio
                words = count_words(filepath)
                results["instruction_modules"][filepath.name] = {
                    "words": words,
                    "estimated_tokens": "pending",
                    "measured": False
                }
    
    # Analyze schemas
    schemas_dir = workspace / "aidm" / "schemas"
    if schemas_dir.exists():
        for filepath in schemas_dir.glob("*.json"):
            words, tokens, ratio = calculate_actual_ratio(filepath.name, filepath)
            if words is not None:
                results["schemas"][filepath.name] = {
                    "words": words,
                    "measured_tokens": tokens,
                    "ratio": round(ratio, 3)
                }
    
    # Calculate average ratio from measured files
    all_ratios = []
    for category in ["instruction_modules", "schemas"]:
        for file_data in results[category].values():
            if "ratio" in file_data:
                all_ratios.append(file_data["ratio"])
    
    avg_ratio = sum(all_ratios) / len(all_ratios) if all_ratios else 1.0
    
    # Now estimate unmeasured files using this ratio
    for filepath in instructions_dir.glob("*.md"):
        if filepath.name not in MEASURED_TOKENS:
            words = count_words(filepath)
            estimated_tokens = int(words * avg_ratio)
            results["instruction_modules"][filepath.name] = {
                "words": words,
                "estimated_tokens": estimated_tokens,
                "ratio": round(avg_ratio, 3),
                "measured": False
            }
    
    # Summary statistics
    total_instruction_tokens = sum(
        d.get("measured_tokens") or d.get("estimated_tokens", 0) 
        for d in results["instruction_modules"].values()
    )
    total_schema_tokens = sum(
        d.get("measured_tokens", 0) 
        for d in results["schemas"].values()
    )
    
    results["summary"] = {
        "measured_files": len(MEASURED_TOKENS),
        "average_ratio": round(avg_ratio, 3),
        "total_instruction_tokens": total_instruction_tokens,
        "total_schema_tokens": total_schema_tokens,
        "total_system_tokens": total_instruction_tokens + total_schema_tokens,
        "ratio_interpretation": f"1 word = ~{round(avg_ratio, 2)} tokens for AIDM markdown/JSON"
    }
    
    return results

def print_report(results):
    """Print detailed report"""
    print("=" * 80)
    print("ACCURATE TOKEN COUNT ANALYSIS")
    print("Based on Claude Sonnet 4.5 External Test Measurements")
    print("=" * 80)
    print()
    
    # Print measured ratios
    print("MEASURED TOKEN-TO-WORD RATIOS (from external test):")
    print("-" * 80)
    measured_modules = {k: v for k, v in results["instruction_modules"].items() 
                       if v.get("measured_tokens")}
    for filename, data in sorted(measured_modules.items()):
        print(f"{filename:40} {data['words']:>6} words = {data['measured_tokens']:>6} tokens (ratio: {data['ratio']:.3f})")
    
    print()
    for filename, data in sorted(results["schemas"].items()):
        print(f"{filename:40} {data['words']:>6} words = {data['measured_tokens']:>6} tokens (ratio: {data['ratio']:.3f})")
    
    print()
    print("-" * 80)
    print(f"AVERAGE RATIO: {results['summary']['average_ratio']} tokens per word")
    print(f"INTERPRETATION: {results['summary']['ratio_interpretation']}")
    print("-" * 80)
    print()
    
    # Print estimates for unmeasured files
    unmeasured = {k: v for k, v in results["instruction_modules"].items() 
                 if not v.get("measured", True)}
    if unmeasured:
        print("ESTIMATED TOKENS (using average ratio):")
        print("-" * 80)
        for filename, data in sorted(unmeasured.items()):
            print(f"{filename:40} {data['words']:>6} words ≈ {data['estimated_tokens']:>6} tokens")
        print()
    
    # Print summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total Instruction Modules: {results['summary']['total_instruction_tokens']:>8} tokens")
    print(f"Total Schemas:             {results['summary']['total_schema_tokens']:>8} tokens")
    print(f"TOTAL SYSTEM:              {results['summary']['total_system_tokens']:>8} tokens")
    print()
    print(f"External Test Measured:    {87343:>8} tokens (includes CORE, Module 07, overhead)")
    print(f"Our Calculation:           {results['summary']['total_system_tokens']:>8} tokens (13 modules + 7 schemas)")
    print()
    print("NOTE: Difference accounts for CORE_AIDM_INSTRUCTIONS, Module 07 (loaded during")
    print("Session Zero), and system overhead/conversation context.")
    print("=" * 80)

if __name__ == "__main__":
    results = analyze_workspace()
    print_report(results)
    
    # Save results to JSON
    output_file = Path("c:/Users/admin/Downloads/workspace/tools/ACCURATE_TOKEN_COUNTS.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print()
    print(f"Detailed results saved to: {output_file}")
