import streamlit as st
import pypdf
import io

st.set_page_config(page_title="Spidey PDF Tool", page_icon="🕸️", layout="centered")

# Load 'Lora' Serif Font from Google Fonts
st.markdown("""
    <style>
    @import url('https://googleapis.com');

    html, body, [class*="css"], h1, h2, h3, p, button, input, label {
        font-family: 'Lora', Georgia, serif !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🕸️ Spidey PDF Tool")
st.caption("Simple PDF merger and splitter — built with Python & Streamlit")

st.info('🚨 Uncle Ben Rule: "With great power comes great responsibility."')

# Sidebar menu
mode = st.sidebar.selectbox(
    "Choose your Spider-Man:",
    [
        "1. Tobey Maguire - Merge PDFs (Jodna)",
        "2. Andrew Garfield - Split PDF (Torna)",
        "3. Tom Holland - Clear Session (Reset)"
    ]
)

# 1. TOBEY MAGUIRE: MERGE PDFs
if "Tobey Maguire" in mode:
    st.subheader("🍕 Tobey Maguire: Merge PDFs")
    st.write('Tobey: "Bhai bikhri hui PDF files yahan daalo, main apne jaalon se sab ko ek bana dunga!"')

    files = st.file_uploader("Upload multiple PDFs:", type="pdf", accept_multiple_files=True)

    if files:
        st.write(f"Selected files: **{len(files)}**")

        if st.button("Merge PDFs"):
            try:
                merger = pypdf.PdfWriter()
                for pdf in files:
                    merger.append(pdf)

                output = io.BytesIO()
                merger.write(output)
                merger.close()
                output.seek(0)

                st.success("Files merge ho gayin! Pizza delivery se bhi tez kaam hua hai.")
                st.balloons()
                st.download_button(
                    label="Download Merged PDF",
                    data=output,
                    file_name="tobey_merged.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Error aa gaya: {e}")

# 2. ANDREW GARFIELD: SPLIT PDF
elif "Andrew Garfield" in mode:
    st.subheader("⚡ Andrew Garfield: Split PDF")
    st.write('Andrew: "Meri third movie toh nahi bani, par tumhari PDF ke tukray zaroor kar dunga."')

    file = st.file_uploader("Upload one PDF:", type="pdf")

    if file:
        reader = pypdf.PdfReader(file)
        total_pages = len(reader.pages)
        st.write(f"Total pages: **{total_pages}**")

        start = st.number_input("Start page:", min_value=1, max_value=total_pages, value=1)
        end = st.number_input("End page:", min_value=1, max_value=total_pages, value=total_pages)

        if start > end:
            st.error("Start page, end page se bada nahi ho sakta!")
        elif st.button("Split PDF"):
            try:
                writer = pypdf.PdfWriter()
                for page in range(start - 1, end):
                    writer.add_page(reader.pages[page])

                output = io.BytesIO()
                writer.write(output)
                writer.close()
                output.seek(0)

                st.success("Pages alag ho gaye! Ab download karo aur parhai pe bhi dhyan dena.")
                st.balloons()
                st.download_button(
                    label="Download Split PDF",
                    data=output,
                    file_name=f"andrew_pages_{start}_to_{end}.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Error aa gaya: {e}")

# 3. TOM HOLLAND: CLEAR / RESET
else:
    st.subheader("🕷️ Tom Holland: Fresh Start")
    st.write('Tom: "Mr. Stark, sab kuch clean kar diya hai! Naya kaam shuru karne ke liye ready hoon."')

    if st.button("Clear & Reset App"):
        st.rerun()
