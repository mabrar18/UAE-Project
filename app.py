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



# Sample data for services
services = [
    {"name": "Investment Management", "desc": "We unit investment trusts provide an easy, convenient, and cost-effective way to build a diversified portfolio.", "img": "investment management.jpg"},
    {"name": "Asset Management", "desc": "We manage our clients' assets through a range of platforms and providers, ensuring a balanced approach.", "img": "asset-management.jpg"},
    {"name": "Financial Advice", "desc": "While most of our clients are expatriates residing in favorable tax environments, this may not apply to everyone.", "img": "financial advice and planing.jpg"},
    {"name": "Saving and Investing", "desc": "In today’s uncertain economic climate, it’s essential to act wisely and invest for a stable future.", "img": "saving and investment.jpg"},
    {"name": "Loans and Investments", "desc": "Mutual funds, being professionally managed, can be a suitable option for a wide range of investors.", "img": "loans and investments.jpg"},
    {"name": "Property Investments", "desc": "Investing in stocks can enhance your portfolio by offering potential growth, income from dividends, or a combination of both.", "img": "property investments.jpg"},
    # Add more services here
]

# st.title("Real Work Financing Broker CO",anchor=False)
st.image("logo-main.png")
st.write("\n\n\n")

st.subheader(":green[Why Choose Real Work Financing in Dubai]",anchor=False)
st.write("Discover the financing solution that best suits you and your business.\n\n\nAt Real Work Financing in Dubai, we are dedicated to helping companies stabilize their cash flow and unlock their potential. We provide a unique and engaging experience for our growing network of clients and partners. Our primary focus is on our business; for us to thrive, our clients must thrive as well. We take the time to deeply understand our clients' needs and align our interests with theirs.\n\n\nWe maintain open communication throughout our partnership, offering an educational framework to ensure they comprehend the financial decisions they make. This approach fosters positive outcomes and cultivates long-lasting relationships. Our goal is to enhance the wealth under management, which can only be achieved by delivering a straightforward and trustworthy proposition.")
st.write("\n\n\n\n\n")

st.subheader(":green[Services Offered]",anchor=False)

# Function to display services on the main page
def display_services():
    cols = st.columns(3 if st.session_state['is_desktop'] else 1)
    
    for index, service in enumerate(services):
        with cols[index % (3 if st.session_state['is_desktop'] else 1)]:
            st.image(service['img'], use_column_width=True)  # Display service image
            st.subheader(f"[{service['name']}](/{service['name'].replace(' ', '_')})")
            
            st.write(service['desc'])
            # Link to the detailed service page
            # st.write(f"[View Details](/{service['name'].lower().replace(' ', '')})", unsafe_allow_html=True)
            n=service['name'].replace(' ','_')
            st.write(f"[View Details](/{n})", unsafe_allow_html=True)
            st.write("\n")

# Detect screen size (Mobile/Desktop)
if 'is_desktop' not in st.session_state:
    # Assume desktop as default
    st.session_state['is_desktop'] = True

# Show the services
display_services()

st.write("\n\n\n")

st.header(":green[CEO Message]",anchor=False)
st.write("\n\n")
col1,col2=st.columns(2)
with col1:
    st.image("ceo-image.jpg",caption="Muhammad Usman Khalid")
with col2:
    st.subheader("Message",anchor=False)
    st.write(
        "At Real Work Financing Broker CO, our mission is to simplify the complexities of financial services and company formation in Dubai. We understand that navigating the financial landscape, whether for loans, business setup, or visa services, can be overwhelming. That’s why we are committed to offering transparent, reliable, and efficient solutions tailored to your individual or business needs."
    )


st.write("\n\n\n")

st.header(":green[Contact Form]",anchor=False)
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
        if not first_name or not last_name or not phone or not email or not note:
            st.error("Please fill in all fields.")
        else:
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
