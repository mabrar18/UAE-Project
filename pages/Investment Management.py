import streamlit as st

# Set the page configuration to wide layout
st.set_page_config(page_title="Real work Financing Broker CO", layout="wide",initial_sidebar_state='collapsed',page_icon="logo.jpg")

# Hide the three dots menu and Streamlit footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.logo("logo.jpg",icon_image="logo.jpg")

st.image("logo-main.png")
st.write("\n\n\n")



st.header("Investment Management")
st.write("\n\n\n")
st.image("investment management.jpg", use_column_width="auto")
st.write("At Real Work Financing Broker CO, we offer comprehensive investment management services tailored to meet the diverse needs of our clients. Our approach focuses on creating well-balanced, diversified portfolios through careful asset allocation and strategic planning. \n\nWhether you're an expatriate or residing in a different tax jurisdiction, our team ensures that your investments are optimized for growth and security. We leverage a variety of platforms and providers to offer personalized investment strategies, always aiming to deliver strong returns while managing risk effectively.")

st.header(":green[Contact Form]")
with st.form("contactform"):
    st.write("Fill the details Below")
    c1,c2=st.columns(2)
    with c1:
        first_name=st.text_input(label="First Name",placeholder="First Name")
    with c2:
        last_name=st.text_input(label="Last Name",placeholder="Last Name")
    c3,c4=st.columns(2)
    with c3:
        phone=st.text_input(label="Phone No.",placeholder="Phone No.")
    with c4:
        email=st.text_input(label="Email",placeholder="Email")
    note=st.text_input(label="Note",placeholder="write your message..")

    submitted=st.form_submit_button("Submit")
    if submitted:
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email="itxabrar7862580@gmail.com"
        reciever_email="investdubai2024@gmail.com"
        password="tpkg yvqp qrlq thai"

        subject=f"New client message!!"
        body=f"Name: {first_name} {last_name}\nEmail: {email}\nPhone: {phone}\n\nUser Note: {note}"

        msg=MIMEMultipart()
        msg["From"]=sender_email
        msg["To"]=reciever_email
        msg["Subject"]=subject
        msg.attach(MIMEText(body,"plain"))

        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        try:
            server.login(sender_email,password)
            server.sendmail(sender_email,reciever_email,msg.as_string())
            st.success("Thanks, Our team will contact you soon!!")
        except:
            pass
        finally:
            server.quit()
        

st.write("\n\n\n\n\n\n\n\n")

st.header(":green[Visit US]",anchor=False)


st.write("🏢 Burjuman Business Tower, 20 Floor-2058 Al Mankool, Bur Dubai U.A.E")

st.write("☎ +971 4 2588721")

st.text("📩 ptigroup-ae@outlook.com")

st.write("[📞 Whatsapp Us](https://wa.me/971042588721)")
st.write("\n\n\n")

    

# Back to main services page
if st.button("Go back to services"):
    st.write("[Back to Services](/)", unsafe_allow_html=True)
