import streamlit as st
import pandas as pd

def main():
       
        st.sidebar.title('WELOME TO DASHBOARD')
        st.sidebar.subheader("Please select one option")
        df = pd.read_csv('data.csv')
        df1 = pd.read_csv('data1.csv')


        colleges = sorted(df['college_name'].unique())
        college_selected=st.sidebar.selectbox('Please select one college', colleges)
        

        branch = sorted(df['branch'].unique())
        branch_selected=st.sidebar.selectbox('Please select branch', branch)

        st.title("Enter the details")
        
        user_list=['MHT-CET','JEE(Main)']
        exam_type = st.selectbox("Exam type",user_list)
        exam_type1=str(exam_type)    
    
        user_list1= sorted(df['seat_type'].unique())
        seat_type = st.selectbox("Seat type",user_list1)
        seat_type1 = str(seat_type)

        user_list2= sorted(df['branch'].unique())
        branch = st.selectbox("Branch",user_list2)
        branch1 = str(branch)
    

    # Number input example
        percentile = st.number_input("Percentile",step=0.01)

        if st.button("Predict"):
        
            df2 = df[(df['seat_type'] == seat_type1) & (df['score_type'] == exam_type1) & (df['min']<percentile) & (df['branch']==branch1)].loc[:,['college_name']]


            st.write(df2)


        if st.sidebar.button("Show analysis"):
           col1, col2, col3 ,col4 = st.columns(4)
           with col1:
               st.header("Students")
               student=df1[(df1['college_name']==college_selected) & (df1['branch']==branch_selected)].shape[0]
               st.title(student)
           with col2:
                st.header("Males")
                male=df1[(df1['college_name']==college_selected) & (df1['branch']==branch_selected) & (df1['gender']=='M')].shape[0]
                st.title(male)
               
           with col3:
               st.header("Females")
               Female=df1[(df1['college_name']==college_selected) & (df1['branch']==branch_selected) & (df1['gender']=='F')].shape[0]
               st.title(Female)

           with col4:
               st.header("Highest")
               Female=df1[(df1['college_name']==college_selected) & (df1['branch']==branch_selected) & (df1['gender']=='F')]['rank'].min()
               st.title(Female)

           st.header("Exams prefered")
           df3=df1[(df1['college_name']==college_selected) & (df1['branch']==branch_selected)]
           st.bar_chart(df3['score_type'].value_counts(),color='#006400')
           
           st.header("Seats Available")
           df3=df1[(df1['college_name']==college_selected) & (df1['branch']==branch_selected)]
           st.bar_chart(df3['seat_type'].value_counts(),color='#006400')
         
     

      
      




if __name__ == "__main__":
    main()
