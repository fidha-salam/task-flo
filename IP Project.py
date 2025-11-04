import pandas as pd
print("Welcome to TaskFlo")
login_desc = input("Are you a Teacher or a Student? ").strip()
login_name = input("Please enter your name: ").strip()
login_id =int(input("Please enter your ID: "))

tchr_df = pd.read_csv("C:\\Users\\fidha\\Downloads\\tchrdf.csv")
tchr_df.columns = tchr_df.columns.str.lower().str.replace(' ', '_')
stu_df = pd.read_csv("C:\\Users\\fidha\\Downloads\\studentdf.csv")
stu_df.columns = stu_df.columns.str.lower().str.replace(' ', '_')
assign_df = pd.read_csv("C:\\Users\\fidha\\Downloads\\assigndf.csv")
assign_df.columns = assign_df.columns.str.lower().str.replace(' ', '_')
print(assign_df['date_date'])
###################################################

if login_desc.lower() == 'teacher':
        print("Hello ", login_name)
        action = int(input("What do you want to do today? upload assignments(1), view all assignments(2): "))
        if action == 1:
            print('Upload assignment')
            pdf_links = []
            num_of_doc = int(input('Enter number of documents to be uploaded: '))
            for i in range(num_of_doc):
                pdflink = input(f'Enter the PDF link for document {i + 1}: ').strip()
                pdf_links.append(pdflink)
            if 'pdf_link' not in assign_df.columns:
                assign_df['pdf_link'] = None
            assign_df.to_csv('C:/Users/fidha/Downloads/assignment_.csv', index=False)
            print("PDF links have been successfully added/updated in the CSV.")
        elif action == 2:
            print('View all assignments')
            print(assign_df)
        else:
            print('Invalid choice!')

###################################################

elif login_desc.lower() == 'student':
        print("Hello ", login_name)
        action = int(input("What do you want to do today? upload assignments(1), view by due date(2), search for an assignment(3): "))
        if action == 1:
            print('Upload assignment')
            pdf_links = []
            num_of_doc = int(input('Enter number of documents to be uploaded: '))
            for i in range(num_of_doc):
                pdflink = input(f'Enter the PDF link for document {i + 1}: ').strip()
                pdf_links.append(pdflink)
            if 'pdf_link' not in assign_df.columns:
                assign_df['pdf_link'] = None
            assign_df.to_csv("C:\\Users\\fidha\\Downloads\\assigndf.csv", index=False)
            print("PDF links have been successfully added/updated in the CSV.")
        elif action == 2:
            due_on = input("Enter due date (YY-MM-DD): ").strip()
            due_df = assign_df[assign_df['date_date'] == due_on]
            if (assign_df['date_date'] == due_on).any():
                print("Assignments due:")
                print(due_df[assign_df['assignment_name', 'date_date']])
            else:
                print("No assignments due on this date.")
        elif action == 3:
            print('Search and filter')
            searching_for = input("Enter file name: ")
            assign_df['assignment_name'] = assign_df['assignment_name'].str.strip().str.lower()
            searching_for = searching_for.strip().lower()
            if searching_for in assign_df['assignment_name'].values:
                print("File found!")
                print(assign_df[assign_df['assignment_name'] == searching_for])
            else:
                print("File not found!")
        else:
            print("Invalid choice!")
    

else:
    print("Invalid login description!")
