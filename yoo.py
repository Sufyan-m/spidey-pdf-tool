import streamlit as st
import pypdf  
import random
import io

# Visual System Configuration
st.set_page_config(page_title="Three Spiderman PDF Tool", page_icon="🕵️‍♂️", layout="centered")

# ==========================================
# NEON SPIDEY SUIT VISUAL ENGINE (CSS)
# ==========================================
st.markdown("""
    <style>
    /* Pure Deep Web Dark Background */
    .main { background-color: #080a10; font-family: 'Segoe UI', sans-serif; }
    
    /* Glowing Spidey Web Red Heading */
    h1 { color: #ff2a2a; text-align: center; font-family: 'Segoe UI', sans-serif; text-shadow: 0 0 15px #ff2a2a, 0 0 5px #00f2fe; margin-bottom: 5px; font-weight: bold; }
    
    /* Interactive SaaS Box (Deep Blue Border with Soft Red Shadow) */
    .saas-box { background-color: #121620; padding: 20px; border-radius: 12px; border: 1px solid #00f2fe; box-shadow: 0 0 12px rgba(229, 9, 20, 0.4); margin-bottom: 25px; color: #f8fafc;}
    .saas-box h3 { color: #00f2fe; text-shadow: 0 0 8px #00f2fe; }
    
    /* Ultimate Spidey Red Action Buttons */
    .stButton>button { background: linear-gradient(90deg, #ff2a2a 0%, #b30000 100%); color: white; font-weight: bold; border-radius: 8px; width: 100%; height: 45px; border: 1px solid #00f2fe; box-shadow: 0 0 12px rgba(255, 42, 42, 0.4); font-size: 16px; }
    .stButton>button:hover { background: linear-gradient(90deg, #b30000 0%, #ff2a2a 100%); color: #00f2fe; transform: scale(1.03); box-shadow: 0 0 20px rgba(0, 242, 254, 0.6); transition: 0.3s ease-in-out; cursor: pointer; }
    
    /* Sidebar Spidey Web Styling */
    [data-testid="stSidebar"] { background-color: #0c101b; border-right: 1px solid #ff2a2a; }
    .stSelectbox label { color: #00f2fe !important; font-weight: bold; text-shadow: 0 0 5px #00f2fe; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1> 🕸️ TRIPLE SPIDEY COMBAT UTILITY 🕷️</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #94a3b8; font-style: italic;'>Zero Configuration // Anonymous Multi-User Token Active 🚀</p>", unsafe_allow_html=True)

# ==========================================
# CENTRAL SPIDER-MAN MOTIVATIONAL QUOTE
# ==========================================
st.markdown("""
<div style='background-color: #1a0f1a; border-left: 5px solid #ff2a2a; padding: 15px; border-radius: 6px; text-align: center; margin-bottom: 20px;'>
    <h4 style='color: #ffaa00; margin: 0;'>🚨 UNCLE BEN'S REAL CODER RULE 🚨</h4>
    <p style='color: #cbd5e1; font-style: italic; margin: 5px 0 0 0;'>
        "With great power comes great responsibility." 💻💀
    </p>
</div>
""", unsafe_allow_html=True)

# 3 Spiderman Options Selection on Sidebar
mode = st.sidebar.selectbox("SELECT YOUR MULTIVERSE AGENT:", [
    "1. Tobey Maguire - Merge Files (Jodna)", 
    "2. Andrew Garfield - Split File (Torna)", 
    "3. Tom Holland - Clear Logs (Kachra Saaf)"
])

# ==========================================
# OPTION 1: TOBEY MAGUIRE (MERGE POV ROAST)
# ==========================================
if "Tobey Maguire" in mode:
    st.markdown("""
    <div class="saas-box">
        <h3>🍕 Tobey Maguire: Old School PDF Fusion Core</h3>
        <p><b>Tobey's POV:</b> "Bhai, main sab se purana aur shareef Spider-Man hoon jo real street fight karta hai aur organic jaalay nikaalta hai. Agar tumhare paas boht saari bikhri hui files hain, toh yahan dump karo. Unhein apne chipchipay jaalon se aisa joroon ga ke Green Goblin bhi dekh kar depression mein chala jaye!"</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_files = st.file_uploader("Yahan apni saari PDF files ek sath upload karo:", type="pdf", accept_multiple_files=True)
    
    if uploaded_files:
        st.success(f"🎯 Target Locked! {len(uploaded_files)} strategic nodes loaded into memory cache.")
        
        if st.button("🍕 Tobey Strike: Join All Assets! 💥"):
            try:
                if hasattr(pypdf, 'PdfMerger'):
                    merger = pypdf.PdfMerger()
                else:
                    merger = pypdf.PdfFileMerger()
                    
                for pdf in uploaded_files:
                    merger.append(pdf)
                    
                output_pdf = io.BytesIO()
                merger.write(output_pdf)
                merger.close()
                output_pdf.seek(0)
                
                st.code("👴 Tobey Maguire: 'Oye hoye, files toh jur gayin! Maine pizza delivery se bhi tez kaam kiya hai. Ab jaldi se download karo warna main chala rent mangne wale landlord se chupne! Bye!'", language="text")
                
                st.balloons() 
                st.success("🔥 FUSION SUCCESSFUL! Loadout compiled perfectly!")
                st.download_button(
                    label="📥 Download Merged PDF Loadout",
                    data=output_pdf,
                    file_name="Tobey_Merged_Loadout.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Glitch Detected during execution: {e}")

# ==========================================
# OPTION 2: ANDREW GARFIELD (SPLIT POV ROAST)
# ==========================================
elif "Andrew Garfield" in mode:
    st.markdown("""
    <div class="saas-box">
        <h3>⚡ Andrew Garfield: Heavy Duty Asset Splitter</h3>
        <p><b>Andrew's POV:</b> "Haan bhai, main wahi hoon jiske skateboard aur Phonk music ke charche hain, aur haan... jiski movie ka third part aaj tak nahi bana (😭). Agar tumhein ek bari file ke tukray karne hain ya specific pages isolated karne hain, toh mujhe batao. Slicing mein mera koi muqabla nahi hai, dukh aur badkismati jo boht jheli hai zindagi mein!"</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Yahan sirf EK target PDF file upload karo:", type="pdf")
    
    if uploaded_file:
        if hasattr(pypdf, 'PdfReader'):
            reader = pypdf.PdfReader(uploaded_file)
        else:
            reader = pypdf.PdfFileReader(uploaded_file)
            
        total_pages = len(reader.pages)
        st.info(f"💡 Total page clusters scanned in memory core: `{total_pages}`")
        
        start_page = st.number_input("Kahan se execution range shuru karni hai?:", min_value=1, max_value=total_pages, value=1)
        end_page = st.number_input("Kahan tak range slice karni hai?:", min_value=1, max_value=total_pages, value=total_pages)
        
        if start_page > end_page:
            st.error("❌ Runtime Latency Error: Starting sector coordinate cannot bypass ending boundary!")
        else:
            if st.button("⚡ Andrew Strike: Breach & Slice Target!"):
                try:
                    if hasattr(pypdf, 'PdfWriter'):
                        writer = pypdf.PdfWriter()
                    else:
                        writer = pypdf.PdfFileWriter()
                        
                    for page_num in range(start_page - 1, end_page):
                        writer.add_page(reader.pages[page_num])
                        
                    output_pdf = io.BytesIO()
                    writer.write(output_pdf)
                    writer.close()
                    output_pdf.seek(0)
                    
                    st.code("💔 Andrew Garfield: 'Pages toh cleanly slice ho gaye... Yeh code safely chal gaya par tumhara dhyan abhi tak parhai se alag kyun chal raha hai? Matric ke baad direct high level hacker banne ka plan hai kya? Download karo aur nikaloo! 🥰'", language="text")
                    
                    st.balloons()
                    st.success("🎉 Slicing operation successful!")
                    st.download_button(
                        label="📥 Download Extracted PDF Asset",
                        data=output_pdf,
                        file_name=f"Andrew_Sliced_Pages_{start_page}_to_{end_page}.pdf",
                        mime="application/pdf"
                    )
                except Exception as e:
                    st.error(f"Glitch Detected during execution: {e}")

# ==========================================
# OPTION 3: TOM HOLLAND (RESET/OTHER POV ROAST)
# ==========================================
elif "Tom Holland" in mode:
    st.markdown("""
    <div class="saas-box">
        <h3>🤖 Tom Holland: Nepo-Baby Cache Evacuation</h3>
        <p><b>Tom's POV:</b> "Hey everyone! Main ameer aur chota Spider-Man hoon jise khud se kuch banana nahi aata, bas Tony Stark ke drones aur high-tech suits use karne aate hain. Agar system mein koi error aa raha hai ya bff ka bheja hua kachra saaf karna hai, toh mere automatic AI system ko bolo, ek click mein poora cache saaf!"</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Bakaya system optimization cache clean karne ke liye Stark button press karein:")
    
    if st.button("🛡️ Tom Strike: Reset Matrix! 💥"):
        st.code("🤖 Tom Holland: 'Mr. Stark! Maine pure system ka kachra saaf kar diya hai! Ab saare memory leaks aur log errors khatam ho gaye hain. Chalo main chala bina dimaag lagaye Avengers ke naye aircrafts urane!'", language="text")
        st.snow()
        st.success("✨ SYSTEM ENVIRONMENT CLEAN! Reload the page to start a new loop.")
