def final_bill(consultation, laboratory, medicine, room, category):
    total = consultation + laboratory + medicine + room
    discount_rate = {"senior": 0.10, "staff": 0.15, "general": 0}.get(category.lower(), 0)
    return total - total * discount_rate

consultation = float(input("Consultation charges: "))
laboratory = float(input("Laboratory charges: "))
medicine = float(input("Medicine charges: "))
room = float(input("Room charges: "))
category = input("Patient category (senior/staff/general): ")
print("Final bill =", final_bill(consultation, laboratory, medicine, room, category))
