import streamlit as st

def main():
    st.write("""Multiplication of 2 numbers""")

    one=st.number_input("First_Number")
    two=st.number_input("Second number")

    ans=one*two

    st.write(ans)


if __name__ == '__main__':
    main()
