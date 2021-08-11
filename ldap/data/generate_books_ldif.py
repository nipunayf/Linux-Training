import pandas

#open input and output files
info = pandas.read_excel('info.xlsx', "Books")
ldif_file = open("Books.ldif", "w")

#iterate each row of the excel file
for i, r in info.iterrows():
	if i==0: pass #skip the heading
	name, doc_id, publisher = r
	ldif_file.write(f"""\
dn: documentIdentifier={doc_id},ou=Books,dc=ltacademy,dc=com
objectClass: document
objectClass: top
documentTitle: {name}
documentIdentifier: {doc_id}
documentPublisher: {publisher}
\n""")

ldif_file.close()
