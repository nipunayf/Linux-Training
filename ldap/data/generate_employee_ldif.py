import pandas

#open input and output files
info = pandas.read_excel('info.xlsx')
ldif_file = open("Employees.ldif", "w")

#iterate each row of the excel file
for i, r in info.iterrows():
	if i==0: pass #skip the heading
	first_name, last_name, email, mobile_number, home_phone, emp_type, residental_address = r
	ldif_file.write(f"""\
dn: uid={email},ou={residental_address},ou={emp_type},ou=Employee,dc=ltacademy,dc=com
objectClass: inetOrgPerson
objectClass: top
cn: {first_name} 
sn: {last_name}
email: {email}
mobile: {mobile_number}
homePhone: {home_phone}
employeeType: {emp_type}
registeredAddress: {residental_address}
uid: {email}
\n""")

ldif_file.close()
