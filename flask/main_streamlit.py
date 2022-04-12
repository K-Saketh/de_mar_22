from flask import Flask,request   # Imported Flask library
import streamlit as st

def hello():
    try:
        st.title('Learning Streamlit')
        stu_name = st.text_input("Student")
        numb = st.text_input("RollNo")
        #return "Oops something went wrong", 400
        result = f"Student name is {stu_name} and Roll number is {numb}"
        #return f"Student name is {stu_name} and Roll number is {numb}"

        if st.button("Print output"):
            st.success(result)
    except Exception as e:
        return f"Error occured with message: {e}"

if __name__ == "__main__":
    #app.run() -----------> Takes port 5000 by default
    #app.run(port = 8000)------> Takes port 8000
    #app.run(host = "0.0.0.0", port = 8000)
    #app.run(host = "0.0.0.0", port = 8000, debug = True)
    hello()