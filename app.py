import streamlit as st
import pandas as pd
import os
import time

def check_credentials(username, password):
    try:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        df = pd.read_excel('users.xlsx')  # อ่านจาก root directory
        user_match = df[(df['username'] == username) & (df['password'] == password)]
        return not user_match.empty
    except FileNotFoundError:
        st.error("ไม่พบไฟล์ users.xlsx กรุณาตรวจสอบ path หรือไฟล์")
        return False
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {str(e)}")
        return False

def main():
    st.title("Login Program")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        username = st.text_input("User")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if check_credentials(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login สำเร็จ")
                st.rerun()
            else:
                st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    else:
        st.write(f"User: {st.session_state.username}")
        options = ['Data','PKASM011', 'PKASM012', 'PKASM013', 'PKASM014', 'PKASM015', 'PKASM016', 'PKASM017', 'PKASM018', 'PKASM019', 'PKASM020', 
                                   'PKASM021', 'PKASM022', 'PKASM023', 'PKASM024', 'PKASM025', 'PKASM026', 'PKASM027', 'PKASM028', 'PKASM029', 'PKASM030', 
                                   'PKASM031', 'PKASM032', 'PKASM033', 'PKASM034', 'PKASM035', 'PKASM036', 'PKASM037', 'PKASM038', 'PKASM039', 'PKASM040', 
                                   'PKASM041', 'PKASM042', 'PKASM043', ]
        selected_option = st.selectbox("Select Machine:", options)

        file_cat = ["A","B","C","D"]
        selected_file_cat = st.selectbox("Select File .cat:", file_cat)
        
        if selected_option:
            st.write(f"Machine: {selected_option}")
        
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()

if __name__ == "__main__":
    main()
