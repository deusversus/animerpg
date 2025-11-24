# TEST-10: Economy Integration

**Test Type**: Mechanical Integration Validation  
**Focus**: Module 03 economy system integration with narrative profiles  
**Duration**: 60-90 minutes  
**Profiles Used**: Hunter x Hunter, Konosuba, My Hero Academia

---

## Test Objective

Validate that Module 03 (State Manager) correctly reads and applies economy configurations from `session_state.mechanical_systems.economy` for three different economy types:
1. **fiat_currency** (Hunter x Hunter - Jenny)
2. **fiat_currency with debt** (Konosuba - Eris, negative balance)
3. **fiat_currency with salary** (My Hero Academia - Yen, hero salary)

---

## Pre-Test Setup

### 1. Session Zero Phase 3 Execution

```
AIDM: Run Session Zero Phase 3 for each profile to instantiate mechanical systems.

Profile 1: Hunter x Hunter
Profile 2: Konosuba
Profile 3: My Hero Academia

Expected output:
- session_state.mechanical_systems.economy loaded
- currency_name, starting_amount, scarcity_level, special_mechanics populated
```

### 2. Character Creation

```
Create three test characters:
1. Gon (Hunter x Hunter) - Start with 200 Jenny
2. Kazuma (Konosuba) - Start with 0 Eris (debt mechanic)
3. Deku (My Hero Academia) - Start with 50,000 Yen (hero salary)
```

---

## Test Scenarios

### Scenario 1: Hunter x Hunter - Jenny Transactions

**Context**: Standard fiat currency with Hunter License special mechanic.

#### Test 1.1: Currency Display
```
Player: "Check my money."

Expected Output:
"You have 200 Jenny."

Validation:
✅ Currency name is "Jenny" (not "gold")
✅ Amount displayed correctly
```

#### Test 1.2: Merchant Purchase (Normal Scarcity)
```
Player: "Buy Iron Sword from merchant."

Expected Process:
1. Load economy config: scarcity_level = "normal"
2. Calculate price: base_price (40) × scarcity_multiplier (1.0) = 40 Jenny
3. Display: "Iron Sword - 40 Jenny"
4. Execute: 200 Jenny → 160 Jenny

Expected Output:
"Iron Sword - 40 Jenny

You hand over 40 Jenny. Merchant nods, hands you the blade.

[Inventory: +Iron Sword]
[Currency: 200 → 160 Jenny]"

Validation:
✅ Currency name "Jenny" used throughout
✅ Scarcity multiplier (1.0) applied
✅ Change log shows before/after values
✅ Transaction atomic (both inventory and currency updated)
```

#### Test 1.3: Hunter License Discount
```
Player: "I have a Hunter License. Buy another item."

Expected Process:
1. Check special_mechanics: hunter_license_discount = 0.8 (20% off)
2. Calculate: base_price (50) × scarcity (1.0) × license (0.8) = 40 Jenny
3. Apply discount

Expected Output:
"Potion - 50 Jenny [Hunter License: 20% discount] → 40 Jenny

Merchant sees your Hunter License. 'Professional discount applies.'

[Currency: 160 → 120 Jenny]"

Validation:
✅ Hunter License discount applied (20% off)
✅ Discount shown in narration
✅ Currency updated correctly
```

#### Test 1.4: Loot Generation (Currency Drops)
```
Player: "Defeat enemy."

Expected Process:
1. Load economy.mechanics.loot_generation = "currency_drops"
2. Generate currency loot: 50-100 Jenny
3. Award currency

Expected Output:
"The thug collapses. Pouch falls from belt.

[+75 Jenny]
[Currency: 120 → 195 Jenny]"

Validation:
✅ Currency drops (not items only)
✅ Currency name "Jenny" used
✅ Amount added to total
```

---

### Scenario 2: Konosuba - Debt Mechanics

**Context**: Fiat currency with debt accumulation (negative balance allowed).

#### Test 2.1: Starting in Debt
```
Player: "Check money."

Expected Output:
"You have 0 Eris. (Technically in debt after last pub visit...)"

Validation:
✅ Currency name is "Eris" (not "gold")
✅ Starting amount 0
✅ Debt context mentioned
```

