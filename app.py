import streamlit as st

def main():
    st.title("""Multiplication of 2 numbers""")

    one=st.number_input("Enter first_Number")
    two=st.number_input("Enter second number")

    ans=one*two

    st.write(one,"x",two,"=",ans)


if __name__ == '__main__':
    main()
