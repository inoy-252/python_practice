def calculate_dti(annual_income, monthly_debt):
    if annual_income <= 0:
        return 100.0
    DTI = (monthly_debt / (annual_income / 12)) * 100
    return round(DTI, 1)


def evaluate_credit(credit_score):
    if credit_score >= 750:
        return 40, "excellent"
    elif credit_score >= 670:
        return 30, "good"
    elif credit_score >= 580:
        return 15, "Fair"
    else:
        return 0, "poor"


applicant = {
    "name": "Inoy",
    "annual_income": 75000,
    "monthly_debt": 1200,
    "credit_score": 720,
    "employment_years": 4,
    "loan_amount": 15000,
}


def evaluate_risk_score(applicant):
    credit_pts, credit_tier = evaluate_credit(applicant["credit_score"])
    dti = calculate_dti(applicant["annual_income"], applicant["monthly_debt"])
    if dti < 25:
        dti_pts = 30
    elif dti < 36:
        dti_pts = 20
    elif dti < 50:
        dti_pts = 10
    else:
        dti_pts = 0
    if applicant["employment_years"] >= 5:
        emp_pts = 15
    elif applicant["employment_years"] >= 2:
        emp_pts = 10
    elif applicant["employment_years"] >= 1:
        emp_pts = 5
    else:
        emp_pts = 0
    lti_ratio = (applicant["loan_amount"] / applicant["annual_income"]) * 100
    if lti_ratio <= 20:
        lti_points = 15
    elif lti_ratio <= 40:
        lti_points = 10
    else:
        lti_points = 0
    total_score = credit_pts + dti_pts + emp_pts + lti_points
    auto_rejected = (applicant["credit_score"] < 500) or (dti > 60.0)
    return total_score, dti, credit_tier, auto_rejected


def get_loan_verdict(total_score, auto_rejected):
    if auto_rejected:
        return "REJECTED (Hard Red-Line Triggered: Credit < 500 or DTI > 60%)"
    elif total_score >= 80:
        return "APPROVED (Tier 1: Preferred Rate - 4.5% APR)"
    elif total_score >= 60:
        return "APPROVED (Tier 2: Standard Rate - 8.5% APR)"
    elif total_score >= 45:
        return "CONDITIONAL APPROVAL (Requires a Co-Signer)"
    else:
        return "REJECTED (Risk score too low)"


score, dti, tier, rejected = evaluate_risk_score(applicant)
print("=" * 45)
print("Total Score:", score)
print("DTI:", dti)
print("Credit Tier:", tier)
print("Auto-Rejected:", rejected)
verdict = get_loan_verdict(score, rejected)
print("FINAL VERDICT:", verdict)
print("=" * 45)