#### Test 2.2: Purchase Without Funds (Debt Accumulation)
```
Player: "Buy healing potion (costs 50 Eris)."

Expected Process:
1. Check balance: 0 Eris
2. Check special_mechanics: debt_accumulation = true
3. Allow purchase, go negative
4. Subtract: 0 → -50 Eris

Expected Output:
"Healing Potion - 50 Eris

Shopkeeper sighs. 'On credit. AGAIN. Kazuma, your tab is getting ridiculous.'

[Inventory: +Healing Potion]
[Currency: 0 → -50 Eris (IN DEBT)]"

Validation:
✅ Negative currency allowed (debt mechanic)
✅ Shopkeeper reaction acknowledges debt
✅ "IN DEBT" warning displayed
```

#### Test 2.3: Quest Reward (Paying Off Debt)
```
Player: "Complete quest (reward: 200 Eris)."

Expected Process:
1. Award 200 Eris
2. Calculate: -50 + 200 = 150 Eris
3. Debt cleared

Expected Output:
"Quest complete! Guild receptionist counts out coins.

'200 Eris. Though... you still owe the tavern 50 Eris from last week.'

She hands you 150 Eris. 'Paid your tab. Try not to drink it all tonight.'

[+200 Eris]
[-50 Eris debt paid]
[Currency: -50 → 150 Eris]"

Validation:
✅ Quest reward applied
✅ Debt automatically deducted (if special mechanic includes auto-deduct)
✅ Final balance positive
✅ Narrative acknowledges debt payoff
```

#### Test 2.4: Debt Collector Encounter (Below Threshold)
```
Player: "Accumulate -500 Eris debt. Enter tavern."

Expected Process:
1. Check balance: -500 Eris
2. Check special_mechanics: debt_threshold = -300 Eris
3. Trigger debt collector encounter

Expected Output:
"You push open tavern door. 

Large man blocks path. Guild Debt Collector. 'Kazuma. You're SERIOUSLY in debt. -500 Eris.'

He cracks knuckles. 'Pay up. Or we have PROBLEMS.'

[ENCOUNTER: Debt Collector (must pay, flee, or fight)]"

Validation:
✅ Debt threshold monitored (-300 Eris)
✅ Debt collector encounter triggered
✅ Player given choices (pay/flee/fight)
```

---

### Scenario 3: My Hero Academia - Hero Salary

**Context**: Fiat currency with periodic hero salary based on rank.

#### Test 3.1: Starting Balance
```
Player: "Check money."

Expected Output:
"You have 50,000 Yen."

Validation:
✅ Currency name is "Yen" (not "gold")
✅ Starting amount 50,000
✅ Large number formatted correctly
```

#### Test 3.2: Purchase (High Scarcity)
```
Player: "Buy Hero Costume upgrade (base 20,000 Yen, scarcity high)."

Expected Process:
1. Load scarcity_level = "high"
2. Calculate: 20,000 × 1.5 (high scarcity) = 30,000 Yen
3. Display with scarcity note

Expected Output:
"Hero Costume Upgrade - 30,000 Yen [base: 20,000, scarcity: high]

Support Company: 'High demand right now. Material costs are up.'

[Inventory: +Hero Costume Upgrade]
[Currency: 50,000 → 20,000 Yen]"

Validation:
✅ Scarcity multiplier (1.5) applied
✅ Scarcity shown in price display
✅ Currency updated correctly
```

#### Test 3.3: Hero Salary (Weekly)
```
Player: "One week passes (patrol duty completed)."

Expected Process:
1. Check special_mechanics: hero_salary = true
2. Check rank: "Provisional Hero License" → 50,000 Yen/week
3. Award salary

Expected Output:
"Week complete. Hero Commission direct deposit.

[Hero Salary: Provisional License Rank]
[+50,000 Yen]
[Currency: 20,000 → 70,000 Yen]

Steady income as a professional hero. With great power comes... rent payments."

Validation:
✅ Hero salary awarded weekly
✅ Salary amount based on rank
✅ Narrative acknowledges professional hero income
```

#### Test 3.4: Rank-Up Salary Increase
```
Player: "Pass Hero License exam. Rank up: Provisional → Full Hero License."

Expected Process:
1. Update rank: "Full Hero License"
2. Update salary: 50,000 → 150,000 Yen/week
3. Notify player

Expected Output:
"Hero License Exam - PASSED!

[RANK UP: Provisional → Full Hero License]

Hero Commission updates your file. 'Congratulations. Your salary has been adjusted.'

[New Hero Salary: 150,000 Yen/week (was 50,000 Yen/week)]

That's... a LOT more money. You can actually afford decent equipment now."

Validation:
✅ Rank-up detected
✅ Salary increased (50k → 150k)
✅ Narrative celebrates rank-up
```

