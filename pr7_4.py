days={"MONDAY":44, "TUESDAY":40, "WEDNESDAY":35, "THURSDAY":50, "FRIDAY":55, "SATURDAY":46,"SUNDAY":20}
print("\n",days,"\n")
print("-------TEMPERATURE BETWEEN (40-50) ------")
for i in days:
  if days[i]>=40 and days[i]<=50:
    print(i)
