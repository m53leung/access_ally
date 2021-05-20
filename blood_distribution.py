def distribute_blood(blood, patients):
    # blood = [0.O-, 1.O+, 2.A-, 3.A+, 4.B-, 5.B+, 6.AB-, 7.AB+]
    # patients = [0.O-, 1.O+, 2.A-, 3.A+, 4.B-, 5.B+, 6.AB-, 7.AB+]
    # Maps blood type of patient to which blood types they can accept
    BLOOD_COMPATIBILITY = ((0,), (1, 0), (2, 0), (3, 2, 1, 0), (4, 0), (5, 4, 1, 0), (6, 2, 4, 0), (7, 6, 3, 5, 2, 4, 1, 0))
    # Defines the order that patients should be given blood (O-, O+, A-, B-, A+, B+, AB-, AB+)
    PATIENT_TYPE_ORDER = (0, 1, 2, 4, 3, 5, 6, 7)
    recieved = 0
    for p in PATIENT_TYPE_ORDER:
        for b in BLOOD_COMPATIBILITY[p]:
            if blood[b] >= patients[p]:
                recieved += patients[p]
                blood[b] -= patients[p]
                patients[p] = 0
            else:
                recieved += blood[b]
                patients[p] -= blood[b]
                blood[b] = 0
    return recieved

line1 = input()
line2 = input()
blood = list(map(int, line1.split()))
patients = list(map(int, line2.split()))
print(distribute_blood(blood, patients))