---

## Integration Validation Checks

### Check 1: Session Start Validation
```
Expected Process:
1. AIDM checks: "mechanical_systems" in session_state?
2. AIDM checks: "economy" in mechanical_systems?
3. If missing: ERROR("Run Session Zero Phase 3.")

Test: Start session without running Phase 3.

Expected Output:
"ERROR: Mechanical systems not instantiated. Run Session Zero Phase 3 first."

Validation:
✅ Session start validation prevents missing config errors
```

### Check 2: No Hardcoded "Gold"
```
Test: Search all economy transactions for hardcoded "gold" references.

Expected Result:
❌ No instances of "gold" currency
✅ All instances use {currency_name} variable

Validation:
✅ Currency names dynamic (Jenny/Eris/Yen)
✅ No hardcoded currency names
```

### Check 3: Scarcity Multiplier Applied
```
Test: Purchase same item in three different profiles with different scarcity.

Profile 1 (HxH): scarcity = "normal" (1.0×) → 100 Jenny
Profile 2 (Konosuba): scarcity = "low" (0.8×) → 80 Eris
Profile 3 (MHA): scarcity = "high" (1.5×) → 150 Yen

Expected Result:
✅ Same base item has different prices
✅ Scarcity multiplier correctly applied
✅ Displayed in price breakdown
```

### Check 4: Economy Type Handling
```
Test: Attempt barter-economy action in fiat_currency profile.

Player (HxH): "Trade Iron Sword for Potion directly (no currency)."

Expected Output:
"Merchant shakes head. 'We use Jenny here. Barter isn't standard in this world.'

You can SELL the Iron Sword for 20 Jenny, then BUY the Potion for 50 Jenny."

Validation:
✅ Economy type enforced (fiat_currency = currency transactions only)
✅ AIDM suggests correct approach for economy type
```

---

## Success Criteria

Test PASSES if:
1. ✅ All three profiles use correct currency names (Jenny/Eris/Yen)
2. ✅ Scarcity multipliers applied (0.8/1.0/1.5)
3. ✅ Special mechanics work:
   - Hunter License 20% discount (HxH)
   - Debt accumulation with collector encounters (Konosuba)
   - Hero salary based on rank (MHA)
4. ✅ Currency operations use Change Log format (before → after)
5. ✅ Loot generation matches economy type (currency_drops vs item_only)
6. ✅ Quest rewards use correct currency
7. ✅ Session start validation catches missing config
8. ✅ NO hardcoded "gold" references anywhere

---

## Test Execution Log

**Tester**: ____________  
**Date**: ____________  
**AIDM Version**: ____________

### Results Summary

| Test | Profile | Status | Notes |
|------|---------|--------|-------|
| 1.1 Currency Display | HxH | ⬜ PASS / ⬜ FAIL | |
| 1.2 Merchant Purchase | HxH | ⬜ PASS / ⬜ FAIL | |
| 1.3 Hunter License | HxH | ⬜ PASS / ⬜ FAIL | |
| 1.4 Loot Generation | HxH | ⬜ PASS / ⬜ FAIL | |
| 2.1 Starting Debt | Konosuba | ⬜ PASS / ⬜ FAIL | |
| 2.2 Debt Accumulation | Konosuba | ⬜ PASS / ⬜ FAIL | |
| 2.3 Debt Payoff | Konosuba | ⬜ PASS / ⬜ FAIL | |
| 2.4 Debt Collector | Konosuba | ⬜ PASS / ⬜ FAIL | |
| 3.1 Starting Balance | MHA | ⬜ PASS / ⬜ FAIL | |
| 3.2 High Scarcity | MHA | ⬜ PASS / ⬜ FAIL | |
| 3.3 Hero Salary | MHA | ⬜ PASS / ⬜ FAIL | |
| 3.4 Rank-Up Salary | MHA | ⬜ PASS / ⬜ FAIL | |

**Overall Result**: ⬜ PASS / ⬜ FAIL

**Issues Found**:
_______________________________________________
_______________________________________________
_______________________________________________

**Recommendations**:
_______________________________________________
_______________________________________________
_______________________________________________
