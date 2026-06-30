# Root Cause Analysis (RCA) Report
**Status:** [x] Completed  [ ] In Progress
**Tracking ID:** QMS-2026-084

---

## 1. Issue Overview
* **Title:** Deviation in Component-X Tensile Strength (Batch #B9921)
* **Date Identified:** June 28, 2026
* **Owner:** Sarah Jenkins (Quality Engineering)
* **Severity:** High (Production Halt)

## 2. Problem Description
* **What happened?** Routine destructive testing of Component-X (Batch #B9921) revealed an average tensile strength of 410 MPa, falling below the minimum engineering specification of 450 MPa.
* **Where did it occur?** Extrusion Line 3, Manufacturing Plant B.
* **Impact:** 1,200 units quarantined; potential 3-day delay on delivery to primary client if recasting is required.

---

## 3. Containment Actions (Immediate Fix)
* **Action Taken:** Implemented physical inventory hold on Batch #B9921. Halts placed on Extrusion Line 3 pending calibration check.
* **Responsible Party:** David Vance (Floor Supervisor)
* **Date Completed:** June 28, 2026

---

## 4. Root Cause Analysis (The 5 Whys)

* **Problem Statement:** Component-X Batch #B9921 failed tensile strength testing specifications.
    * **Why? (Why did the tensile strength fail?):** The polymer molecular chains did not properly cross-link during the curing stage.
    * **Why? (Why was cross-linking insufficient?):** The curing oven temperature fluctuated drastically, dropping to 165°C instead of maintaining the steady required 180°C.
    * **Why? (Why did the oven temperature drop undetected?):** The heating element Zone B failed mid-cycle, and the built-in control panel did not trigger an audible alert.
    * **Why? (Why did the element fail and the alert fail to trigger?):** The element exceeded its duty-cycle lifespan by 400 hours, and the alarm relay logic was accidentally disabled during a software patch update last month.
    * **Why? (Why was the element over-aged and the software bug missed?):** **[ROOT CAUSE]** There is no automated preventive maintenance alert system linking equipment runtime hours to maintenance schedules, and software updates lack a standardized post-deployment regression testing protocol.

---

## 5. Corrective & Preventive Actions (CAPA)
1.  **Replace and Recalibrate:** Replace heating element Zone B and patch the alarm relay code on Line 3. *(Owner: Maintenance / Due: Immediate)*
2.  **Software Validation:** Establish a mandatory software verification checklist for all PLC/Control panel updates. *(Owner: Systems Eng / Due: July 5, 2026)*
3.  **Preventive Maintenance (PM) Integration:** Link oven runtime logs directly to the CMMS (Computerized Maintenance Management System) to auto-generate work orders 50 hours before element expiration. *(Owner: Operations / Due: July 20, 2026)*

## 6. Verification Plan
* **Method:** Run 3 consecutive test batches on Line 3 under continuous thermocouple monitoring. Review alarm logs by intentionally dropping temperature.
* **Sign-off:** __________________________ (Quality Director)